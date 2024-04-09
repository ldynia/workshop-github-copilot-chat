# Copilot Chat

Remember to **DISCONNECT VPN**.

[GitHub Copilot Pricing](https://github.com/features/copilot/plans)

## Agents and Commands

**Objectives:** Explain core concepts of GitHub Copilot.

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

# Sherlock

## How To Run The Project

**Objectives:** How to start working with unknown project.

Go to `cd chat/sherlock` directory and run the application.

```
@workspace What is sherlock?
@workspace How to run sherlock locally?
@workspace How to run sherlock with docker?
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

**Objectives:** Write unit tests for the application.

```
# Select index, live and recommended functions
@workspace /tests Generate unit tests for selected code. Use pytest module.
```

**Notes:** Create following files and run `pytest app/tests` command.
- `app/tests/__init__.py` file
- `app/tests/test_app.py` file
- `app/tests` directory

## Refactor `rengine.py`

**Objectives:** refactor application.

```
# Select all
Propose better variable names

# Select all
Refactor this code to a more generic implementation

# Select code in recommend method
Comment every line in selected code with time complexity. Estimate the total time complexity of the recommended method.

# Select all
Add pep8 docs string

# Select all
Use Python annotations to document methods in selected code.
```

## Refactor `run.py`

**Objectives:** Refactor application.

```
# Select the whole file
Does this code violate SOLID principles?

# Select recommended and alive functions
Refactor
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
```

## Links

- [Time Complexity](https://www.desmos.com/calculator/xpfyjl1lbn)
- [Intro Time Complexity](https://victoria.dev/blog/a-coffee-break-introduction-to-time-complexity-of-algorithms/)
- [GitHub Copilot](https://docs.github.com/en/copilot/configuring-github-copilot/configuring-github-copilot-in-your-environment?tool=vscode)
- [GitHub Copilot Chat](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-chat?view=vs-2022)
