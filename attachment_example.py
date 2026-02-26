"""Demonstrate structured inputs with file-grounded context."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Any

from agents import Agent, Runner
from dotenv import load_dotenv


def get_model_name() -> str:
    """Load environment variables and return the configured model name."""
    load_dotenv()
    return os.getenv("OPENAI_MODEL", "gpt-5-mini")


def build_structured_input(prompt: str, file_content: str) -> list[dict[str, Any]]:
    """Build explicit input items that map directly to Responses API content blocks."""
    # Structured inputs make each content item explicit instead of flattening into one string.
    return [
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": prompt},
                {"type": "input_text", "text": f"File content:\n{file_content}"},
            ],
        }
    ]


def run_attachment(prompt: str, file_path: str) -> str:
    """Run a prompt grounded by text file contents."""
    file_content = Path(file_path).read_text(encoding="utf-8")
    agent = Agent(
        name="attachment_educator",
        model=get_model_name(),
        instructions="Use the provided file content when answering the user.",
    )
    # Runner forwards this list of structured items into the underlying Responses API input.
    result = Runner.run_sync(agent, build_structured_input(prompt, file_content))
    return str(result.final_output)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for the attachment example."""
    parser = argparse.ArgumentParser(description="Run file-grounded structured input demo.")
    parser.add_argument("--prompt", required=True, help="Prompt to ask the agent.")
    parser.add_argument("--file", required=True, help="Path to a text file.")
    return parser.parse_args()


def main() -> None:
    """Run the attachment example from the command line."""
    args = parse_args()
    output = run_attachment(args.prompt, args.file)
    print(output)


if __name__ == "__main__":
    main()
