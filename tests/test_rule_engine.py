# tests/test_rule_engine.py

import unittest
from rule_engine.rule_parser import create_rule
from rule_engine.rule_combiner import combine_rules
from rule_engine.rule_evaluator import evaluate_rule

class TestRuleEngine(unittest.TestCase):
    
    def test_create_rule(self):
        rule = create_rule("age > 30 AND department = 'Sales'")
        self.assertEqual(rule.node_type, 'operator')
        self.assertEqual(rule.value, 'and')

    def test_combine_rules(self):
        combined_rule = combine_rules(["age > 30", "salary > 50000"])
        self.assertEqual(combined_rule.node_type, 'operator')
        self.assertEqual(combined_rule.value, 'or')

    def test_evaluate_rule(self):
        rule = create_rule("age > 30 AND salary > 50000")
        user_data = {"age": 35, "salary": 60000}
        result = evaluate_rule(rule, user_data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
