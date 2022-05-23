import unittest

from port.models.base_model import BaseModel


class DummyModel(BaseModel):
    pass



class TestBaseModel(unittest.TestCase):

    dummy_model = DummyModel()

    def test_base_model_plugin_name(self):
        self.assertTrue(self.dummy_model.plugin_name == 'tests.models')

    def test_base_model_plugin_id(self):
        self.assertTrue(self.dummy_model.plugin_id == 1)