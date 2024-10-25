# rule_engine/storage.py

import json
from pymongo import MongoClient
from .ast_node import Node

client = MongoClient('mongodb://localhost:27017/')
db = client['rule_engine']
rules_collection = db['rules']

def save_rule(rule_id, rule_ast):
    """
    Save a rule AST to the database.
    """
    rule_json = json.dumps(rule_ast, default=lambda o: o.__dict__)
    rules_collection.insert_one({"rule_id": rule_id, "rule_ast": rule_json})

def load_rule(rule_id):
    """
    Load a rule AST from the database and convert it back to Node objects.
    """
    rule = rules_collection.find_one({"rule_id": rule_id})
    if rule:
        rule_dict = json.loads(rule['rule_ast'])
        return dict_to_node(rule_dict)
    return None

def dict_to_node(data):
    """
    Recursively convert dictionary back to Node objects.
    """
    if not isinstance(data, dict):
        return None
    
    node = Node(data['node_type'], data.get('value'))
    node.left = dict_to_node(data.get('left'))
    node.right = dict_to_node(data.get('right'))
    return node
