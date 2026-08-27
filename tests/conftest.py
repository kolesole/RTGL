from io import StringIO

import pandas as pd
import pytest

from rtgl.base import Database, Table
from rtgl.converter import SConverter, TConverter


@pytest.fixture(scope="session")
def test_db():
    r"""The shared schema for the whole test suite: products, users, and their relations.

    Relations (all foreign keys point at the parent's primary key):
        products <- reviews     (reviews.product_id), reviews.user_id -> users   [products-users: 2 hops]
        products <- wishlists   (wishlists.product_id), wishlists.user_id -> users [products-users: 2 hops, ties with reviews route -> ambiguous]
        products <- carts       (carts.product_id), no time_col
        carts <- cart_items     (cart_items.cart_id), cart_items.user_id -> users [carts-users: 2 hops, uniquely shortest]
        products <- notes       (notes.product_id), leaf table, no time_col anywhere on its only path to products
        products <- productMeta (productMeta.product_id, which is also productMeta's own primary
            key -- a one-to-one extension table), no time_col

    product_id=3 ("Gizmo") has no reviews/wishlists/carts/notes rows at all (empty-aggregation-window
    case), but does have a productMeta row with a null priority (present-row-but-null-value case).
    """
    products_data = """
    productId, name
    1,         Widget
    2,         Gadget
    3,         Gizmo
    """
    products_df = pd.read_csv(StringIO(products_data),
                              skipinitialspace=True,
                              na_values=['nan', 'NaN', 'NONE', ''])
    products_table = Table(
        df=products_df,
        fkey_col_to_pkey_table=None,
        pkey_col="productId",
        time_col=None)

    users_data = """
    userId, name
    1,      alice
    2,      bob
    """
    users_df = pd.read_csv(StringIO(users_data),
                           skipinitialspace=True,
                           na_values=['nan', 'NaN', 'NONE', ''])
    users_table = Table(
        df=users_df,
        fkey_col_to_pkey_table=None,
        pkey_col="userId",
        time_col=None)

    reviews_data = """
    reviewId, productId, userId, rating, comment, reviewDate
    1,        1,         1,      5,      OPT,     2025-02-02
    2,        1,         2,      3,      ALG,     2025-02-04
    3,        2,         1,      4,      PRP,     2025-02-03
    4,        1,         1,      nan,    ITM,     2025-02-11
    """
    reviews_df = pd.read_csv(StringIO(reviews_data),
                             skipinitialspace=True,
                             parse_dates=["reviewDate"],
                             na_values=['nan', 'NaN', 'NONE', ''])
    reviews_table = Table(
        df=reviews_df,
        fkey_col_to_pkey_table={"productId": "products", "userId": "users"},
        pkey_col="reviewId",
        time_col="reviewDate")

    carts_data = """
    cartId, productId
    1,      1
    2,      2
    """
    carts_df = pd.read_csv(StringIO(carts_data),
                           skipinitialspace=True,
                           na_values=['nan', 'NaN', 'NONE', ''])
    carts_table = Table(
        df=carts_df,
        fkey_col_to_pkey_table={"productId": "products"},
        pkey_col="cartId",
        time_col=None)

    cart_items_data = """
    itemId, cartId, userId, itemDate
    1,      1,      1,      2025-02-05
    2,      2,      2,      2025-02-06
    """
    cart_items_df = pd.read_csv(StringIO(cart_items_data),
                                skipinitialspace=True,
                                parse_dates=["itemDate"],
                                na_values=['nan', 'NaN', 'NONE', ''])
    cart_items_table = Table(
        df=cart_items_df,
        fkey_col_to_pkey_table={"cartId": "carts", "userId": "users"},
        pkey_col="itemId",
        time_col="itemDate")

    wishlists_data = """
    wishlistId, productId, userId, wishlistDate
    1,          1,         2,      2025-02-07
    2,          2,         1,      2025-02-08
    """
    wishlists_df = pd.read_csv(StringIO(wishlists_data),
                               skipinitialspace=True,
                               parse_dates=["wishlistDate"],
                               na_values=['nan', 'NaN', 'NONE', ''])
    wishlists_table = Table(
        df=wishlists_df,
        fkey_col_to_pkey_table={"productId": "products", "userId": "users"},
        pkey_col="wishlistId",
        time_col="wishlistDate")

    notes_data = """
    noteId, productId, note
    1,      1,         fragile
    2,      2,         popular
    """
    notes_df = pd.read_csv(StringIO(notes_data),
                           skipinitialspace=True,
                           na_values=['nan', 'NaN', 'NONE', ''])
    notes_table = Table(
        df=notes_df,
        fkey_col_to_pkey_table={"productId": "products"},
        pkey_col="noteId",
        time_col=None)

    # one row per product (productId doubles as its own primary key and foreign key), with a
    # nullable numeric column and a non-null string column -- for plain id_dot_id condition
    # tests. product 3 has a null priority, mirroring the "one entity missing a value" shape.
    product_meta_data = """
    productId, priority, category
    1,         3,        AI
    2,         7,        DS
    3,         nan,      SI
    """
    product_meta_df = pd.read_csv(StringIO(product_meta_data),
                                  skipinitialspace=True,
                                  na_values=['nan', 'NaN', 'NONE', ''])
    product_meta_table = Table(
        df=product_meta_df,
        fkey_col_to_pkey_table={"productId": "products"},
        pkey_col="productId",
        time_col=None)

    table_dict = {
        "products"    : products_table,
        "users"       : users_table,
        "reviews"     : reviews_table,
        "carts"       : carts_table,
        "cartItems"   : cart_items_table,
        "wishlists"   : wishlists_table,
        "notes"       : notes_table,
        "productMeta" : product_meta_table}

    return Database(table_dict=table_dict)


@pytest.fixture(scope="session")
def static_converter(test_db):
    return SConverter(db=test_db)


@pytest.fixture(scope="session")
def temporal_converter(test_db):
    timestamps = pd.Series(pd.to_datetime(["2025-02-01", "2025-02-10"]))
    return TConverter(db=test_db, timestamps=timestamps)
