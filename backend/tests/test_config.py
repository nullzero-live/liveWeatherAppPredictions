import pytest
from ..api import Config  # replace 'your_module' with the actual module name

def test_config_get_existing_key():
    assert Config.get("VERIFY_SSL") is True

def test_config_set_existing_key():
    Config.set("VERIFY_SSL", False)
    assert Config.get("VERIFY_SSL") is False

def test_config_set_non_existing_key():
    with pytest.raises(KeyError):
        Config.set("NON_EXISTING_KEY", True)
