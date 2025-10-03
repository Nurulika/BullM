# test_bullmqworker.py
"""
Tests for BullMQWorker module.
"""

import unittest
from bullmqworker import BullMQWorker

class TestBullMQWorker(unittest.TestCase):
    """Test cases for BullMQWorker class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BullMQWorker()
        self.assertIsInstance(instance, BullMQWorker)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BullMQWorker()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
