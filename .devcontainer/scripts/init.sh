#!/usr/bin/env bash

set -Eeuo pipefail

# Add the GitHub CLI package repository to the system's list of APT sources.
type -p curl >/dev/null || (sudo apt update && sudo apt install curl -y)
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
  && sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
  && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null

# Install packages
sudo apt-get update && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y \
  bash-completion \
  gh \
  git \
  tig \
  pcregrep \
  tmux

# This will work in gh's codespeces, not in local!
if [[ -v GITHUB_TOKEN ]]; then
  # Install gh extention Copilot CLI
  gh extension install github/gh-copilot
  gh extension upgrade gh-copilot
fi
