from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import date
import json
from pathlib import Path
from typing import Any


@dataclass
class Task:
    number: int
    title: str
    raw_text: str
    edited_text: str
    points: int = 0
    topic: str = ""
    difficulty: str = "mittel"


@dataclass
class Worksheet:
    university: str
    course: str
    semester: str
    sheet_number: int
    due_date: str
    lecturer: str
    tasks: list[Task] = field(default_factory=list)

    @staticmethod
    def create_default(course: str, semester: str, sheet_number: int, due_date: str, lecturer: str) -> "Worksheet":
        return Worksheet(
            university="Universität Bielefeld",
            course=course,
            semester=semester,
            sheet_number=sheet_number,
            due_date=due_date,
            lecturer=lecturer,
        )

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "Worksheet":
        tasks = [Task(**task_data) for task_data in data.get("tasks", [])]
        data = {**data, "tasks": tasks}
        return Worksheet(**data)

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")

    @staticmethod
    def load(path: Path) -> "Worksheet":
        data = json.loads(path.read_text(encoding="utf-8"))
        return Worksheet.from_dict(data)


def default_due_date() -> str:
    return str(date.today())
