def evaluate_rule(node, user_data):
    if node.node_type == 'operand':
        attribute, operator, value = node.value
        user_value = user_data.get(attribute)

        print(f"Evaluating: {user_value} {operator} {value}")  # Debugging output

        # Comparison logic
        if operator == '>':
            return user_value > int(value)
        elif operator == '<':
            return user_value < int(value)
        elif operator == '>=':
            return user_value >= int(value)
        elif operator == '<=':
            return user_value <= int(value)
        elif operator == '=':
            return user_value == value
        else:
            raise ValueError(f"Invalid operator: {operator}")

    elif node.node_type == 'operator':
        left_result = evaluate_rule(node.left, user_data)
        right_result = evaluate_rule(node.right, user_data)

        print(f"Operator: {node.value}, Left Result: {left_result}, Right Result: {right_result}")  # Debugging output

        # Adjusting logical operations
        if node.value == 'and':
            return left_result and right_result  # Return True only if both are True
        elif node.value == 'or':
            return left_result or right_result  # Return True if at least one is True
        else:
            raise ValueError(f"Invalid operator: {node.value}")
