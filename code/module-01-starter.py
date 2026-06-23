"""TaskFlow starter script (Module 01) — intentionally messy.

This is a single top-to-bottom blob with an inline secret and copy-pasted
logic. Your job in the lab is to refactor it into clean, single-responsibility
functions (see code/module-01-example.py for the target style) and to read the
database URL from the environment instead of hardcoding it.

Run:
    python code/module-01-starter.py
"""
# NOTE: The following three lines in the original exercise were plain-text
# questions inserted into the file; they caused a syntax error when running
# the script. They are intentionally left here as comments for students to
# answer during the lab.
# - What distinct *jobs* is this one script doing?
# - Which line is a security problem?
# - If a teammate had to reuse just the "make a slug"

import os

# BAD: a secret pasted straight into the source (never do this!).
# Read the database URL from the environment instead of hardcoding it.
DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://USER:PASSWORD@localhost:5432/taskflow",
)

# Everything happens in one blob with duplicated, hard-to-reuse logic.
t1 = "  Ship the Release  "
slug1 = t1.strip().lower().replace("   ", " ").replace("  ", " ").replace(" ", "-")
print("slug:", slug1)

p1 = "URGENT"
if p1.strip().lower() == "low":
    pr1 = "low"
elif p1.strip().lower() == "medium":
    pr1 = "medium"
elif p1.strip().lower() == "high":
    pr1 = "high"
else:
    pr1 = "medium"
print("priority:", pr1)

# ... and again for another task, copy-pasted instead of reused ...
t2 = "Write   the   Docs"
slug2 = t2.strip().lower().replace("   ", " ").replace("  ", " ").replace(" ", "-")
print("slug:", slug2)

# Avoid printing secrets to stdout; show a redacted placeholder instead.
print("connecting with: <REDACTED>")
