"""Provide a unified CLI that dispatches each teaching example."""

from __future__ import annotations

import argparse

from attachment_example import run_attachment
from basic_example import run_basic
from stock_tool_example import run_stock_example
from web_search_example import run_web_search


def build_parser() -> argparse.ArgumentParser:
    """Create the top-level parser and all subcommands."""
    parser = argparse.ArgumentParser(description="OpenAI Agents SDK teaching CLI.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    basic_parser = subparsers.add_parser("basic", help="Run minimal agent example.")
    basic_parser.add_argument("--prompt", required=True, help="Prompt to send to the agent.")

    attachment_parser = subparsers.add_parser(
        "attachment", help="Run structured input + file grounding example."
    )
    attachment_parser.add_argument("--prompt", required=True, help="Prompt to ask the agent.")
    attachment_parser.add_argument("--file", required=True, help="Path to a text file.")

    search_parser = subparsers.add_parser("web-search", help="Run hosted web search example.")
    search_parser.add_argument("--prompt", required=True, help="Prompt for the search agent.")

    stock_parser = subparsers.add_parser("stock", help="Run local function tool example.")
    stock_parser.add_argument(
        "--prompt",
        default="What is the current price of BPOP?",
        help="Prompt for the stock tool agent.",
    )
    return parser


def main() -> None:
    """Parse CLI args and run the selected example implementation."""
    args = build_parser().parse_args()
    if args.command == "basic":
        output = run_basic(args.prompt)
    elif args.command == "attachment":
        output = run_attachment(args.prompt, args.file)
    elif args.command == "web-search":
        output = run_web_search(args.prompt)
    else:
        output = run_stock_example(args.prompt)
    print(output)


if __name__ == "__main__":
    main()
