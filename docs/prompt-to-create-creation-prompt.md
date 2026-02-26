User:
I want to create a new repository. This product is the education-agent. I'm using this as a public repository to show my team how to work with agents, specifically the python agents sdk from OpenAI. https://openai.github.io/openai-agents-python/.

I'd like to create a simple repository they can clone and work from. In it, i'd like to have the most basic agent possible. from there I'd like to have 3 sample improvements, the first is attachments (text, image, other). The second is web search as a tool, the third is a custom API call as a tool(perhaps some way to find the stock value of Popular Bank) Think deeply and ask me any questions you might need in order to accomplish this

I want you to ask those questions then help me generate a prompt I gave give to Codex . at the end of the questions, provide me the prompt and a transcription of our full chat so they understand the workflow I used to get the prompt.

Assistant:
Questions I need from you (so the repo is actually usable by your team)

1) Python + env manager
- Python version you want to standardize on (3.10? 3.11? 3.12?)
- Do you want uv, poetry, or plain pip + venv?

2) “Basic agent” scope
- Should the “basic agent” be single-file (main.py) or a tiny package (src/education_agent/…)?
- Do you want a CLI entrypoint (python -m … / education-agent …) or “run this file”?

3) Model choice
- Which default model should the examples use (and should it be an env var override)?
  - If you don’t care, I’ll default to a modern general model and make it configurable via OPENAI_MODEL.

4) Attachments demo: what should it do?
- When a user attaches:
  - text file → should the agent summarize it? extract action items? answer questions grounded in it?
  - image → should it describe the image? extract text? answer a question about it?
  - other file (pdf/csv/etc.) → do you want it simply passed through as an input_file (demo), or parsed locally for something deterministic?

5) Web search demo
- Do you want to use the SDK’s hosted WebSearchTool (simplest) or a “local tool” that calls a search API?
  - I strongly recommend hosted WebSearchTool for the education repo because it’s minimal and shows the canonical pattern.

6) Custom API tool demo: “Popular Bank stock value”
- Confirm this is fine: use Popular, Inc. ticker BPOP (NASDAQ).
- Should the tool return price only, or also day change / market cap / timestamp?
- Do you want the tool to call a free endpoint (e.g., Stooq) or require an API key (Alpha Vantage / Polygon)?
  - If you want zero keys, I’ll pick a free source and add a warning about rate limits.

7) Testing + CI
- Do you want basic pytest tests for the tools and input builders?
- Add GitHub Actions CI (lint + tests) or keep it lean?

8) “3 sample improvements” structure
- Prefer:
  - examples/01_basic_agent.py, 02_attachments.py, 03_web_search.py, 04_custom_tool.py
  - or progressive branches/tags?

9) Team teaching goal
- Is your objective “copy/paste patterns” or “teach internals”?
  - If copy/paste: I’ll prioritize small runnable scripts.
  - If internals: I’ll add a short “how Runner loop works” section.

Assistant:
(Also provided: a first-pass Codex prompt + a brief transcript block, noting that answering the above questions would tighten the prompt further.)

User:
1. 3.12 with poetry
2. lets aim for a single main.py. I do want a CLI entrypoint
3. We're going to provide the model and the apikey via a .env file. gpt-5-mini should be the default.
4. Lets aim for a text file
5. use the SDK’s hosted WebSearchTool
6. BPOP is correct. Current price only. Please use whichever free endpoint is available and doesn't require credentialling.
7. No tests for now. No github actions
8. the first basic files example. From there we will integrate them into the main.py
9. It's to teach internals and fundamentals

Assistant:
Confirmed locked decisions based on your answers and produced a tightened Codex prompt:
- Python 3.12 + Poetry
- single main.py + CLI subcommands
- .env with OPENAI_API_KEY and default model gpt-5-mini
- attachments demo: text file only (structured input items)
- hosted WebSearchTool
- custom tool: BPOP current price from free endpoint (Stooq CSV)
- no tests, no CI
- examples first, then integrated into main.py
- README teaches internals (Runner loop, tools, structured inputs, hosted vs local tools)