from rule_engine.rule_parser import create_rule
from rule_engine.rule_combiner import combine_rules
from rule_engine.rule_evaluator import evaluate_rule
from rule_engine.storage import save_rule, load_rule

# Define rule strings
rule1_string = "age > 30 AND salary > 50000"
rule2_string = "department = 'Sales'"  # Adjust rules as needed

# Combine the rules using AND
combined_rule = combine_rules([rule1_string, rule2_string])  

# Save and load rule from the database
save_rule("rule1", combined_rule)
loaded_rule = load_rule("rule1")

# Evaluate user data against the rule
test_cases = [
    {"age": 35, "salary": 60000, "department": "Sales"},     # True (All conditions met)
    {"age": 28, "salary": 70000, "department": "Sales"},     # False (age < 30)
    {"age": 40, "salary": 40000, "department": "Sales"},     # False (salary < 50000)
    {"age": 32, "salary": 75000, "department": "Marketing"},  # False (department != 'Sales')
    {"age": 25, "salary": 30000, "department": "Sales"},     # False (age < 30, salary < 50000)
]

for i, user_data in enumerate(test_cases):
    result = evaluate_rule(loaded_rule, user_data)
    print(f"Test case {i + 1}: Evaluation result:", result)
