"""Demonstrate hosted web search tool usage with Runner orchestration."""

from __future__ import annotations

import argparse
import os

from agents import Agent, Runner, WebSearchTool
from dotenv import load_dotenv


def get_model_name() -> str:
    """Load environment variables and return the configured model name."""
    load_dotenv()
    return os.getenv("OPENAI_MODEL", "gpt-5-mini")


def run_web_search(prompt: str) -> str:
    """Run a prompt where the model may call a hosted web search tool."""
    agent = Agent(
        name="web_search_educator",
        model=get_model_name(),
        instructions="Use web search when current external information is required.",
        # Hosted tools execute server-side and are available by schema to the model.
        tools=[WebSearchTool()],
    )
    # Runner handles the tool-calling loop: model -> tool call -> tool result -> model rerun.
    result = Runner.run_sync(agent, prompt)
    return str(result.final_output)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for the web search example."""
    parser = argparse.ArgumentParser(description="Run hosted WebSearchTool example.")
    parser.add_argument("--prompt", required=True, help="Prompt for the web-enabled agent.")
    return parser.parse_args()


def main() -> None:
    """Run the web search example from the command line."""
    args = parse_args()
    output = run_web_search(args.prompt)
    print(output)


if __name__ == "__main__":
    main()
