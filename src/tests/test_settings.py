from __future__ import annotations

from typed_settings import EnvLoader, load_settings
from utilities.os import temp_environ

from uv_publish.settings import Settings


class TestSettings:
    def test_empty_strs(self) -> None:
        with temp_environ(TOKEN="", USERNAME="", PASSWORD="", PUBLISH_URL=""):
            settings = load_settings(Settings, [EnvLoader("")])
        assert settings.token is None
        assert settings.username is None
        assert settings.password is None
        assert settings.publish_url is None
