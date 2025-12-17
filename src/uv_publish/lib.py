from __future__ import annotations

from subprocess import check_call

from utilities.tempfile import TemporaryDirectory

from uv_publish.logging import LOGGER
from uv_publish.settings import SETTINGS


def uv_publish(*, trusted_publishing: bool = SETTINGS.trusted_publishing) -> None:
    with TemporaryDirectory() as temp:
        _log_run("uv", "build", "--out-dir", str(temp), "--wheel", "--clear")
        _log_run(
            "uv",
            "publish",
            *(["--trusted-publishing", "always"] if trusted_publishing else []),
            f"{temp}/*",
        )


def _log_run(*cmds: str) -> None:
    LOGGER.info("Running '%s'...", " ".join(cmds))
    _ = check_call(cmds, text=True)


__all__ = ["uv_publish"]
