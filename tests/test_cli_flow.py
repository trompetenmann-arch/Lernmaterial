from pathlib import Path

from worksheet_tool.cli import cmd_add_task, cmd_new, cmd_render


class Args:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def test_cli_flow(tmp_path: Path) -> None:
    data_file = tmp_path / "blatt01.json"
    out_file = tmp_path / "blatt01.md"

    cmd_new(
        Args(
            file=data_file,
            course="Lineare Algebra 1",
            semester="WS 2026/27",
            sheet=1,
            due="2026-11-10",
            lecturer="Prof. Muster",
        )
    )

    cmd_add_task(
        Args(
            file=data_file,
            title="Vektorräume",
            text="beweise fuer alle v in R^n",
            points=5,
            topic="Lineare Algebra",
            difficulty="mittel",
        )
    )

    cmd_render(Args(file=data_file, out=out_file))

    content = out_file.read_text(encoding="utf-8")
    assert "Universität Bielefeld" in content
    assert "Aufgabe 1: Vektorräume" in content
