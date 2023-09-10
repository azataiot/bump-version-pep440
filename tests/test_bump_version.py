# tests/test_bump_version.py

import pytest

from src.bump_version import bump_version


# Define a fixture for safe default parameters
@pytest.fixture
def safe_params():
    return {"tag": False, "commit": False, "dry_run": True}


def test_bump_major_version(safe_params):
    # Test bumping a major version
    assert bump_version("major", current_version="1.2.3", **safe_params) == "2.0.0"


def test_bump_minor_version(safe_params):
    # Test bumping a minor version
    assert bump_version("minor", current_version="1.2.3", **safe_params) == "1.3.0"


def test_bump_micro_version(safe_params):
    # Test bumping a micro version
    assert bump_version("micro", current_version="1.2.3", **safe_params) == "1.2.4"


def test_invalid_version_type(safe_params):
    # Test providing an invalid version type
    with pytest.raises(ValueError):
        bump_version("invalid_type", current_version="1.2.3", **safe_params)


def test_new_version_not_greater(safe_params):
    # Test when the new version is not greater than the current version
    with pytest.raises(ValueError):
        bump_version(
            "micro", current_version="1.2.3", new_version="1.2.2", **safe_params
        )
