# pylint: disable=missing-docstring

import context_parser
from context import Context
from tree import Tree, Branch
from expressions import CHECKING

def create_tree(context):
    root = create_branch(context)
    tree = Tree(root)
    order_tree(tree)
    return tree


def create_branch(context):
    branch = None

    if is_malformed(context):
        branch = Branch(context, malformed=True)
    else:
        if is_basic(context):
            branch = Branch(context.text)
        elif is_statement(context):
            branch = context_parser.parse_statement(context)
        else:
            branch = context_parser.parse_compound(context)

        create_sub_branches(branch)

    return branch


def create_sub_branches(branch):
    branch.left_branch = process_sub_branch(branch.left_branch)
    branch.right_branch = process_sub_branch(branch.right_branch)

    return branch


def process_sub_branch(sub_branch):
    if isinstance(sub_branch, Context):
        return create_branch(sub_branch)
    elif isinstance(sub_branch, Branch):
        return create_sub_branches(sub_branch)
    else:
        return None


def order_tree(tree):
    order_branch(tree.root)


def order_branch(branch):
    if not branch.is_leaf():
        if branch.element == "AFTER":
            branch.left_branch, branch.right_branch = branch.right_branch, branch.left_branch

        if branch.has_left_branch():
            order_branch(branch.left_branch)

        if branch.has_right_branch():
            order_branch(branch.right_branch)


def is_malformed(context):
    compound = is_compound(context)
    statement = is_statement(context)

    if context.has_sub_contexts():
        return not statement and not compound

    return not is_basic(context) and not statement and not compound


def is_basic(context):
    return CHECKING["basic"].match(context.text)


def is_statement(context):
    return CHECKING["statement"].match(context.text)


def is_compound(context):
    return CHECKING["compound"].match(context.text)
