# -*- coding: utf-8 -*-
"""
Module: Advanced Output with Native Typing
Demonstrates advanced output in Python 3.12 using:
- Colored output
- Formatted tables
- Logging
- Native type hints
- Pylint-clean code

Author: Marcel Kaled
Date: 2025-09-24
Version: 1.1
"""

import logging

# --- Logging Configuration ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# --- ANSI Color Codes ---


class Colors:

    HEADER: str = "\033[95m"
    OKBLUE: str = "\033[94m"
    OKCYAN: str = "\033[96m"
    OKGREEN: str = "\033[92m"
    WARNING: str = "\033[93m"
    FAIL: str = "\033[91m"
    ENDC: str = "\033[0m"
    BOLD: str = "\033[1m"
    UNDERLINE: str = "\033[4m"


def print_colored(text: str, color: str = Colors.ENDC) -> None:
    """Prints text in the terminal with ANSI color."""
    print(f"{color}{text}{Colors.ENDC}")


def print_table(data: list[dict[str, str]]) -> None:
    """
    Prints a list of dictionaries as a formatted table.

    Args:
        data (list[dict[str, str]]): List of records to display
    """
    if not data:
        logging.warning("No data available to display.")
        return

    headers: list[str] = list(data[0].keys())
    col_widths: dict[str, int] = {
        h: max(len(h), *(len(row[h]) for row in data)) for h in headers
    }

    # Header row
    header_row: str = " | ".join(f"{h:<{col_widths[h]}}" for h in headers)
    print_colored(header_row, Colors.BOLD + Colors.OKBLUE)

    # Separator
    separator: str = "-+-".join("-" * col_widths[h] for h in headers)
    print(separator)

    # Data rows
    for row in data:
        row_text: str = " | ".join(f"{row[h]:<{col_widths[h]}}" for h in headers)
        print(row_text)


def demo_logging() -> None:
    """Demonstrates logging at different levels."""
    logging.debug("Debug message")
    logging.info("Info message")
    logging.warning("Warning message")
    logging.error("Error message")
    logging.critical("Critical message")


def main() -> None:
    """Main demonstration function for advanced output."""
    print_colored("=== Colored Output ===", Colors.HEADER)
    print_colored("Success message", Colors.OKGREEN)
    print_colored("Warning message", Colors.WARNING)
    print_colored("Error message", Colors.FAIL)
    print()

    print_colored("=== Table Output ===", Colors.HEADER)
    data: list[dict[str, str]] = [
        {"Name": "Alice", "Age": "30", "City": "New York"},
        {"Name": "Bob", "Age": "25", "City": "Los Angeles"},
        {"Name": "Carla", "Age": "40", "City": "Chicago"},
    ]
    print_table(data)
    print()

    print_colored("=== Logging Demo ===", Colors.HEADER)
    demo_logging()


# --- Entry Point ---
if __name__ == "__main__":
    main()
