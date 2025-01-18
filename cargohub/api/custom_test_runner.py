from django.test.runner import DiscoverRunner

class NoFlushTestRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):
        # Override to avoid database flush or reset
        pass

    def teardown_databases(self, old_config, **kwargs):
        # Override to avoid database flush or reset
        pass
