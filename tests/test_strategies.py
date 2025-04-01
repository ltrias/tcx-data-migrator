import unittest
from src import strategies


class TestDataMigrationContext(unittest.TestCase):
    def testDefaultArguments(self):
        pass
        subject = strategies.DataMigrationContext(src=None, dst=None, metric=None)
        self.assertEqual('HR', subject._metric)


if __name__ == '__main__':
    unittest.main()
