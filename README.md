# py-basic-scaffold

The objective of this project is to provide a quick basic setup for a python project. `git clone` and make it yours!


# Table of Contents
- [Prerequisites](#prerequisites)
  - [Install software](#install-software)
- [Get up and running](#get-up-and-running)
- [Configure VS Code](#configure-vs-code)


## Prerequisites

### Install software
- [git](https://git-scm.com/downloads)
- [pyenv - _optional_](https://github.com/pyenv/pyenv)
- [VS Code - _optional_](https://code.visualstudio.com/download)


## Get up and running

Run the below command to create a project based on this basic scaffold. **NOTE**: It assumes that you have installed Python and configured git. If you are using pyenv, `.python-version` file will be used.

**Option 1**: Create new project from Linux or macOS command shell and stay in the shell:
```sh
# Replace "my_project" with your own project name.
curl -sSL https://raw.githubusercontent.com/zen-code-symphony/py-basic-scaffold/main/create-project.sh | bash -s my_project && cd my_project && source venv/bin/activate
```

**Option 2**: Create new project from Linux or macOS shell and open VS Code editor:
```sh
# Replace "my_project" with your own project name.
curl -sSL https://raw.githubusercontent.com/zen-code-symphony/py-basic-scaffold/main/create-project.sh | bash -s my_project && cd my_project && code .
```

## Configure VS Code
  - As part of VS Code workspace extensions recommendations, the extensions mentioned in [.vscode/extensions.json](./.vscode/extensions.json), should be installed. This includes extensions for flake8, black, isort etc.
  - Make sure that you are using the workspace settings mentioned in repository file [.vscode/settings.json](./.vscode/settings.json). `CTRL+,` and open `Workspace` settings tab to check.
