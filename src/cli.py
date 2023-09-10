# src/cli.py
from typing import Optional

import typer

from .bump_version import bump_version

app = typer.Typer()


@app.command()
def bump(
    version_type: str,
    current_version: Optional[str] = typer.Option(
        None,
        "--current-version",
        "-c",
        help="Current version to be used instead of reading from pyproject.toml.",
    ),  # noqa: E501
    new_version: Optional[str] = typer.Option(
        None,
        "--new-version",
        "-n",
        help="New version to be set instead of incrementing the current version.",
    ),
    commit: bool = typer.Option(
        False, "--commit", help="If set, a git commit will be created."
    ),
    commit_message: Optional[str] = typer.Option(
        None, "--commit-message", help="Custom commit message."
    ),
    dry_run: bool = typer.Option(
        False, "--dry-run", help="If set, no actual changes will be made, only printed."
    ),
    tag: bool = typer.Option(False, "--tag", help="If set, a git tag will be created."),
    tag_name: Optional[str] = typer.Option(None, "--tag-name", help="Custom tag name."),
):
    """
    Bump the version based on the provided version type and other parameters.
    """
    try:
        new_version = bump_version(
            version_type=version_type,
            current_version=current_version,
            new_version=new_version,
            commit=commit,
            commit_message=commit_message,
            dry_run=dry_run,
            tag=tag,
            tag_name=tag_name,
        )
        typer.echo(f"Version bumped to: {new_version}")
    except ValueError as e:
        typer.echo(typer.style(str(e), fg=typer.colors.RED))
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
