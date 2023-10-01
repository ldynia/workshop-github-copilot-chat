#!/usr/bin/env bash

set -Eeuo pipefail

function install() {
  sudo apt-get update && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y \
    bash-completion \
    git-core \
    tmux
}

function autocomplete() {
  source /usr/share/bash-completion/completions/git
  source /usr/share/bash-completion/completions/docker
}

function configure_tmux() {
  touch ~/.tmux.conf
  echo "set -g mode-mouse on" >> ~/.tmux.conf
  tmux source-file ~/.tmux.conf
}

# Execut function(s)
install
autocomplete
configure_tmux