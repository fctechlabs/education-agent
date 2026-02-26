"""Demonstrate the smallest useful Agent + Runner flow."""

from __future__ import annotations

import argparse
import os

from agents import Agent, Runner
from dotenv import load_dotenv


def get_model_name() -> str:
    """Load environment variables and return the configured model name."""
    load_dotenv()
    return os.getenv("OPENAI_MODEL", "gpt-5-mini")


def run_basic(prompt: str) -> str:
    """Run a single-turn prompt and return the model's final text output."""
    agent = Agent(
        name="basic_educator",
        model=get_model_name(),
        instructions="You are a concise educational assistant. If unsure, say so.",
    )
    # Runner executes the model loop and normalizes the final response text.
    result = Runner.run_sync(agent, prompt)
    return str(result.final_output)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for the basic example."""
    parser = argparse.ArgumentParser(description="Run the minimal Agents SDK example.")
    parser.add_argument("--prompt", required=True, help="Prompt to send to the agent.")
    return parser.parse_args()


def main() -> None:
    """Run the basic example from the command line."""
    args = parse_args()
    output = run_basic(args.prompt)
    print(output)


if __name__ == "__main__":
    main()
