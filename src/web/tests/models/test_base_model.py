import unittest

from server.models.base_model import BaseModel


class DummyModel(BaseModel):
    pass


class TestBaseModel(unittest.TestCase):

    dummy_model = DummyModel()

    def test_base_model_plugin_name(self):
        print(self.dummy_model.plugin_name)
        self.assertTrue(self.dummy_model.plugin_name == 'tests')

    def test_base_model_plugin_id(self):
        self.assertTrue(self.dummy_model.plugin_id == 1)
