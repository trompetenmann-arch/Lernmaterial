from __future__ import annotations

import argparse
from pathlib import Path

from worksheet_tool.editing import lint_task_text, rewrite_task_text
from worksheet_tool.models import Task, Worksheet, default_due_date
from worksheet_tool.renderer import render_to_file


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Arbeitsblatt-Tool für Mathematik")
    subparsers = parser.add_subparsers(dest="command", required=True)

    new_parser = subparsers.add_parser("new", help="Neues Arbeitsblatt anlegen")
    new_parser.add_argument("--file", required=True, type=Path)
    new_parser.add_argument("--course", required=True)
    new_parser.add_argument("--semester", required=True)
    new_parser.add_argument("--sheet", required=True, type=int)
    new_parser.add_argument("--due", default=default_due_date())
    new_parser.add_argument("--lecturer", required=True)

    add_task_parser = subparsers.add_parser("add-task", help="Aufgabe hinzufügen und redigieren")
    add_task_parser.add_argument("--file", required=True, type=Path)
    add_task_parser.add_argument("--title", required=True)
    add_task_parser.add_argument("--text", required=True, help="Rohtext der Aufgabe")
    add_task_parser.add_argument("--points", type=int, default=0)
    add_task_parser.add_argument("--topic", default="")
    add_task_parser.add_argument("--difficulty", default="mittel")

    render_parser = subparsers.add_parser("render", help="Arbeitsblatt als Markdown rendern")
    render_parser.add_argument("--file", required=True, type=Path)
    render_parser.add_argument("--out", required=True, type=Path)

    return parser


def cmd_new(args: argparse.Namespace) -> None:
    worksheet = Worksheet.create_default(
        course=args.course,
        semester=args.semester,
        sheet_number=args.sheet,
        due_date=args.due,
        lecturer=args.lecturer,
    )
    worksheet.save(args.file)
    print(f"Arbeitsblatt erstellt: {args.file}")


def cmd_add_task(args: argparse.Namespace) -> None:
    worksheet = Worksheet.load(args.file)
    edited = rewrite_task_text(args.text)
    hints = lint_task_text(edited)

    task = Task(
        number=len(worksheet.tasks) + 1,
        title=args.title,
        raw_text=args.text,
        edited_text=edited,
        points=args.points,
        topic=args.topic,
        difficulty=args.difficulty,
    )
    worksheet.add_task(task)
    worksheet.save(args.file)

    print(f"Aufgabe hinzugefügt: {task.number} - {task.title}")
    if hints:
        print("Hinweise zur Formulierung:")
        for hint in hints:
            print(f"- {hint}")


def cmd_render(args: argparse.Namespace) -> None:
    worksheet = Worksheet.load(args.file)
    render_to_file(worksheet, args.out)
    print(f"Markdown exportiert: {args.out}")


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "new":
        cmd_new(args)
    elif args.command == "add-task":
        cmd_add_task(args)
    elif args.command == "render":
        cmd_render(args)


if __name__ == "__main__":
    main()
