# Copilot Chat

Remember to **DISCONNECT VPN**.

## Agents and Commands

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

## flask-init

Write unit test for flask app test `run.py`.

```
@workspace /tests only with pytest module.
```

Make `Dockerfile` secure. **Select all**.

```shell
Expose port.
Expose port but use variable syntax.
Secure this.
Make Dockerfile rootless.
Secure Dockerfile with nobody and nogroup user.
Explaing user and group id ranges in Linux. Show it as a table.
Implement Dockerfile application HEALTHCHECK with default intervals.
Remove cache after add.
```

## sherlock
Run prompts against `run.py` file.

```
# Select recommend and alive functions
@workspace /tests this

# Select whole file
Does this code violates SOLID principles?

# Select recommend and alive functions
Refactor this code

# Select recommend functions
Implement a decorator to handle errors
```

Run prompts against `rengine.py` file

```
Propose a better variables name
Refactor
Add pep8 docs string
Use Python annotations to document methods
Comment every line in the recommend method with time complexity. Estimate the total time complexity of the recommend method.
```

## Links

- https://docs.github.com/en/copilot/configuring-github-copilot/configuring-github-copilot-in-your-environment?tool=vscode
- https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-chat?view=vs-2022
