# Github Copilot CLI

```shell
unset GITHUB_TOKEN
gh auth login

gh copilot suggest "grep for # in md files"
gh copilot suggest "remove all files with pyc and pyo extension"
gh copilot suggest "list free memory in GiB"
gh copilot suggest "list file system utilization"
gh copilot suggest "list mounts"
gh copilot suggest "make POST request with json body"
gh copilot suggest "delete all python __pycache__ dir"
gh copilot suggest "GET weather in CPH now"

gh copilot explain "docker build -t flask-mini --build-arg FLASK_DEBUG=True ."
gh copilot explain "docker run -d --name flask-app -p 80:8080 --rm flask-mini"
gh copilot explain "find . -name "__pycache__" -type d -exec rm -rf {} +"
gh copilot explain "kubectl autoscale deployment api-backend --cpu-percent 80 --min 3 --max 6"
gh copilot explain "tmux new-session \; split-window -v -p 55 \; split-window -v -p 55 \; select-pane -U\; split-window -h \; select-pane -U \;"
```

# Questions

```
How to grep markdown code block in terminal?
```
