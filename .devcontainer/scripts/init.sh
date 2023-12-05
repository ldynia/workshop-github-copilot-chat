#!/usr/bin/env bash

set -Eeuo pipefail

# install packages
sudo apt-get update && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y \
  bash-completion \
  git \
  tmux

# autocomplete
source /usr/share/bash-completion/completions/git
