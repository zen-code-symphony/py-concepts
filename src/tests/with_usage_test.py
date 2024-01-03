from unittest.mock import Mock, patch

import pytest

from app.with_usage import ManagedFile, PrintIndenter, managed_file

_FILE_NAME = "filename.txt"


@pytest.fixture
def mocked_file_calls(mocker):
    mock_file = Mock()
    mock_open = mocker.mock_open(mock_file)
    mock_open.return_value = mock_file
    mocker.patch("builtins.open", mock_open)
    return (mock_file, mock_open)


def test_open_with_class_based_context_manager(mocked_file_calls):
    mock_file, mock_open = mocked_file_calls
    file = ManagedFile(_FILE_NAME)
    with file as _:
        mock_open.assert_called_with(_FILE_NAME)
    mock_file.close.assert_called_once()
    assert file.file is None


def test_open_with_decorator_based_context_manager(mocked_file_calls):
    mock_file, mock_open = mocked_file_calls
    file = managed_file(_FILE_NAME)
    with file as _:
        mock_open.assert_called_with(_FILE_NAME)
    mock_file.close.assert_called_once()


@patch("builtins.print")
def test_nested_context_management(mock_print):
    with PrintIndenter() as indenter:
        indenter.print("This")
        mock_print.assert_called_with("    This")
        assert indenter.level == 1
        with indenter:
            indenter.print("is")
            mock_print.assert_called_with("        is")
            assert indenter.level == 2
            with indenter:
                indenter.print("sooo")
                mock_print.assert_called_with("            sooo")
                assert indenter.level == 3
        indenter.print("cool!")
        mock_print.assert_called_with("    cool!")
        assert indenter.level == 1
