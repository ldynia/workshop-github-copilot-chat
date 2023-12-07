# Copilot CLI

Remember to **DISCONNECT VPN**.

## Setup

```shell
unset GITHUB_TOKEN
gh auth login

bash .devcontainer/scripts/init.sh

gh copilot
```

## Suggest comands

```shell
gh copilot suggest "grep for # in md files"
gh copilot suggest "remove all files with pyc and pyo extension"
gh copilot suggest "delete all python __pycache__ dir"
gh copilot suggest "list free memory in GiB"
gh copilot suggest "list file system utilization"
gh copilot suggest "make POST request with json body"
gh copilot suggest "Rename all folders in current directory to lower case"
gh copilot suggest "Install rename in ubuntu"
gh copilot suggest "GET weather in CPH now"
```

## Explain commands

``` shell
gh copilot explain 'find . -name "__pycache__" -type d -exec rm -rf {} +'
gh copilot explain "docker build -t flask-mini --build-arg FLASK_DEBUG=True ."
gh copilot explain "docker run -d --name flask-app -p 80:8080 --rm flask-mini"
gh copilot explain "kubectl autoscale deployment api-backend --cpu-percent 80 --min 3 --max 6"
gh copilot explain "tmux new-session \; split-window -v -p 55 \; split-window -v -p 55 \; select-pane -U\; split-window -h \; select-pane -U \;"
```

## Questions

```shell
@terminal How to grep markdown code block in terminal?
@terminal How to grep markdown code block in terminal using pcregrep?
```
