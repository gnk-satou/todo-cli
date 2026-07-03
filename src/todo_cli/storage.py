"""JSON-backed task storage."""

from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class Task:
    id: int
    title: str
    done: bool = False


def default_path() -> Path:
    env = os.environ.get("TODO_CLI_FILE")
    if env:
        return Path(env)
    return Path.home() / ".todo-cli.json"


def load_tasks(path: Path | None = None) -> list[Task]:
    path = path or default_path()
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    return [Task(**item) for item in data]


def save_tasks(tasks: list[Task], path: Path | None = None) -> None:
    path = path or default_path()
    path.write_text(
        json.dumps([asdict(t) for t in tasks], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def next_id(tasks: list[Task]) -> int:
    return max((t.id for t in tasks), default=0) + 1
