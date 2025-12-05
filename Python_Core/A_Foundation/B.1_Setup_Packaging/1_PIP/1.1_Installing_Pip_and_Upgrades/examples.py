"""Examples for installing and upgrading pip consistently.

The functions favour generating explicit command invocations so learners can
adapt them to their own shell. Nothing is executed automatically to keep the
module side-effect free.
"""

from __future__ import annotations

from pathlib import Path
from shlex import quote
from typing import Iterable


def default_python() -> str:
	"""Return the platform-neutral prefix for invoking pip via the interpreter."""

	return "python"


def upgrade_pip_command() -> list[str]:
	"""Build the recommended upgrade command for pip."""

	return [default_python(), "-m", "pip", "install", "--upgrade", "pip"]


def check_pip_version_command() -> list[str]:
	"""Return a command that prints the pip version and executable location."""

	return [default_python(), "-m", "pip", "--version"]


def user_install_command(package: str) -> list[str]:
	"""Generate a command to install *package* in the current user's site-packages."""

	return [default_python(), "-m", "pip", "install", "--user", package]


def ensure_user_site_export() -> list[str]:
	"""Command for printing the user site directory to verify --user placement."""

	return [default_python(), "-m", "site", "--user-site"]


def format_command(tokens: Iterable[str]) -> str:
	return " ".join(quote(token) for token in tokens)


def write_upgrade_script(path: Path) -> None:
	"""Create a helper shell script that upgrades pip and reports the new version."""

	commands = [
		format_command(upgrade_pip_command()),
		format_command(check_pip_version_command()),
	]
	path.write_text("\n".join(commands) + "\n", encoding="utf-8")


if __name__ == "__main__":
	print("Recommended commands:")
	print("  upgrade ->", format_command(upgrade_pip_command()))
	print("  version ->", format_command(check_pip_version_command()))
	print("  user install ->", format_command(user_install_command("example")))