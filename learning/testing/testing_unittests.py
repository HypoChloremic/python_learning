from unittest import mock
from scripts.scripts_to_test import calling


@mock.patch('utils.classes_to_be_imported.ClassCalledOnce.save')
@mock.patch('scripts.scripts_to_test.method_to_be_called')
def test_calling(mock_method_to_be_called, mock_save):
    mock_method_to_be_called.return_value = 2
    calling()
    mock_method_to_be_called.assert_called_once()
    mock_save.assert_called() 
    mock_save.assert_called_once()
    print("success")

if __name__ == '__main__':
    test_calling()