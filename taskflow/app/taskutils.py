"""TaskFlow task utilities for Module 02.

This module normalizes raw task records, validates them, computes a priority
score, and exposes a small Task class with behavior.
"""

from __future__ import annotations


ALLOWED_PRIORITIES = {"low", "medium", "high"}
MAX_TITLE_LENGTH = 200


class InvalidTaskError(ValueError):
    """Raised when a task record is missing or has an invalid field."""


def parse_task(record: dict) -> dict:
    """Normalize a raw task record; raise InvalidTaskError on bad input."""
    title = record.get("title", "").strip()
    if not title:
        raise InvalidTaskError("Task 'title' is required")
    if len(title) > MAX_TITLE_LENGTH:
        raise InvalidTaskError(
            f"Task 'title' too long ({len(title)} > {MAX_TITLE_LENGTH})"
        )

    priority = record.get("priority", "medium").strip().lower()
    if priority not in ALLOWED_PRIORITIES:
        priority = "medium"

    return {"title": title, "priority": priority, "done": False}


def priority_score(priority: str) -> int:
    """Return a numeric weight for sorting tasks by priority."""
    weights = {"low": 1, "medium": 2, "high": 3}
    return weights.get(priority, 0)


def sort_tasks(tasks: list[dict]) -> list[dict]:
    """Return tasks ordered by priority, highest first."""
    return sorted(
        tasks,
        key=lambda task: priority_score(task["priority"]),
        reverse=True,
    )


def high_priority_titles(tasks: list[dict]) -> list[str]:
    """Return titles of high-priority tasks, in original order."""
    return [task["title"] for task in tasks if task["priority"] == "high"]


def add_tag(tag: str, tags: list[str] | None = None) -> list[str]:
    """Append a tag to a list, creating a fresh list when none is given."""
    if tags is None:
        tags = []
    tags.append(tag)
    return tags


class Task:
    """A TaskFlow task with data and simple behavior."""

    def __init__(self, title: str, priority: str = "medium"):
        self.title = title
        self.priority = priority
        self.done = False

    def complete(self) -> None:
        """Mark the task as done."""
        self.done = True

    def __repr__(self) -> str:
        return (
            f"Task(title={self.title!r}, priority={self.priority!r}, "
            f"done={self.done})"
        )

    @classmethod
    def from_dict(cls, record: dict) -> "Task":
        """Build a Task from a raw record, validated through parse_task."""
        data = parse_task(record)
        return cls(title=data["title"], priority=data["priority"])
