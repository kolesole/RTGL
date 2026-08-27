"""Diagnostics module for collecting and reporting RTGL syntax and validation issues."""

import warnings
from typing import override

from antlr4.error.ErrorListener import ErrorListener


class Colors:
    r"""ANSI color codes for terminal output formatting."""

    DEFAULT = "\033[0m"
    RED = "\033[31m"
    YELLOW = "\033[33m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class RTGLValidationError(Exception):
    r"""Custom exception for RTGL validation errors."""
    pass


class Error(Exception):
    r"""Represents a single syntax or validation error.

    Stores the location and message of an error that occurred during
    parsing or validation of a RTGL query.
    """

    def __init__(self, line: int, column: int, message: str) -> None:
        r"""Initialize an *`Error`* object.

        Args:
            line (int): Line number of the error.
            column (int): Column number of the error.
            message (str): Error message.

        Returns:
            out (None):
        """
        self.line = line
        self.column = column
        self.message = message

    def __str__(self) -> str:
        r"""Format the error as a colored string for terminal output.

        Returns:
            out (str): Formatted error string with ANSI color codes.
        """
        location = f" at line {self.line}:{self.column} -" if self.line else ""

        return (
            f"{Colors.RED}{Colors.BOLD}[ERROR]{Colors.DEFAULT}"
            f"{location} {self.message}"
        )


class Warning(UserWarning):
    r"""Represents a single warning message.

    Stores the location and message of a warning that occurred during
    parsing or validation of a RTGL query.
    """

    def __init__(self, message: str) -> None:
        r"""Initialize a *`Warning`* object.

        Args:
            message (str): Warning message.

        Returns:
            out (None):
        """
        self.message = message

    def __str__(self) -> str:
        r"""Format the warning as a colored string for terminal output.

        Returns:
            out (str): Formatted warning string with ANSI color codes.
        """
        return (
            f"{Colors.YELLOW}{Colors.BOLD}[WARN]{Colors.DEFAULT}"
            f" {self.message}"
        )


class IssueCollector(ErrorListener):
    r"""Collects syntax and validation errors during parsing.

    Implements ANTLR ErrorListener interface to capture syntax errors during
    parsing, and provides additional methods for collecting validation errors.
    """

    def __init__(self) -> None:
        r"""Initialize the *`IssueCollector`* with empty warnings and errors lists.

        Returns:
            out (None):
        """
        super().__init__()
        self.warnings = []
        self.errors = []

    def has_warnings(self) -> bool:
        r"""Check if any warnings have been collected.

        Returns:
            out (bool): True if there are warnings, False otherwise.
        """
        return len(self.warnings) > 0

    def has_errors(self) -> bool:
        r"""Check if any errors have been collected.

        Returns:
            out (bool): True if there are errors, False otherwise.
        """
        return len(self.errors) > 0

    @override
    def syntaxError(self, recognizer: any, offendingSymbol: any, line: int, column: int, msg: str, e: any) -> None:
        r"""Handle a syntax error reported by the ANTLR parser during parsing.

        Args:
            recognizer (any): The parser instance.
            offendingSymbol (any): The token that caused the error.
            line (int): Line number of the error.
            column (int): Column number of the error.
            msg (str): Error message from ANTLR.
            e (any): The recognition exception (if any).

        Returns:
            out (None):
        """
        self.add_error(line, column, msg)

    def add_warning(self, msg: str) -> None:
        r"""Add a warning message to the collection.

        Used by validators to report non-critical issues (e.g., existence of multiple paths between tables).

        Args:
            msg (str): Warning message.

        Returns:
            out (None):
        """
        self.warnings.append(Warning(msg))

    def add_error(self, line: int, column: int, msg: str) -> None:
        r"""Add a validation error to the collection.

        Used by validators to report semantic errors (e.g., referencing non-existent tables or columns).

        Args:
            line (int): Line number of the error.
            column (int): Column number of the error.
            msg (str): Error message.

        Returns:
            out (None):
        """
        self.errors.append(Error(line, column, msg))

    def report(self, after_syntax_validation: bool=True) -> None:
        r"""Print all warnings and raise an exception if errors exist.

        Args:
            after_syntax_validation (bool): Whether this report is issued after
                syntax validation (True) or semantic validation (False). Only
                affects the wording used for errors.

        Returns:
            out (None):
        """
        type = "syntax" if after_syntax_validation else "semantic"

        if self.has_warnings():
            unique_warnings = sorted({str(w) for w in self.warnings})
            num_warnings = len(unique_warnings)

            warning_summary = (
                f"{Colors.YELLOW}{Colors.BOLD}{Colors.UNDERLINE}"
                f"Validation completed with {num_warnings} {type} warning(s)"
                f"{Colors.DEFAULT}:"
            )

            with warnings.catch_warnings():
                warnings.formatwarning = (
                    lambda message, category, filename, lineno, line=None: f"{message}\n"
                )
                warnings.warn(warning_summary, stacklevel=4)

                warnings.formatwarning = (
                    lambda message, category, filename, lineno, line=None: f"{filename}:{lineno}: {message}\n"
                )
                for warning in unique_warnings:
                    warnings.warn(warning, stacklevel=4)

        if self.has_errors():
            num_errors = len(self.errors)
            error_messages = "\n".join(str(err) for err in self.errors)
            self.clear()

            raise RTGLValidationError(
                f"\n{Colors.RED}{Colors.BOLD}{Colors.UNDERLINE}Validation failed with {num_errors} {type} error(s)"
                f"{Colors.DEFAULT}:\n{error_messages}"
            )
        
        self.clear()

    def clear(self) -> None:
        r"""Clear all collected warnings and errors from the collector.

        Returns:
            out (None):
        """
        self.warnings.clear()
        self.errors.clear()
