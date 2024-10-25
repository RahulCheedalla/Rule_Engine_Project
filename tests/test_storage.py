# tests/test_storage.py

import unittest
from pymongo import MongoClient
from rule_engine.rule_parser import create_rule
from rule_engine.storage import save_rule, load_rule

class TestStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up MongoDB connection for testing."""
        cls.client = MongoClient('mongodb://localhost:27017/')
        cls.db = cls.client['rule_engine_test']  # Use a test database
        cls.rules_collection = cls.db['rules']
        cls.rules_collection.delete_many({})  # Clean up the collection before tests

    @classmethod
    def tearDownClass(cls):
        """Close the MongoDB connection after all tests."""
        cls.client.close()

    def test_save_rule(self):
        """Test saving a rule to the database."""
        rule = create_rule("age > 30 AND salary > 50000")
        save_rule("test_rule1", rule)

        # Verify that the rule has been saved in the database
        saved_rule = self.rules_collection.find_one({"rule_id": "test_rule1"})
        self.assertIsNotNone(saved_rule)
        self.assertIn("rule_ast", saved_rule)

    def test_load_rule(self):
        """Test loading a rule from the database."""
        rule = create_rule("department = 'Sales'")
        save_rule("test_rule2", rule)

        # Load the rule from the database and verify it matches the saved rule
        loaded_rule = load_rule("test_rule2")
        self.assertEqual(loaded_rule['node_type'], 'operand')
        self.assertEqual(loaded_rule['value'][0], 'department')
        self.assertEqual(loaded_rule['value'][1], '=')
        self.assertEqual(loaded_rule['value'][2], 'Sales')

    def test_load_nonexistent_rule(self):
        """Test loading a rule that doesn't exist."""
        loaded_rule = load_rule("nonexistent_rule")
        self.assertIsNone(loaded_rule)

if __name__ == '__main__':
    unittest.main()
