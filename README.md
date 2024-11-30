# Advent of Code (AoC) 2024!

This will be my attempt at the AoC challenge of this year (2024).


## Table of Contents

- [Advent of Code (AoC) 2024!](#advent-of-code-aoc-2024)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
    - [uv: Python package and project manager](#uv-python-package-and-project-manager)
  - [Tooling](#tooling)
    - [Poe the Poet](#poe-the-poet)
      - [Tasks](#tasks)
        - [Check all code](#check-all-code)
        - [Lint code](#lint-code)
        - [Format code](#format-code)
        - [Run unit tests](#run-unit-tests)

## Prerequisites

### uv: Python package and project manager

>uv manages project dependencies and environments, with support for lockfiles, workspaces, and more, similar to rye or poetry

Install uv using the official documentation [docs.astral.sh](https://docs.astral.sh/uv/#getting-started).

After installing uv you are able to install the projects dependencies within a separate virtual environment. Use the following command.

```shell
uv venv
uv sync --all-extras
```

## Tooling

### Poe the Poet

Within this project a tool called poe the poet, in short poe, is used to define simple tasks to run.

After installing the project with uv you are able to get a overview of the defined tasks within this project as followed:

```shell
poe
```

#### Tasks

These are a few of the tasks that have been defined

##### Check all code

Checks all code for any problems by running multiple tooling after each other (linting, testing, style, etc.)

```shell
poe check
```

##### Lint code

Run the linters defined for this project

```shell
poe lint
```

##### Format code

Run the formatters defined for this project

```shell
poe format
```

##### Run unit tests

Run the tests suite of this project.

```shell
poe test
```
