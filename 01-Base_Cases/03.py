import unittest
from unittest.mock import MagicMock
from ProductionClass import ProductionClass


class TestMock(unittest.TestCase):

    # the mocked values will be called, return a generated mock value if not specified
    def test_mock_03(self):

        # Arrange
        sut = ProductionClass()
        sut.sub_method = MagicMock(return_value=4)
        sut.sub_method_2 = MagicMock(return_value=5)
        sut.complex_sub_method = MagicMock(return_value='world')

        # Act
        result = sut.complex_method(True, False, False)

        # Assert
        print(result)
        sut.sub_method.assert_called_once_with(True)
        sut.sub_method_2.assert_called_once_with(False, False)
        sut.complex_sub_method.assert_called_once_with(4, 5)
