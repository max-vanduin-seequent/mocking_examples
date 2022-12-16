import unittest

from unittest.mock import patch, MagicMock
from ImportingClass import ImportingClass
from ProductionClass import ProductionClass


class TestMock(unittest.TestCase):

    # Dependency Injection allows to inject the code we're dependent on, replacing it with a mock
    @patch('math.pi')
    @patch('math.e')
    def test_mock_01(self, complex_object, second_complex_object):

        # Arrange
        mock_production_class = MagicMock(spec=ProductionClass)
        mock_production_class.method_that_will_fail.return_value = 3

        sut = ImportingClass(production_class=mock_production_class,
                             complex_object=complex_object,
                             second_complex_object=second_complex_object)

        # Act
        result = sut.method_using_imports(True)

        # Assert
        assert result == 3
        mock_production_class.method_that_will_fail.assert_called_once_with(True)
