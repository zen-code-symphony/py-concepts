from unittest.mock import Mock

from app.with_usage import ManagedFile, managed_file

_FILE_NAME = "filename.txt"


def test_open_with_class_based_context_manager(mocker):
    mock_file = Mock()
    mock_open = mocker.mock_open(mock_file)
    mock_open.return_value = mock_file
    mocker.patch("builtins.open", mock_open)
    file = ManagedFile(_FILE_NAME)
    with file as _:
        mock_open.assert_called_with(_FILE_NAME)
    mock_file.close.assert_called_once()
    assert file.file is None


def test_open_with_decorator_based_context_manager(mocker):
    mock_file = Mock()
    mock_open = mocker.mock_open(mock_file)
    mock_open.return_value = mock_file
    mocker.patch("builtins.open", mock_open)
    file = managed_file(_FILE_NAME)
    with file as _:
        mock_open.assert_called_with(_FILE_NAME)
    mock_file.close.assert_called_once()
