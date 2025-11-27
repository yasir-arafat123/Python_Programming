from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Exercise:
    title: str
    summary: str
    checklist: tuple[str, ...]


EXERCISES: tuple[Exercise, ...] = (
    Exercise(
        title="Upgrade pip and confirm version",
        summary="Upgrade pip in the active interpreter and verify the reported version aligns with expectations.",
        checklist=(
            "Run python -m pip install --upgrade pip",
            "Capture the output from python -m pip --version",
            "Record the pip location to ensure you updated the intended interpreter",
        ),
    ),
    Exercise(
        title="Install a user-scoped package",
        summary="Install a lightweight dependency using --user and ensure it imports from a fresh Python session.",
        checklist=(
            "Select a package and install with python -m pip install --user <name>",
            "Launch a new shell or use subprocess to query python -m site --user-site",
            "Verify the package imports successfully",
        ),
    ),
    Exercise(
        title="Compare OS pip vs python -m pip",
        summary="Demonstrate why invoking pip through the python module ensures alignment with the desired interpreter.",
        checklist=(
            "Record the path reported by pip --version",
            "Record the path reported by python -m pip --version",
            "Summarize when paths diverge (e.g., multiple Python installations)",
        ),
    ),
)


def iter_exercises() -> Iterable[Exercise]:
    return EXERCISES


def as_markdown() -> str:
    lines: list[str] = ["# Exercises", ""]
    for index, exercise in enumerate(EXERCISES, start=1):
        lines.append(f"{index}. {exercise.title}")
        lines.append(f"   - {exercise.summary}")
        for task in exercise.checklist:
            lines.append(f"     * {task}")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    print(as_markdown())
