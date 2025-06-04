
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

    def test_same_number_of_samples(self):
        result = self.subject.migrate(self.smallTCXData, self.revSmallTCXData)
        self.assertEqual(self.smallTCXData, result)

    def test_src_has_more_samples(self):
        size_before = len(self.revSmallTCXData)
        result = self.subject.migrate(self.bigTCXData, self.revSmallTCXData)
        self.assertEqual(self.bigTCXData[:len(self.revSmallTCXData)], result)
        self.assertEqual(size_before, len(result))

    def test_src_has_less_samples(self):
        size_before = len(self.bigTCXData)
        result = self.subject.migrate(self.revSmallTCXData, self.bigTCXData)
        self.assertEqual(self.revSmallTCXData, result[:len(self.revSmallTCXData)])
        self.assertEqual(size_before, len(result))
        self.assertEqual(self.bigTCXData[len(self.revSmallTCXData):], result[len(self.revSmallTCXData):])