import unittest
from unittest.mock import MagicMock
from ProductionClass import ProductionClass


class TestMock(unittest.TestCase):

    # basic use case
    # mock out a method's return value
    def test_mock_01(self):

        # Arrange
        sut = ProductionClass
        sut.method = MagicMock(return_value=3)

        # Act
        result = sut.method(3, 4, 5, key='value')

        # Assert
        assert result == 3
        sut.method.assert_called_with(3, 4, 5, key='value')

    # more useful basic use case
    # mock out the methods the sut uses
    def test_mock_02(self):

        # Arrange
        sut = ProductionClass()
        sut.sub_method = MagicMock(return_value=5)
        sut.sub_method_2 = MagicMock(return_value=8)

        # Act
        result = sut.method(0, 4, 5)

        # Assert
        assert result == 8
        sut.sub_method.assert_not_called()
        sut.sub_method_2.assert_called_once_with(sut, 4, 5)
