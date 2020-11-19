import git
import toml

from collections import OrderedDict
from datetime import datetime
from pathlib import Path
from typing import Dict


def git_repo_path() -> str:
    """https://stackoverflow.com/questions/22081209"""
    git_repo = git.Repo(__file__, search_parent_directories=True)
    git_root = git_repo.git.rev_parse("--show-toplevel")
    return git_root


def timestamp() -> str:
    DATETIME_FORMAT = "%d-%b-%Y-%H-%M-%S"
    return datetime.now().strftime(DATETIME_FORMAT)


def backup_target_file_if_exists(target: Path) -> None:
    """If target exists, and is not a symlink, back it up as:
        `f"{filename}.{timestamp()}.{BACKUP_SUFFIX}`
    """
    # TODO: Return enum representing backup status
    BACKUP_SUFFIX = "dotfile.sync.backup"

    if not target.exists():
        return
    
    if target.is_symlink():
        return
    
    if target.is_file():
        new_target_name = f"{target.name}.{timestamp()}.{BACKUP_SUFFIX}"
        new_target = target.parent / new_target_name
        # Disregard unlikely case of target already existing - if so, we'll make it somehow.
        target.replace(new_target)


def expand_path(path_template: str) -> Path:
    """Expand placeholders in path template string"""
    expanders: Dict[str, Path] = {"${REPO}": git_repo_path(), "${USER_HOME}": str(Path.home())}

    for variable, value in expanders.items():
        path_template = path_template.replace(variable, value)
    return Path(path_template)


class PathMap:
    def __init__(self, source: str, destination: str):
        self.source: Path = source
        self.destination: Path = destination

    @property
    def source(self) -> Path:
        return self._source

    @source.setter
    def source(self, source: str) -> None:
        self._source = expand_path(source)

    @property
    def destination(self) -> Path:
        return self._destination

    @destination.setter
    def destination(self, destination: str) -> None:
        self._destination = expand_path(destination)

    def link(self) -> None:
        """Create symlink from self.source to self.destination."""
        # TODO: Return enum representing sync status
        if not self.source.exists():
            return False

        # Ensure destination parent directory exists
        self.destination.parent.mkdir(parents=True, exist_ok=True)
        # Backup existing files if needed
        backup_target_file_if_exists(self.destination)
        # Now we can link: https://docs.python.org/3/library/pathlib.html?highlight=link#pathlib.Path.symlink_to
        self.destination.symlink_to(self.source)

    def __repr__(self):
        return f"{self.__class__.__name__}(source='{self.source}', destination='{self.destination}')"

    def __str__(self):
        return f"{self.__class__.__name__}(source='{self.source}', destination='{self.destination}')"


if __name__ == "__main__":
    file_list = toml.load("testfiles.toml")

    res = OrderedDict()
    for title, paths in file_list.items():
        res[title] = PathMap(**paths)
    
    print(timestamp())
    for title, pathmap in res.items():
        #print(title)
        #print(pathmap)
        #print(pathmap.destination.parent)
        #print()
        pathmap.link()
