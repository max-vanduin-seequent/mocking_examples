import unittest
from unittest.mock import MagicMock
from ProductionClass import ProductionClass
from ExternalClass import ExternalClass


class TestMock(unittest.TestCase):

    # simple side effect examples
    def test_mock_01(self):

        sut = ProductionClass()
        sut.sub_method = MagicMock(side_effect=KeyError("Dangerous Error"))

        try:
            print(sut.method(True, 'foo', 'bar'))
        except KeyError as ke:
            print(ke)
            assert True
        else:
            assert False, "Error should have been thrown"

    def test_mock_02(self):

        sut = ProductionClass()
        external_class = ExternalClass()
        sut.sub_method = MagicMock(side_effect=external_class.increment_value())

        print(sut.method(True, 'foo', 'bar'))

        assert external_class.get_value() == 1
