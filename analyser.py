# pylint: disable=missing-docstring

import checker
import parser
from tree import Tree, Branch

def create_tree(context):
    root = __create_branch(context)
    tree = Tree(root)
    __order_tree(tree)
    return tree

def __create_branch(context):
    branch = None

    if checker.is_malformed(context):
        branch = Branch(context, malformed=True)
    else:
        if checker.is_basic(context):
            branch = Branch(context.text)
        elif checker.is_statement(context):
            branch = Branch(*parser.parse_statement(context))
        else:
            branch = Branch(*parser.parse_compound(context))

    if not branch.is_leaf():
        branch.left_branch = __create_branch(branch.left_branch)
        branch.right_branch = __create_branch(branch.right_branch)

    return branch

def __order_tree(tree):
    __order_branch(tree.root)

def __order_branch(branch):
    if not branch.is_leaf():
        if branch.element == "AFTER":
            branch.left_branch, branch.right_branch = branch.right_branch, branch.left_branch

        if branch.has_left_branch():
            __order_branch(branch.left_branch)

        if branch.has_right_branch():
            __order_branch(branch.right_branch)
