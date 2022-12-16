import unittest
from unittest.mock import MagicMock
from ImportingClass import ImportingClass


class TestMock(unittest.TestCase):

    def test_mock_01(self):

        # Arrange
        complex_object = MagicMock()
        second_complex_object = MagicMock()

        sut = ImportingClass(complex_object=complex_object, second_complex_object=second_complex_object)
        sut.local_method = MagicMock(return_value=3)

        # Act
        result = sut.method_using_imports(False)

        # Assert
        assert(result == 3)
        sut.local_method.assert_called_once_with(False)
