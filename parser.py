# pylint: disable=missing-docstring,line-too-long

from expressions import MATCHING, CHECKING
from context import Context

def parse_statement(context):
    match = MATCHING["statement"].match(context.text)
    command = match.group(2)
    left = __get_context(match.group(1), context)
    right = __get_context(match.group(3), context)

    return (command, left, right)

def __get_context(text, context):
    if CHECKING["basic"].match(text):
        return Context(text)

    index = int(MATCHING["context"].match(text).group(1))
    return context.contexts[index]

def parse_compound(context):
    match = MATCHING["compound"].search(context.text)

