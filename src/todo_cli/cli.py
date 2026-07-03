"""Command-line interface for todo-cli."""

from __future__ import annotations

import argparse
import sys

from .storage import Task, load_tasks, next_id, save_tasks


def cmd_add(title: str) -> int:
    tasks = load_tasks()
    task = Task(id=next_id(tasks), title=title)
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added #{task.id}: {task.title}")
    return 0


def cmd_list() -> int:
    tasks = load_tasks()
    if not tasks:
        print("No tasks.")
        return 0
    for t in tasks:
        mark = "x" if t.done else " "
        print(f"[{mark}] #{t.id} {t.title}")
    return 0


def cmd_done(task_id: int) -> int:
    tasks = load_tasks()
    for t in tasks:
        if t.id == task_id:
            t.done = True
            save_tasks(tasks)
            print(f"Done #{t.id}: {t.title}")
            return 0
    print(f"Task #{task_id} not found.", file=sys.stderr)
    return 1


def cmd_remove(task_id: int) -> int:
    tasks = load_tasks()
    remaining = [t for t in tasks if t.id != task_id]
    if len(remaining) == len(tasks):
        print(f"Task #{task_id} not found.", file=sys.stderr)
        return 1
    save_tasks(remaining)
    print(f"Removed #{task_id}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="todo", description="Minimal TODO manager")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Add a task")
    p_add.add_argument("title", help="Task title")

    sub.add_parser("list", help="List tasks")

    p_done = sub.add_parser("done", help="Mark a task as done")
    p_done.add_argument("id", type=int)

    p_rm = sub.add_parser("remove", help="Remove a task")
    p_rm.add_argument("id", type=int)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "add":
        return cmd_add(args.title)
    if args.command == "list":
        return cmd_list()
    if args.command == "done":
        return cmd_done(args.id)
    if args.command == "remove":
        return cmd_remove(args.id)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
