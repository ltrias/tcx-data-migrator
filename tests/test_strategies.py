
import unittest
from unittest.mock import MagicMock
from src import strategies

class TestTrackpointIndexStrategy(unittest.TestCase):
    
    def setUp(self):
        self._bigTCXData = [*range(100)]
        small_hr_data = [*range(10)]
        self._smallTCXData = small_hr_data
        self._revSmallTCXData = [*reversed(small_hr_data)]
    
    @unittest.skip("Actually a DataMigationContext test")
    def testDefaultArguments(self):
        self.fail()
        subject = strategies.DataMigrationContext(None, None) 
        self.assertEqual('HR', subject._metric)
        self.assertIsInstance(subject._strategy, strategies.TrackpointIndexStrategy)

    def test_same_number_of_samples(self):
        subject = strategies.TrackpointIndexStrategy()
        subject.migrate(self._smallTCXData, self._revSmallTCXData)
        self.assertEqual(self._smallTCXData, self._revSmallTCXData)

    def test_src_has_more_samples(self):
        self.fail()

    def test_src_has_less_samples(self):
        self.fail()