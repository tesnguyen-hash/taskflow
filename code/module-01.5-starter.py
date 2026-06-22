"""TaskFlow triage engine — STARTER (Module 1.5).

Print the startup banner, then complete the TODOs to clean a messy title
and build a slug. A reference implementation lives in
code/module-01.5-example.py.

Run:
    python code/module-01.5-starter.py
"""

from __future__ import annotations


def clean_title(title: str) -> str:
    """Return a display-ready title: trimmed and Title-Cased.

    ".strip()" removes the stray spaces from both ends; ".title()" gives
    each word a capital letter so the report looks tidy for humans.
    """
    return title.strip().title()


def slugify(title: str) -> str:
    """Return a URL-friendly slug like "fix-login-bug".

    Clean the title first, lowercase it, then swap spaces for dashes.
    """
    cleaned = clean_title(title)
    return cleaned.lower().replace(" ", "-")


if __name__ == "__main__":
    app_name = "TaskFlow"

    # 🧩 Debug/Fix: the line below had a stray indent which caused an
    # IndentationError. The extra spaces were removed so the banner prints.
    print(f"Starting {app_name} Task Triage Engine...")
    print("Loaded 3 sample tasks.")
    print("Ready to analyze.")
