# pylint: disable=missing-docstring,line-too-long

import re

CHECKING = {
    "basic": re.compile(r"^\s*(FORWARD|BACK|LEFT|RIGHT)\s+\d+\s*$"),
    "statement": re.compile(r"^\s*(\[\d+\]|(FORWARD|BACK|LEFT|RIGHT)\s+\d+)\s+(THEN|AFTER)\s+(\[\d+\]|(FORWARD|BACK|LEFT|RIGHT)\s+\d+)\s*$"),
    "compound": re.compile(r"^\s*(\[\d+\]|(FORWARD|BACK|LEFT|RIGHT)\s+\d+)(\s+(THEN|AFTER)\s+(\[\d+\]|(FORWARD|BACK|LEFT|RIGHT)\s+\d+)){2,}\s*$")
}

MATCHING = {
    "context": re.compile(r"\[(\d+)\]"),
    "basic": re.compile(r"(FORWARD|BACK|LEFT|RIGHT)\s+(\d+)"),
    "command": re.compile(r"(?:\[(\d+)\]|(FORWARD|BACK|LEFT|RIGHT)\s+(\d+))"),
    "statement": re.compile(r"(\[\d+\]|(?:FORWARD|BACK|LEFT|RIGHT)\s+\d+)\s+(THEN|AFTER)\s+(\[\d+\]|(?:FORWARD|BACK|LEFT|RIGHT)\s+\d+)"),
    "compound": re.compile(r"(\[\d+\]|(?:FORWARD|BACK|LEFT|RIGHT)\s+\d+)(?:\s+(THEN|AFTER))?"),
    "useless_parentheses": re.compile(r"\(\s*((?:FORWARD|BACK|LEFT|RIGHT)\s+\d+)\s*\)")
}