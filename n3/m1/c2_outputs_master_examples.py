# -*- coding: utf-8 -*-
"""
Ultra-Professional Dynamic Table Output
=======================================

Features:
- Terminal tables with dynamic alignment
- Conditional coloring based on user-defined rules
- Logging integration
- Supports multiple data types (str, int, float)
- Native Python 3.12 type hints
- NumPy-style docstrings
- Pylint-clean code

Author: Marcel Kaled
Date: 2025-09-24
Version: 5.1
"""

import logging
from collections.abc import Callable

# ---------------- Logging Configuration ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# ---------------- ANSI Color Codes ----------------


class Colors:
    HEADER: str = "\033[95m"
    OKBLUE: str = "\033[94m"
    OKCYAN: str = "\033[96m"
    OKGREEN: str = "\033[92m"
    WARNING: str = "\033[93m"
    FAIL: str = "\033[91m"
    ENDC: str = "\033[0m"
    BOLD: str = "\033[1m"


# ---------------- Core Functions ----------------
def print_colored(text: str, color: str = Colors.ENDC) -> None:
    """
    Prints colored text to terminal.

    Parameters
    ----------
    text : str
        Text to display.
    color : str
        ANSI color code to apply.
    """
    print(f"{color}{text}{Colors.ENDC}")


def format_cell(
    value: str | int | float,
    width: int,
    color_rule: Callable[[object], str] | None = None,
) -> str:
    """
    Formats a single cell with width and optional color rule.

    Parameters
    ----------
    value : str | int | float
        Cell value.
    width : int
        Column width for alignment.
    color_rule : Callable[[object], str] | None
        Function returning ANSI color code based on value.

    Returns
    -------
    str
        Formatted and colored string for the cell.
    """
    color: str = color_rule(value) if color_rule else Colors.ENDC
    if isinstance(value, (int, float)):
        return f"{color}{value:>{width}}{Colors.ENDC}"
    return f"{color}{str(value):<{width}}{Colors.ENDC}"


def print_dynamic_table(
    data: list[dict[str, str | int | float]],
    color_rules: dict[str, Callable[[object], str]] | None = None,
) -> None:
    """
    Prints a table with dynamic columns, alignment, and optional coloring.

    Parameters
    ----------
    data : list[dict[str, str | int | float]]
        List of rows; each row is a dict with column names as keys.
    color_rules : dict[str, Callable[[object], str]] | None
        Optional dict mapping column names to functions returning ANSI color codes.
    """
    if not data:
        logging.warning("No data available for table.")
        return

    headers: list[str] = list(data[0].keys())
    col_widths: dict[str, int] = {
        h: max(len(h), *(len(str(row[h])) for row in data)) for h in headers
    }

    # Header row
    header_row: str = " | ".join(f"{h:<{col_widths[h]}}" for h in headers)
    print_colored(header_row, Colors.BOLD + Colors.OKBLUE)
    print("-+-".join("-" * col_widths[h] for h in headers))

    # Data rows
    for row in data:
        row_items: list[str] = [
            format_cell(
                row[h], col_widths[h], color_rules.get(h) if color_rules else None
            )
            for h in headers
        ]
        print(" | ".join(row_items))


# ---------------- Color Rules ----------------
def score_color(value: float) -> str:
    """Returns color code based on score."""
    if value >= 90:
        return Colors.OKGREEN
    if value >= 70:
        return Colors.WARNING
    return Colors.FAIL


def age_color(value: int) -> str:
    """Returns color code based on age."""
    if value < 25:
        return Colors.OKCYAN
    if value > 35:
        return Colors.WARNING
    return Colors.ENDC


# ---------------- Main ----------------
def main() -> None:
    """
    Demonstrates ultra-professional dynamic table output with conditional coloring and logging.
    """
    print_colored("=== Ultra-Professional Dynamic Table ===", Colors.HEADER)

    data: list[dict[str, str | int | float]] = [
        {"Name": "Alice", "Age": 30, "Score": 95.5},
        {"Name": "Bob", "Age": 25, "Score": 88.2},
        {"Name": "Carla", "Age": 40, "Score": 65.0},
        {"Name": "David", "Age": 22, "Score": 72.5},
    ]

    color_rules: dict[str, Callable[[object], str]] = {
        "Score": score_color,
        "Age": age_color,
    }

    print_dynamic_table(data, color_rules)
    print()

    logging.info("Dynamic table printed successfully.")


# ---------------- Entry Point ----------------
if __name__ == "__main__":
    main()
