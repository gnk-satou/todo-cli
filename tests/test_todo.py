import pytest

from todo_cli import cli, storage


@pytest.fixture(autouse=True)
def tmp_store(tmp_path, monkeypatch):
    monkeypatch.setenv("TODO_CLI_FILE", str(tmp_path / "tasks.json"))


def test_add_and_list(capsys):
    assert cli.main(["add", "buy milk"]) == 0
    assert cli.main(["list"]) == 0
    out = capsys.readouterr().out
    assert "buy milk" in out
    assert "[ ] #1" in out


def test_done(capsys):
    cli.main(["add", "task"])
    assert cli.main(["done", "1"]) == 0
    cli.main(["list"])
    assert "[x] #1" in capsys.readouterr().out


def test_done_not_found():
    assert cli.main(["done", "99"]) == 1


def test_remove(capsys):
    cli.main(["add", "task"])
    assert cli.main(["remove", "1"]) == 0
    cli.main(["list"])
    assert "No tasks." in capsys.readouterr().out


def test_remove_not_found():
    assert cli.main(["remove", "99"]) == 1


def test_next_id_empty():
    assert storage.next_id([]) == 1
