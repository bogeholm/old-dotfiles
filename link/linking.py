import git
import toml

from collections import OrderedDict
from pathlib import Path
from typing import Dict

def git_repo_path() -> str:
    """https://stackoverflow.com/questions/22081209"""
    git_repo = git.Repo(__file__, search_parent_directories=True)
    git_root = git_repo.git.rev_parse("--show-toplevel")
    return git_root


class PathMap:
    def __init__(self, source: str, destination: str):
        self.source: Path = source
        self.destination: Path = destination

    @property
    def source(self) -> Path:
        return self._source

    @source.setter
    def source(self, source: str) -> None:
        self._source = self.path_expansion(source)

    @property
    def destination(self) -> Path:
        return self._destination

    @destination.setter
    def destination(self, destination: str) -> None:
        self._destination = self.path_expansion(destination)

    @staticmethod
    def path_expansion(path_template: str) -> Path:

        expanders: Dict[str, Path] = {"${REPO}": git_repo_path(), "${USER_HOME}": str(Path.home())}

        for variable, value in expanders.items():
            path_template = path_template.replace(variable, value)

        return Path(path_template)

    def __repr__(self):
        return f"{self.__class__.__name__}(source='{self.source}', destination='{self.destination}')"

    def __str__(self):
        return f"{self.__class__.__name__}(source='{self.source}', destination='{self.destination}')"


if __name__ == "__main__":
    file_list = toml.load("files.toml")

    res = OrderedDict()
    for title, paths in file_list.items():
        res[title] = PathMap(**paths)
    
    for title, pathmap in res.items():
        print(title)
        print(pathmap)
        print()
