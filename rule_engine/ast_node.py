# rule_engine/ast_node.py

class Node:
    def __init__(self, node_type, value=None):
        """
        Initialize a Node.

        :param node_type: 'operator' for AND/OR, 'operand' for conditions
        :param value: Optional value for operand nodes (e.g., condition string like 'age > 30')
        """
        self.node_type = node_type  # 'operator' or 'operand'
        self.left = None  # Left child (for binary operators)
        self.right = None  # Right child (for binary operators)
        self.value = value  # For operand nodes, store the condition value
