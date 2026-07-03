# todo-cli

A minimal command-line TODO manager written in Python. Tasks are stored in a local JSON file.

## Features

- Add, list, complete, and remove tasks
- Zero runtime dependencies (standard library only)
- Tested with pytest, CI via GitHub Actions

## Install

```bash
pip install -e .
```

## Usage

```bash
todo add "buy milk"
todo list
todo done 1
todo remove 1
```

Example output:

```
$ todo list
[ ] #1 buy milk
[x] #2 write README
```

## Storage

Tasks are saved to `~/.todo-cli.json`. Override the location with the `TODO_CLI_FILE` environment variable.

## Development

```bash
pip install -e . pytest
pytest
```

## License

MIT
