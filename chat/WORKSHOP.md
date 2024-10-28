# Copilot Chat

Remember to **DISCONNECT VPN**.

* [GitHub Copilot Pricing](https://github.com/features/copilot/plans)
* [GitHub Copilot Docs](https://docs.github.com/en/copilot/using-github-copilot)

## Agents and Commands

**Objectives:** Explain the core concepts of GitHub Copilot.

An agent is a specialized chat participant that can assist in specific areas.

* `@workspace` - Ask about your workspace
  * `/explain` - Explain how the selected code works
  * `/tests`- Generate unit tests for the selected code
  * `/fix`- Propose a fix for the problems in the selected code
  * `/new`- Scaffold code for a new workspace
  * `/newNotebook` - Create a new Jupyter Notebook
* `@vscode` - Ask about VS Code
  * `/search` - Generate query parameters for workspace search
  * `/api` - Ask about VS Code extension development
* `@terminal` - Ask how to do something in the terminal
  * `/help` - General help about GitHub Copilot.
  * `/clear` - Clear the session.

Chat variables include specific context in your prompt.

* `#file` - Include specific file.
* `#editor` - Include visible source code.
* `#selection` - The current selection in the active editor.
* `#terminalLastCommand` - The active terminal's last run command
* `#terminalSelection` - The current selection in the terminal.
* `#codebase` - Searches through the codebase and pulls out relevant information for the query.

# Sherlock

## How To Run The Project

**Objectives:** How to start working with an unknown project

Go to `cd chat/sherlock` directory and run the application.

```
@workspace What is Sherlock?
@workspace How to run Sherlock locally?
@workspace How to run this project with docker?
```

Visit the following URLs: Run locally

- http://localhost:8080/

## Fix Project

**Objectives:** Compare GitHub Copilot and GitHub Copilot Chat.

In Vs Code Open `OUTPUT` tab and select `GitHub Copilot Chat` log.

```
Ctrl + I
# Add current directory to PYTHONPATH

Ctrl + Shift + C
# Add current directory to PYTHONPATH
```

## How To Write Unit Tests

**Objectives:** Write unit tests with `/tests` command.

```
# Select index, live, and recommended functions
@workspace /tests Generate unit tests for selected code. Use pytest module.
```

**Notes:** Create the following files and run `pytest -vs app/tests` command.
- `app/tests/__init__.py` file
- `app/tests/conftest.py` file
- `app/tests/test_run.py` file

## Refactor `run.py`

**Objectives:** Refactor application.

```
# Select the whole file. Send two prompts.
Does this code violate SOLID principles?
What to refactor?

# Select the whole file. Send one prompt.
Does this code violate SOLID principles? What to refactor?

Analyze selected code for SRP violation?

# Select recommended functions
Refactor
```

## Refactor `rengine.py` And Document

**Objectives:** Refactor application and document methods with `/doc` command.

```
# Select all
Propose better variables name and class name

# Select all
Refactor selected code to a more generic implementation

# Select the code in the recommend method.
Comment every line in recommend method with time complexity. Estimate the total time complexity of the recommended method.

# Select the method and use /doc command
Add pep8 docs string

# Select all
Use Python annotations to document methods in selected code.
```

## Refactor `Dockerfile`

**Objectives:** Apply best practices to Dockerfile. Find the difference between GPT gpt-3.5-turbo vs gpt-4

```
# Select FROM instruction `Ctrl + I`
What is the latest Python image that I can use?

# Ports
Expose port
Expose port but use variable syntax

# Rootless
Make Dockerfile rootless
Secure Dockerfile with nobody and nogroup user
Explain user and group ID ranges in Linux. Show results as a table.

# Select RUN apk add curl
Remove application cache and cache dir

# HEALTHCHECK
Implement application HEALTHCHECK with default intervals

# Add comments
```

## Links

- [Time Complexity](https://www.desmos.com/calculator/xpfyjl1lbn)
- [Intro Time Complexity](https://victoria.dev/blog/a-coffee-break-introduction-to-time-complexity-of-algorithms/)
- [GitHub Copilot](https://docs.github.com/en/copilot/configuring-github-copilot/configuring-github-copilot-in-your-environment?tool=vscode)
- [GitHub Copilot Chat](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-chat?view=vs-2022)
