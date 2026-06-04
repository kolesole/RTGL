"""Helper utilities for RTGL showcase notebooks."""

from antlr4 import CommonTokenStream, InputStream, TerminalNode

from rtgl.base import Database
from rtgl.converter import Converter, SConverter, TConverter
from rtgl.parser.gen.LexerRTGL import LexerRTGL
from rtgl.parser.gen.ParserRTGL import ParserRTGL
from rtgl.visitor import Visitor


def print_tree(node, parser):

    space = '  '

    if isinstance(node, TerminalNode):
        print(f"{space}Terminal: {node.getText()} ({parser.symbolicNames[node.getSymbol().type]})")
    else:
        rule_name = parser.ruleNames[node.getRuleIndex()]
        print(f"{space}Rule: {rule_name}")
        for child in node.getChildren():
            print_tree(child, parser)

def parse_query(query: str):
    input_stream = InputStream(query)
    lexer = LexerRTGL(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ParserRTGL(token_stream)

    tree = parser.query()

    print("=== Input Query ===")
    print(query)
    print("=== Parse Tree ===")
    print_tree(tree, parser)
    visitor = Visitor()
    print(visitor.visit(tree))
    print("==================")

    return tree

class ConverterShowcaseHelper:
    rtgl_converter: Converter

    def __init__(self, db: Database, timestamps=None):

        if timestamps is not None:
            self.rtgl_converter = TConverter(db, timestamps)
        else:
            self.rtgl_converter = SConverter(db)

    def convert_query(self, query):
        print("========================================")
        print(query)
        table = self.rtgl_converter.convert(query, execute=True)
        print(table)
        print("========================================")

