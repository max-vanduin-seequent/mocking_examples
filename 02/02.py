import unittest
from unittest.mock import MagicMock, patch
from ImportingClass import ImportingClass


class TestMock(unittest.TestCase):

    @patch('math.pi')
    @patch('math.e')
    def test_mock_01(self, complex_object, second_complex_object):

        # Arrange
        sut = ImportingClass(complex_object=complex_object, second_complex_object=second_complex_object)
        sut.local_method = MagicMock(return_value=complex_object)

        # Act
        result = sut.method_using_imports(False)

        # Assert
        assert result == complex_object
