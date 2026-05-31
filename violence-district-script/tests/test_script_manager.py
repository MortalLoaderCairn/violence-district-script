import unittest
from src.script_manager import ScriptManager
from src.config import Config

class TestScriptManager(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        self.manager = ScriptManager(self.config)

    def test_execute_valid_script(self):
        result = self.manager.execute_script("test_script")
        self.assertIn("completed", result)

    def test_execute_invalid_script(self):
        with self.assertRaises(ValueError):
            self.manager.execute_script("nonexistent")

    def test_execute_script_failure(self):
        # Force failure by mocking random
        import random
        random.choice = lambda x: False
        with self.assertRaises(RuntimeError):
            self.manager.execute_script("test_script")

if __name__ == "__main__":
    unittest.main()