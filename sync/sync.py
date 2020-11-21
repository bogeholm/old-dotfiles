"""Create symbolic links from present repo to files on host"""

from collections import OrderedDict
from datetime import datetime
from pathlib import Path
from typing import Dict

import git
import toml

BACKUP_SUFFIX = "dotfile.sync.backup"
DATETIME_FORMAT = "%d-%b-%Y-%H-%M-%S"


def git_repo_path() -> str:
    """https://stackoverflow.com/questions/22081209"""
    git_repo = git.Repo(__file__, search_parent_directories=True)
    git_root = git_repo.git.rev_parse("--show-toplevel")
    return git_root


def timestamp() -> str:
    """Return a timestamp in the module specified format"""
    return datetime.now().strftime(DATETIME_FORMAT)


def backup_destination_file_if_exists(destination: Path) -> None:
    """If destination exists, and is not a symlink, back it up as:
    `f"{filename}.{timestamp()}.{BACKUP_SUFFIX}`
    """

    if not destination.exists():
        return

    if destination.is_symlink():
        return

    if destination.is_file():
        new_destination_name = f"{destination.name}.{timestamp()}.{BACKUP_SUFFIX}"
        new_destination = destination.parent / new_destination_name
        # Disregard unlikely case of destination already existing - if so, we'll make it somehow.
        destination.replace(new_destination)


def expand_path(path_template: str) -> Path:
    """Expand placeholders in path template string"""
    expanders: Dict[str, str] = {"${REPO}": git_repo_path(), "${USER_HOME}": str(Path.home())}

    for variable, value in expanders.items():
        path_template = path_template.replace(variable, value)
    return Path(path_template)


class PathMap:
    """Sync (link) files from repository to user's home."""

    def __init__(self, source: str, destination: str):
        self.source: Path = expand_path(source)
        self.destination: Path = expand_path(destination)

    def link(self) -> None:
        """Create symlink from self.source to self.destination."""
        if not self.source.exists():
            return

        # Ensure destination parent directory exists
        self.destination.parent.mkdir(parents=True, exist_ok=True)
        # Backup existing files if needed
        backup_destination_file_if_exists(self.destination)
        # Remove destination if it is a symlink
        if self.destination.is_symlink():
            self.destination.unlink()
        # Now we can link:
        # https://docs.python.org/3/library/pathlib.html?highlight=link#pathlib.Path.symlink_to
        self.destination.symlink_to(self.source)

    def __repr__(self):
        return f"{self.__class__.__name__}(source='{self.source}', destination='{self.destination}')"

    def __str__(self):
        return f"{self.__class__.__name__}(source='{self.source}', destination='{self.destination}')"


if __name__ == "__main__":
    file_list = toml.load(Path(__file__).parent / "testfiles.toml")

    res = OrderedDict()
    for title, paths in file_list.items():
        res[title] = PathMap(**paths)

    print(timestamp())
    for title, pathmap in res.items():
        print(title)
        print(pathmap)
        pathmap.link()
