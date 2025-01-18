from django.test import TestCase
from django.db import connections

class PersistentTestCase(TestCase):
    # Override the `_fixture_setup` and `_fixture_teardown` methods to prevent data flushing.
    def _fixture_setup(self):
        pass

    def _fixture_teardown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # Iterate over all database aliases in cls.databases
        for db_alias in cls.databases:
            connections[db_alias].creation.destroy_test_db(
                connections[db_alias].settings_dict['NAME'], verbosity=0)
        super().tearDownClass()
