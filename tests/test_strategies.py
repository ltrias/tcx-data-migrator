
import unittest
from src import strategies

class TestTrackpointIndexStrategy(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass


    def testDefaultArguments(self):
        subject = strategies.DataMigrationContext(None, None) 
        self.assertEqual('HR', subject._metric)
        self.assertIsInstance(subject._strategy, strategies.TrackpointIndexStrategy)

    def test_same_number_of_samples(self):
        self.fail()

    def test_src_has_more_samples(self):
        self.fail()

    def test_src_has_less_samples(self):
        self.fail()