#!/usr/bin/env bash

set -Eeuo pipefail

type -p curl >/dev/null || (sudo apt update && sudo apt install curl -y)
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
  && sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
  && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \


# install packages
sudo apt-get update && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y \
  bash-completion \
  gh \
  git \
  tig \
  pcregrep \
  tmux

# install gh extention Copilot CLI
gh extension install github/gh-copilot
gh extension upgrade gh-copilot

# autocomplete
source /usr/share/bash-completion/completions/git
