You are Codex operating inside a fresh git repository.

Build a public teaching repository named "education-agent".

GOAL
Create a minimal but instructional Python 3.12 project (Poetry-based) that demonstrates how to use the OpenAI Agents SDK (Python). The repository must teach fundamentals and internals — not just usage.

This repo must include:

1) The most basic possible agent example
2) A text file attachment example
3) A web search tool example (using SDK hosted WebSearchTool)
4) A custom function tool example (fetching current stock price for BPOP from a free public endpoint)
5) A final unified CLI entrypoint (main.py) that integrates all of the above

This is a teaching repository. Code must be readable, annotated, and minimal.

---

# TECHNICAL REQUIREMENTS

## Environment

- Python 3.12
- Poetry project
- Use `.env` for:
  - OPENAI_API_KEY
  - OPENAI_MODEL (default to "gpt-5-mini" if not set)

Do NOT hardcode secrets.

---

# PROJECT STRUCTURE

.
├── README.md
├── pyproject.toml
├── .env.example
├── basic_example.py
├── attachment_example.py
├── web_search_example.py
├── stock_tool_example.py
└── main.py

No tests. No CI.

---

# IMPLEMENTATION DETAILS

## 1. Basic Agent Example (basic_example.py)

Demonstrate:

- `Agent`
- `Runner.run_sync()`
- Accessing `result.final_output`

Instructions:
"You are a concise educational assistant. If unsure, say so."

It must clearly show:
- How the Agent is constructed
- What the Runner does
- Where the final output comes from

Keep it extremely minimal.

---

## 2. Attachment Example (attachment_example.py)

Goal:
Demonstrate structured input items and file-based grounding.

Behavior:
- Accept CLI args:
  --prompt
  --file path/to/text.txt

Implementation:
- Read the text file
- Build input items:
  - one `input_text` with the user prompt
  - one `input_text` with the file content (labeled as file content)
- Pass list of structured items into Runner

Add comments explaining:
- Why structured inputs exist
- How Agents SDK passes these into the Responses API

Do NOT over-engineer.

---

## 3. Web Search Tool Example (web_search_example.py)

Use:
from agents import WebSearchTool

Create agent:
tools=[WebSearchTool()]

Demonstrate:
- Tool calling loop
- Automatic tool execution handled by Runner

Add comments explaining:
- That hosted tools run server-side
- The model decides when to call them
- Runner orchestrates tool calls and reruns

Keep example minimal but real.

---

## 4. Custom Tool Example (stock_tool_example.py)

Implement a function tool:

Name: get_stock_price
Input: ticker: str
Output: string (ticker + current price)

Use free endpoint:
https://stooq.com/q/l/?s=bpop.us&f=sd2t2ohlcv&h&e=csv

Implementation:
- Use requests
- Parse CSV
- Extract close price
- Return formatted string:
  "BPOP: $<price>"

Create agent:
tools=[FunctionTool(...) or @function_tool decorator]

Prompt:
"What is the current price of BPOP?"

Explain in comments:
- Difference between hosted tools and local function tools
- How the tool schema is derived
- How the Runner loop executes the function and resumes the agent

---

## 5. Unified CLI (main.py)

Use argparse.

Subcommands:
- basic
- attachment
- web-search
- stock

Each subcommand should call the corresponding example logic.

Usage examples in README:
poetry install
poetry run python main.py basic --prompt "Explain recursion"
poetry run python main.py attachment --prompt "Summarize this file" --file sample.txt
poetry run python main.py web-search --prompt "What happened in AI news today?"
poetry run python main.py stock

---

# README CONTENT

Must include:

- What the Agents SDK is
- How Runner works conceptually
- How tools are invoked
- Difference between:
  - plain agent
  - structured inputs
  - hosted tools
  - local function tools
- Setup instructions:
  - poetry install
  - copy .env.example to .env
  - set OPENAI_API_KEY
- Exact run commands

README should be educational but concise.

---

# CODE QUALITY RULES

- Use type hints
- Keep files under 150 lines
- Add meaningful inline comments explaining internals
- No unnecessary abstractions
- No tests
- No GitHub Actions
- Keep dependency list minimal:
  - openai-agents
  - python-dotenv
  - requests

---

# FINAL CHECKLIST

Before finishing, verify:

- Poetry project runs
- All four examples execute independently
- main.py integrates all modes
- No API keys required except OpenAI
- BPOP price fetch works without credentials
- Model defaults to gpt-5-mini if OPENAI_MODEL not set

This is a teaching repo for engineers learning agent internals. Keep it sharp and clean.