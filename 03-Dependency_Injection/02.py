import unittest

from unittest.mock import MagicMock, patch
from ImportingClass import ImportingClass


class TestMock(unittest.TestCase):

    # Works as normal due to default value
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

    @patch('math.pi')
    @patch('math.e')
    def test_mock_02(self, complex_object, second_complex_object):

        # Arrange
        sut = ImportingClass(complex_object=complex_object, second_complex_object=second_complex_object)

        # Act
        try:
            sut.method_using_imports(True)

        # Assert
        except KeyError as ke:
            print(ke)
            assert ke.args[0] == "This always fails"
        else:
            assert False, "Error should have been thrown"
