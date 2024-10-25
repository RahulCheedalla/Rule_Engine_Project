import re
from .ast_node import Node

def parse_condition(condition):
    pattern = r"(\w+)\s*(>=|<=|>|<|=)\s*(\d+|'[^']*'|\"[^\"]*\")"
    match = re.match(pattern, condition)
    if match:
        attribute, operator, value = match.groups()
        if value.startswith(("'", '"')) and value.endswith(("'", '"')):
            value = value[1:-1]
        return attribute, operator, value
    else:
        raise ValueError("Invalid condition format")

def create_rule(rule_string):
    tokens = re.split(r'(\band\b|\bor\b)', rule_string, flags=re.IGNORECASE)

    def build_ast(tokens):
        if len(tokens) == 1:
            attribute, operator, value = parse_condition(tokens[0].strip())
            return Node('operand', (attribute, operator, value))
        
        operator_token = tokens[1].strip().lower()  
        operator_node = Node('operator', operator_token)
        
        operator_node.left = build_ast([tokens[0].strip()])
        operator_node.right = build_ast([tokens[2].strip()])
        
        return operator_node

    return build_ast(tokens)
