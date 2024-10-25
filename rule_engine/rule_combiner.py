from .rule_parser import create_rule  
from .ast_node import Node

def combine_rules(rules):
    if len(rules) == 1:
        return create_rule(rules[0])
    
    combined_node = create_rule(rules[0])  # Start combining from the first rule
    
    for rule in rules[1:]:
        new_combined = Node('operator', 'and')  
        new_combined.left = combined_node
        new_combined.right = create_rule(rule)
        combined_node = new_combined
    
    return combined_node
