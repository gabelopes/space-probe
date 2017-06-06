# pylint: disable=missing-docstring,line-too-long

from expressions import MATCHING, CHECKING
from tree import Branch

def parse_statement(context):
    match = MATCHING["statement"].match(context.text)
    statement = match.group(2)
    left = get_context(match.group(1), context)
    right = get_context(match.group(3), context)

    return Branch(statement, left, right)


def get_context(text, context):
    if CHECKING["basic"].match(text):
        return Branch(text)

    index = int(MATCHING["context"].match(text).group(1))
    return context.contexts[index]


def parse_compound(context):
    matches = MATCHING["compound"].findall(context.text)
    first_branch = current_branch = get_branch(context, *matches[0])
    last_branch = get_branch(context, *matches[-1])

    for command, statement in matches[1:-1]:
        current_branch.right_branch = get_branch(context, command, statement)
        current_branch = current_branch.right_branch

    current_branch.right_branch = last_branch

    return first_branch


def get_branch(context, command, statement):
    if statement:
        return Branch(statement, get_context(command, context))
    else:
        return get_context(command, context)
