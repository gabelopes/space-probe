# pylint: disable=missing-docstring,line-too-long

from expressions import CHECKING

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
