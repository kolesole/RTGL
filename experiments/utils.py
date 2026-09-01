import sys
from pathlib import Path

import pandas as pd
import numpy as np

from relbench.base import BaseTask, Dataset, TaskType
from relbench import load_dataset

from rtgl.converter import TConverter


sys.path.append(str(Path(__file__).parent.parent))


def load_dataset_rb(name: str) -> Dataset:
    return load_dataset(name)


def load_task_rb(dataset: Dataset, task_name: str) -> BaseTask:
    return dataset.load_task(task_name)

def get_timestamps(dataset: Dataset, 
                   timedelta: pd.Timedelta, 
                   num_eval_timestamps: int, 
                   split: str) -> "pd.Series[pd.Timestamp]":
    db = dataset.get_db(upto_test_timestamp=(split != "test"))

    if split == "train":
        start = dataset.val_timestamp - timedelta
        end = db.min_timestamp
        freq = -timedelta
    elif split == "val":
        start = dataset.val_timestamp
        end = min(
            dataset.val_timestamp
            + timedelta * (num_eval_timestamps - 1),
            dataset.test_timestamp - timedelta,
            )
        freq = timedelta
    elif split == "test":
        start = dataset.test_timestamp
        end = min(
            dataset.test_timestamp
            + timedelta * (num_eval_timestamps - 1),
            db.max_timestamp - timedelta,
            )
        freq = timedelta
    else:
        pass

    timestamps = pd.date_range(start=start, end=end, freq=freq)
    return timestamps


def process_df_rb(df_rb: pd.DataFrame,
                  fk: str,
                  timestamp: str,
                  label: str) -> pd.DataFrame:
    renamed_df_rb = df_rb.rename(columns={fk: 'fk',
                                          timestamp: 'timestamp',
                                          label: 'label'})
    df_rb = renamed_df_rb.sort_values(by=['timestamp', 'fk'])

    df_rb['timestamp'] = df_rb['timestamp']

    return df_rb


def merge_dataframes(df_rb: pd.DataFrame,
                     df_rtgl: pd.DataFrame) -> None:
    # normalization if LIST_DISTINCT was used in the query
    def normalize(x):
        if isinstance(x, (list, np.ndarray, tuple)):
            return tuple(sorted(x))
        elif isinstance(x, (float, np.floating)):
            return round(float(x), 4)
        
        return x

    df_rb['label'] = df_rb['label'].apply(normalize)
    df_rtgl['label'] = df_rtgl['label'].apply(normalize)

    merged = pd.merge(
        df_rb,
        df_rtgl,
        on=['fk', 'timestamp', 'label'],
        how='outer',
        suffixes=('_rb', '_rtgl'),
        indicator=True
    )

    print(f"Only in RelBench:\n {merged[merged['_merge'] == 'left_only']}")
    print(f"Only in RTGL:\n {merged[merged['_merge'] == 'right_only']}")
    print(f"In both:\n {merged[merged['_merge'] == 'both']}")


def check_correctness(dataset: Dataset,
                      task: BaseTask,
                      rtgl_query: str,
                      split: str) -> None:

    if task.task_type == TaskType.RECOMMENDATION:
        fk_col_name = task.src_entity_col
        label_col_name = task.dst_entity_col
    else:
        fk_col_name = task.entity_col
        label_col_name = task.target_col
    timestamp_col_name = task.time_col

    timestamps = get_timestamps(dataset, task.timedelta, task.num_eval_timestamps, split)

    print(f"TIMEDELTA: {task.timedelta}")
    print(f"NUM_EVAL_TIMESTAMPS: {task.num_eval_timestamps}")

    converter = TConverter(dataset.get_db(upto_test_timestamp=(split != "test")), timestamps)
    table_rb = task.get_table(split, mask_input_cols=False)
    df_rb = process_df_rb(table_rb.df, fk_col_name, timestamp_col_name, label_col_name)
    table_rtgl = converter.convert(rtgl_query, execute=True)
    df_rtgl = table_rtgl.df

    print(f"------------------- START {split.upper()} -------------------")
    print(f"RelBench fkeys: {table_rb.fkey_col_to_pkey_table}")
    print(f"RelBench pkey: {table_rb.pkey_col}")
    print(f"RelBench time col: {table_rb.time_col}")
    print(f"RTGL fkeys: {table_rtgl.fkey_col_to_pkey_table}")
    print(f"RTGL pkey: {table_rtgl.pkey_col}")
    print(f"RTGL time col: {table_rtgl.time_col}")
    merge_dataframes(df_rb, df_rtgl)
    print(f"------------------- END {split.upper()} ---------------------")