# todo-cli

![CI](https://github.com/gnk-satou/todo-cli/actions/workflows/ci.yml/badge.svg)

Minimal command-line TODO manager written in Python. Tasks are stored locally as JSON — no external services, no dependencies beyond the standard library.

## Features

- Add, list, complete, and remove tasks
- Local JSON storage
- Zero runtime dependencies
- Tested with pytest, CI on Python 3.10 / 3.12 via GitHub Actions

## Installation

```bash
git clone https://github.com/gnk-satou/todo-cli.git
cd todo-cli
pip install -e .
```

## Usage

```bash
# Add a task
$ todo add "Write README"
Added #1: Write README

# List tasks
$ todo list
[ ] #1 Write README

# Mark a task as done
$ todo done 1
Done #1: Write README

$ todo list
[x] #1 Write README

# Remove a task
$ todo remove 1
Removed #1
```

## Development

```bash
pip install -e . pytest
pytest
```

## Project Structure

```
src/todo_cli/   # Application code
tests/          # pytest test suite
.github/workflows/ci.yml  # CI (Python 3.10 / 3.12)
```

## License

MIT
