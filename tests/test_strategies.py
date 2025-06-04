
import unittest
from unittest.mock import MagicMock
from src import strategies

class TestTrackpointIndexStrategy(unittest.TestCase):
    
    def setUp(self):
        self.subject = strategies.TrackpointIndexStrategy()
        
        self.bigTCXData = [*range(100)]
        small_hr_data = [*range(10)]
        self.smallTCXData = small_hr_data
        self.revSmallTCXData = [*reversed(small_hr_data)]
    
    @unittest.skip("Actually a DataMigationContext test")
    def testDefaultArguments(self):
        subject = strategies.DataMigrationContext(None, None) 
        self.assertEqual('HR', subject._metric)
        self.assertIsInstance(subject._strategy, strategies.TrackpointIndexStrategy)

    def test_same_number_of_samples(self):
        self.subject.migrate(self.smallTCXData, self.revSmallTCXData)
        self.assertEqual(self.smallTCXData, self.revSmallTCXData)

    def test_src_has_more_samples(self):
        size_before = len(self.revSmallTCXData)
        self.subject.migrate(self.bigTCXData, self.revSmallTCXData)
        self.assertEqual(self.bigTCXData[:len(self.revSmallTCXData)], self.revSmallTCXData)
        self.assertEqual(size_before, len(self.revSmallTCXData))

    def test_src_has_less_samples(self):
        size_before = len(self.bigTCXData)
        self.subject.migrate(self.revSmallTCXData, self.bigTCXData)
        self.assertEqual(self.revSmallTCXData, self.bigTCXData[:len(self.revSmallTCXData)])
        self.assertEqual(size_before, len(self.bigTCXData))