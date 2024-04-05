# Workshop Github Copilot Chat

![github](/docs/assets/github.jpg)

## Installation Local

1. GitHub Copilot is not free. It costs [$10](https://github.com/features/copilot/plans#pricing) per month for individuals.
1. DISCONNECT VPN - GitHub Copilot doesn't work with VPN.

```shell
git clone https://github.com/ldynia/workshop-github-copilot-chat.git
code workshop-github-copilot-chat/

# Rebuild Container
Ctrl + K Ctrl + O
```

## Github Copilot X

1. [Copilot](./copilot/WORKSHOP.md)
1. [Copilot Chat](./chat/WORKSHOP.md)
1. [Copilot CLI](./cli/WORKSHOP.md)
1. [~~Copilot Labs~~](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-labs)

## Copilot Shortcuts Linux

| Shortcut | Description |
| -------- | ----------- |
| `tab` | Accept suggestion |
| `alt+enter` | Show 10 suggestions |
| `alt+/` | Show suggestions |
| `alt+[` | Show previous suggestions |
| `alt+]` | Show next suggestions |
| `ctrl+alt+i`, `ctrl+shift+c` | Chat |
| `ctrl+i` | Chat inline |
| `ctrl+l` | Clear the session |
| `ctrl+enter` | Insert into code |
| `ctrl+alt+enter` | Insert into terminal |

## Links

- https://code.visualstudio.com/docs/editor/github-copilot#_chat-view
- https://docs.github.com/en/copilot/configuring-github-copilot/configuring-github-copilot-in-your-environment?tool=vscode
- https://docs.github.com/en/copilot/using-github-copilot/getting-started-with-github-copilot?tool=vscode
- https://www.youtube.com/watch?v=SZVCJRUADc4


## Workshop Setup

```shell
{
  mkdir -p ~/workshop/chat/solution/copilot ~/workshop/chat/solution/sherlock ~/workshop/chat/solution/cli;
  cd ~/workshop/chat/;
  git clone https://github.com/ldynia/workshop-github-copilot-chat.git;
  tar -vxf workshop-github-copilot-chat/chat/solution-sherlock.tar.xz --directory solution/sherlock;
  tar -vxf workshop-github-copilot-chat/copilot/solution-copilot.tar.xz --directory solution/copilot;
  find ~/workshop/chat/workshop-github-copilot-chat/ -type f -name "*.tar.xz" -exec rm -f {} \;
  cp ~/workshop/chat/workshop-github-copilot-chat/chat/WORKSHOP.md ~/workshop/chat/solution/sherlock;
  cp ~/workshop/chat/workshop-github-copilot-chat/cli/WORKSHOP.md ~/workshop/chat/solution/cli;
  cp ~/workshop/chat/workshop-github-copilot-chat/copilot/WORKSHOP.md ~/workshop/chat/solution/copilot;
  code ~/workshop/chat/solution/;
  code ~/workshop/chat/workshop-github-copilot-chat/;
}
```
