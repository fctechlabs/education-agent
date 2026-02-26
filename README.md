# education-agent

A minimal Python 3.12 teaching repository for the OpenAI Agents SDK.

## What the Agents SDK is

The OpenAI Agents SDK helps you build agent workflows on top of the Responses API.
You define an `Agent` (instructions, model, tools) and run it with `Runner`.
The SDK manages response state, tool schemas, and tool-calling loops.

## How Runner works conceptually

`Runner` is the orchestration layer:

- Sends your input plus agent configuration to the model.
- Detects model-requested tool calls.
- Executes tools (hosted or local, depending on tool type).
- Feeds tool results back to the model.
- Repeats until a final model output is produced.

You usually consume this final text through `result.final_output`.

## How tools are invoked

- **Hosted tools** (like `WebSearchTool`) run server-side.
- **Local function tools** (from `@function_tool`) run in your Python process.
- In both cases, the model decides whether to call a tool based on instructions and prompt.
- `Runner` coordinates calls and resumes the model automatically.

## Agent patterns included here

- **Plain agent**: one prompt, no tools (`basic_example.py`).
- **Structured inputs**: explicit `input_text` items, including file content (`attachment_example.py`).
- **Hosted tools**: server-side web search via `WebSearchTool` (`web_search_example.py`).
- **Local function tools**: Python tool for live BPOP quote via Stooq (`stock_tool_example.py`).

## Setup

1. Install dependencies:

```bash
poetry install
```

2. Configure environment:

```bash
cp .env.example .env
```

3. Set your key in `.env`:

```dotenv
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-5-mini
```

If `OPENAI_MODEL` is omitted, examples default to `gpt-5-mini`.

## Run the unified CLI

```bash
poetry run python main.py basic --prompt "Explain recursion"
poetry run python main.py attachment --prompt "Summarize this file" --file sample.txt
poetry run python main.py web-search --prompt "What happened in AI news today?"
poetry run python main.py stock
```

## Run individual examples

```bash
poetry run python basic_example.py --prompt "Explain recursion"
poetry run python attachment_example.py --prompt "Summarize this file" --file sample.txt
poetry run python web_search_example.py --prompt "What happened in AI news today?"
poetry run python stock_tool_example.py
```

## Install Python 3.12 and Poetry

### macOS

```bash
brew install python@3.12
brew install poetry
python3.12 --version
poetry --version
```

### Linux

```bash
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.12 python3.12-venv python3.12-dev pipx
pipx install poetry
python3.12 --version
poetry --version
```

#### WSL (Linux on Windows)

If you run commands as `python3.12`, set Poetry to use that interpreter by default in this project:

```bash
poetry env use python3.12
poetry run python --version
```

## Requirements

- Sign up on https://platform.openai.com/
- Add 5 dollars to your account.
- SET YOUR LIMIT TO 5 DOLLARS: https://platform.openai.com/settings/organization/limits
- Generate an OpenAI API key and copy it.
