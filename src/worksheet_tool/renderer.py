from __future__ import annotations

from pathlib import Path

from worksheet_tool.models import Worksheet


def render_markdown(worksheet: Worksheet) -> str:
    header = [
        f"# {worksheet.university}",
        f"## {worksheet.course}",
        "",
        f"**Semester:** {worksheet.semester}  ",
        f"**Übungsblatt:** {worksheet.sheet_number}  ",
        f"**Abgabe:** {worksheet.due_date}  ",
        f"**Dozent*in:** {worksheet.lecturer}",
        "",
        "---",
        "",
    ]

    sections: list[str] = []
    for task in worksheet.tasks:
        section = [
            f"### Aufgabe {task.number}: {task.title}",
            f"**Thema:** {task.topic or 'Allgemein'}  ",
            f"**Schwierigkeit:** {task.difficulty}  ",
            f"**Punkte:** {task.points}",
            "",
            task.edited_text,
            "",
        ]
        sections.extend(section)

    return "\n".join(header + sections).strip() + "\n"


def render_to_file(worksheet: Worksheet, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_markdown(worksheet), encoding="utf-8")
