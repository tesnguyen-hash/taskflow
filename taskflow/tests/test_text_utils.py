import pytest

from app.text_utils import slugify_title, normalize_priority, clean_title


def test_slugify_title():
    assert slugify_title("  Ship the Release  ") == "ship-the-release"


def test_normalize_priority():
    assert normalize_priority("URGENT") == "medium"
    assert normalize_priority("High") == "high"


def test_clean_title_valid():
    assert clean_title("  Deploy  ") == "Deploy"


def test_clean_title_empty():
    with pytest.raises(ValueError):
        clean_title("   ")
