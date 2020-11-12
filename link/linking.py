import git
import yaml
from pathlib import Path

def get_repo_path() -> Path:
    """ https://stackoverflow.com/questions/22081209
    """
    git_repo = git.Repo(__file__, search_parent_directories=True)
    git_root = git_repo.git.rev_parse("--show-toplevel")
    return Path(git_root)

with open("files.yml", "r") as fhandle:
    files = yaml.safe_load(fhandle)

print(files)