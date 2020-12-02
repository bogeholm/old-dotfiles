"""Unit tests for sync.sync.PathMap"""

from pathlib import Path
from typing import List

from sync.sync import PathMap, BACKUP_SUFFIX

SOURCE_DIR = Path("source")
DESTINATION_DIR = Path("destination")

SOURCE_FILES_AND_CONTENTS_MAP = {"abc": "abc", "def": "def", "ghi": "ghi"}
FILE_SUFFIX = "txt"


def get_source_file_list() -> List[Path]:
    """Make a list of available files"""
    file_names = list(SOURCE_FILES_AND_CONTENTS_MAP.keys())
    return [Path(f"{file_name}.{FILE_SUFFIX}") for file_name in file_names]


def setup_directories(path: Path) -> None:
    """Setup test directories:
    - source/abc.txt
    - source/def.txt
    - source/ghi.txt
    - destination/
    """
    source = path / SOURCE_DIR
    destination = path / DESTINATION_DIR

    # source and destination directories for linking
    source.mkdir(parents=True, exist_ok=True)
    destination.mkdir(parents=True, exist_ok=True)

    # source files
    for key, val in SOURCE_FILES_AND_CONTENTS_MAP.items():
        with open(source / Path(f"{key}.{FILE_SUFFIX}"), "w") as fhandle:
            fhandle.write(val)


def test_source_does_not_exist_fail_gracefully(tmp_path):
    """Check that we fail gracefully if source doesn't exist"""

    # Note missing call to `setup_directories()`

    source_file_list = get_source_file_list()
    source_file = source_file_list[0]
    source = tmp_path / SOURCE_DIR / source_file
    destination = tmp_path / DESTINATION_DIR / source_file

    pathmap = PathMap(str(source), str(destination))
    assert not source.exists()
    pathmap.link()


def test_dest_dir_exists_dest_file_does_not(tmp_path):
    """source/abc.txt exists
    destination/abc.txt does not
    destination/abc.txt is created
    """
    setup_directories(tmp_path)

    source_file_list = get_source_file_list()
    source_file = source_file_list[0]
    source = tmp_path / SOURCE_DIR / source_file
    destination = tmp_path / DESTINATION_DIR / source_file

    pathmap = PathMap(str(source), str(destination))
    pathmap.link()

    assert destination.exists()
    assert destination.is_symlink()


def test_dest_dir_does_not_exist_and_is_created(tmp_path):
    """Make sure that destination directory is created if non-existant"""
    setup_directories(tmp_path)

    source_file_list = get_source_file_list()
    source_file = source_file_list[0]
    source = tmp_path / SOURCE_DIR / source_file
    destination = tmp_path / "alternative_destination" / source_file

    pathmap = PathMap(str(source), str(destination))
    pathmap.link()

    assert destination.exists()
    assert destination.is_symlink()


def test_dest_dir_exists_dest_file_exists_backup_created(tmp_path):
    """Create backup of already existing file"""
    setup_directories(tmp_path)

    source_file_list = get_source_file_list()
    source_file = source_file_list[0]
    source = tmp_path / SOURCE_DIR / source_file
    destination_dir = tmp_path / DESTINATION_DIR
    destination = destination_dir / source_file

    with open(destination, "w") as fhandle:
        fhandle.write("this spot is taken")

    assert destination.exists()
    assert destination.is_file()

    pathmap = PathMap(str(source), str(destination))
    pathmap.link()

    assert destination.is_symlink()

    # Glob for files with the backup suffix
    backup_glob = list(destination_dir.glob(f"*.{BACKUP_SUFFIX}"))
    assert len(backup_glob) == 1


def test_dest_dir_exists_dest_is_link_no_backup_created(tmp_path):
    """Do not create a backup if destination is a link"""
    setup_directories(tmp_path)

    source_file_list = get_source_file_list()
    source_file = source_file_list[0]
    source = tmp_path / SOURCE_DIR / source_file
    destination_dir = tmp_path / DESTINATION_DIR
    destination = destination_dir / source_file

    pathmap = PathMap(str(source), str(destination))
    pathmap.link()

    assert destination.exists()
    assert destination.is_symlink()

    pathmap.link()

    assert destination.exists()
    assert destination.is_symlink()

    # Glob for files with the backup suffix
    backup_glob = list(destination_dir.glob(f"*.{BACKUP_SUFFIX}"))
    assert len(backup_glob) == 0
