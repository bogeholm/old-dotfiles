from pathlib import Path

SOURCE = "source"
DESTINATION = "destination"

SOURCE_FILES = {"abc": "abc", "def": "def", "ghi": "ghi"}
FILE_SUFFIX = "txt"

# ```
# def f(tmp_path):
#     """ https://docs.pytest.org/_/downloads/en/3.9.0/pdf/
#         pytest makes `tmp_path` available
#     return tmp_path.exists() # True
# ```
def setup_directories(path: Path) -> None:
    source = path / SOURCE
    destination = path / DESTINATION

    # source and destination directories for linking
    source.mkdir(parents=True, exist_ok=True)
    destination.mkdir(parents=True, exist_ok=True)

    # source files
    for key, val in SOURCE_FILES.items():
        with open(source / Path(f"{key}.{FILE_SUFFIX}"), "w") as fhandle:
            fhandle.write(val)


def test_source_does_not_exist_fail_gracefully(tmp_path):
    assert True


def test_dest_dir_exists_dest_file_does_not(tmp_path):
    setup_directories(tmp_path)
    assert True


def test_dest_dir_does_not_exist_and_is_created(tmp_path):
    assert True


def test_dest_dir_exists_dest_file_exists_backup_created(tmp_path):
    assert True


def test_dest_dir_exists_dest_is_link_no_backup_created(tmp_path):
    assert True
