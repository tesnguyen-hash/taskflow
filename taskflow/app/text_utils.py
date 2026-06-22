def slugify_title(title: str) -> str:
    """Convert a task title into a URL-safe slug."""
    return "-".join(title.strip().lower().split())


def normalize_priority(priority: str) -> str:
    """Map free-text priority to a known value, defaulting to 'medium'."""
    allowed = {"low", "medium", "high"}
    value = priority.strip().lower()
    return value if value in allowed else "medium"


def clean_title(title: str) -> str:
    """Strip surrounding whitespace and validate the title.

    Raises:
        ValueError: If the title is empty or only whitespace after stripping.
    """
    cleaned = title.strip()
    if not cleaned:
        raise ValueError("title must not be empty")
    return cleaned


if __name__ == "__main__":
    print(slugify_title("  Ship the Release  "))
    print(normalize_priority("URGENT"))
    print(clean_title("  Deploy  "))
