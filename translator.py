# pylint: disable=missing-docstring,line-too-long

import analyser
from context import Context
from expressions import MATCHING

def translate(source):
    prepared_source = __prepare_source(source)

    initial_context = Context(prepared_source)
    initial_context.create_contexts()

    command_tree = analyser.create_tree(initial_context)

    return __generate_commands(command_tree)

def __prepare_source(source):
    source_lines = source.split("\n")
    joined_source = ") THEN (".join(source_lines)

    return __clear_useless_parentheses(f"({joined_source})")

def __clear_useless_parentheses(source):
    matches = MATCHING["useless_parentheses"].findall(source)

    while matches:
        for match in matches:
            replace_string = f"({match})"
            source = source.replace(replace_string, match)
        matches = MATCHING["useless_parentheses"].findall(source)

    return source

def __generate_commands(tree):
    commands = __generate_branch_command(tree.root)

    return commands

def __generate_branch_command(branch):
    commands = []

    if branch.is_leaf():
        commands.append(__get_basic_command(branch))
    else:
        if branch.has_left_branch():
            commands += __generate_branch_command(branch.left_branch)

        if branch.has_right_branch():
            commands += __generate_branch_command(branch.right_branch)

    return commands


def __get_basic_command(leaf):
    match = MATCHING["basic"].match(leaf.element)
    command = match.group(1)
    offset = int(match.group(2))

    return (command, offset)
