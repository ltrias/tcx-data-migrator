
import unittest
from src import strategies

class TestTrackpointIndexStrategy(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass


    def testDefaultArguments(self):
        pass
        subject = strategies.DataMigrationContext(src=None, dst=None, metric=None)
        self.assertEqual('HR', subject._metric)

    def test_same_number_of_samples(self):
        self.fail()

    def test_src_has_more_samples(self):
        self.fail()

    def test_src_has_less_samples(self):
        self.fail()




if __name__ == '__main__':
    unittest.main()
