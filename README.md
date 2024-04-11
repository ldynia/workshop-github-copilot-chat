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
- https://resources.github.com/learn/pathways/?utm_source=learning-pathways&utm_medium=Resources&utm_campaign=copilot-banner
- https://resources.github.com/learn/pathways/copilot/essentials/essentials-of-github-copilot/?utm_campaign=copilot-banner&utm_medium=Resources&utm_source=learning-pathways
- https://learn.microsoft.com/en-us/legal/cognitive-services/openai/customer-copyright-commitment

## Workshop Setup

```shell
{
  rm -rf ~/copilot_chat;
  mkdir -p ~/copilot_chat/solution/copilot ~/copilot_chat/solution/sherlock ~/copilot_chat/solution/cli;
  cd ~/copilot_chat/;
  git clone https://github.com/ldynia/workshop-github-copilot-chat.git;
  tar -vxf workshop-github-copilot-chat/chat/solution-sherlock.tar.xz --directory solution/sherlock;
  tar -vxf workshop-github-copilot-chat/copilot/solution-copilot.tar.xz --directory solution/copilot;
  find ~/copilot_chat/workshop-github-copilot-chat/ -type f -name "*.tar.xz" -exec rm -f {} \;
  mv ~/copilot_chat/workshop-github-copilot-chat/chat/WORKSHOP.md ~/copilot_chat/solution/sherlock;
  mv workshop-github-copilot-chat/cli/ ~/copilot_chat/solution/;
  mv ~/copilot_chat/workshop-github-copilot-chat/copilot/WORKSHOP.md ~/copilot_chat/solution/copilot;
  rm -rf ~/copilot_chat/workshop-github-copilot-chat/README.md;
  rm -rf ~/copilot_chat/workshop-github-copilot-chat/docs;
  touch workshop-github-copilot-chat/copilot/app.js;
  touch workshop-github-copilot-chat/copilot/bitcoin.py;
  touch workshop-github-copilot-chat/copilot/fibonacci-v1.py;
  touch workshop-github-copilot-chat/copilot/regex.py;
  touch workshop-github-copilot-chat/copilot/questions.py;
  code ~/copilot_chat/solution/;
  code ~/copilot_chat/workshop-github-copilot-chat/;
}
```
