import graphviz
from queue import Queue

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_expression_tree(expression):
    stack = []
    for char in expression:
        if char.isdigit() or char == '.':
            stack.append(TreeNode(char))
        elif char == '(':
            stack.append(char)
        elif char == ')':
            sub_expression = []
            while stack[-1] != '(':
                sub_expression.append(stack.pop())
            stack.pop()  # Remove '(' from the stack
            sub_expression.reverse()
            stack.append(sub_expression)
        else:
            stack.append(char)
    
    # Reorganize stack to create the expression tree
    operator_stack = []
    operand_stack = []
    for item in stack:
        if isinstance(item, list):
            operand_stack.append(build_expression_tree(item))
        elif isinstance(item, TreeNode):  # Check if item is a TreeNode
            operand_stack.append(item)
        elif item in {'+', '-', '*', '/'}:
            operator_stack.append(item)
    
    while operator_stack:
        operator = operator_stack.pop()
        right = operand_stack.pop()
        left = operand_stack.pop()
        operator_node = TreeNode(operator)
        operator_node.left = left
        operator_node.right = right
        operand_stack.append(operator_node)
    
    return operand_stack[0]  # Root of the expression tree

def print_tree_dot(node, dot):
    if node is not None:
        if node.left is not None:
            dot.node(str(node.left.value))
            dot.edge(str(node.value), str(node.left.value))
            print_tree_dot(node.left, dot)
        if node.right is not None:
            dot.node(str(node.right.value))
            dot.edge(str(node.value), str(node.right.value))
            print_tree_dot(node.right, dot)

def main():
    expression = input("Ingrese una expresión aritmética: ")
    root = build_expression_tree(expression)
    
    dot = graphviz.Digraph(comment='Árbol de expresiones')
    dot.node(str(root.value))
    print_tree_dot(root, dot)
    dot.render(filename='arbol_expresiones', format='png', directory='C:\\Users\\jargueta\\Desktop', cleanup=True)

if __name__ == "__main__":
    main()
