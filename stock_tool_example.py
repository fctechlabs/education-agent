"""Demonstrate a local Python function tool that fetches stock data."""

from __future__ import annotations

import argparse
import csv
import io
import os

import requests
from agents import Agent, Runner, function_tool
from dotenv import load_dotenv


def get_model_name() -> str:
    """Load environment variables and return the configured model name."""
    load_dotenv()
    return os.getenv("OPENAI_MODEL", "gpt-5-mini")


@function_tool
def get_stock_price(ticker: str) -> str:
    """Fetch the current close price from Stooq and return a formatted ticker string."""
    symbol = f"{ticker.lower()}.us"
    url = f"https://stooq.com/q/l/?s={symbol}&f=sd2t2ohlcv&h&e=csv"
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    rows = list(csv.DictReader(io.StringIO(response.text)))
    if not rows or rows[0].get("Close") in (None, "N/D"):
        return f"{ticker.upper()}: price unavailable"
    close_price = rows[0]["Close"]
    return f"{ticker.upper()}: ${close_price}"


def run_stock_example(prompt: str = "What is the current price of BPOP?") -> str:
    """Run a prompt that can call a local function tool."""
    agent = Agent(
        name="stock_tool_educator",
        model=get_model_name(),
        instructions="Use the stock price tool when asked about stock prices.",
        # Local function tools run in this process, not on OpenAI servers.
        tools=[get_stock_price],
    )
    # The tool schema is derived from Python signature + docstring by the SDK.
    # Runner executes the function call locally, then resumes the model with tool output.
    result = Runner.run_sync(agent, prompt)
    return str(result.final_output)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for the stock tool example."""
    parser = argparse.ArgumentParser(description="Run local function tool stock demo.")
    parser.add_argument(
        "--prompt",
        default="What is the current price of BPOP?",
        help="Prompt for the stock tool agent.",
    )
    return parser.parse_args()


def main() -> None:
    """Run the stock tool example from the command line."""
    args = parse_args()
    output = run_stock_example(args.prompt)
    print(output)


if __name__ == "__main__":
    main()
