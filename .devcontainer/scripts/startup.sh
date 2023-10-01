#!/usr/bin/env bash

set -Eeuo pipefail

function autocomplete() {
  source /usr/share/bash-completion/completions/git
  source /usr/share/bash-completion/completions/docker
}

function configure_tmux() {
  touch ~/.tmux.conf
  echo "set -g mode-mouse on" >> ~/.tmux.conf
  tmux source-file ~/.tmux.conf
}

autocomplete
configure_tmux
