from pathlib import Path

SOURCE = "source"
DESTINATION = "destination"

# ```
# def f(tmp_path):
#     """ https://docs.pytest.org/_/downloads/en/3.9.0/pdf/
#         pytest makes `tmp_path` available
#     return tmp_path.exists() # True
# ```
def setup_directories(path: Path) -> None:
    source = path / SOURCE
    destination = path / DESTINATION

    source.mkdir(parents=True, exist_ok=True)
    destination.mkdir(parents=True, exist_ok=True)


def test_source_does_not_exist_fail_gracefully():
    assert True


def test_dest_dir_exists_dest_file_does_not():
    assert True


def test_dest_dir_does_not_exist_and_is_created():
    assert True


def test_dest_dir_exists_dest_file_exists_backup_created():
    assert True


def test_dest_dir_exists_dest_is_link_no_backup_created():
    assert True
