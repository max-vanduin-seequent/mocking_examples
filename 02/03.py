import unittest

from unittest.mock import patch
from ImportingClass import ImportingClass
import ProductionClass


class TestMock(unittest.TestCase):

    @patch.object(ProductionClass.ProductionClass,
                  'method_that_will_fail',
                  lambda a: 3)
    @patch('math.pi')
    @patch('math.e')
    def test_mock_01(self, complex_object, second_complex_object):

        # Arrange
        sut = ImportingClass(complex_object=complex_object, second_complex_object=second_complex_object)

        # Act
        result = sut.method_using_imports("this is a valid value")

        # Assert
        assert result == 3
