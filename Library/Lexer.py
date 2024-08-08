import ast
# Function to build the AST tree

def buildTree(str):
    try:
        tree = ast.parse(str)
        return ast.dump(tree, indent=4)
    except SyntaxError as e:
        return f"SyntaxError: {e}"
