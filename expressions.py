# pylint: disable=missing-docstring,line-too-long

import re

CHECKING = {}

CHECKING["basic"] = re.compile(r"^\s*(FORWARD|BACK|LEFT|RIGHT)\s+\d+\s*$")
CHECKING["statement"] = re.compile(r"^\s*(\[\d+\]|(FORWARD|BACK|LEFT|RIGHT)\s+\d+)\s+(THEN|AFTER)\s+(\[\d+\]|(FORWARD|BACK|LEFT|RIGHT)\s+\d+)\s*$")
CHECKING["compound"] = re.compile(r"^\s*(\[\d+\]|(FORWARD|BACK|LEFT|RIGHT)\s+\d+)\s+(THEN|AFTER)\s+(\[\d+\]|(FORWARD|BACK|LEFT|RIGHT)\s+\d+){2,}\s+(\[\d+\]|(FORWARD|BACK|LEFT|RIGHT)\s+\d+)\s+(THEN|AFTER)\s+(\[\d+\]|(FORWARD|BACK|LEFT|RIGHT)\s+\d+)\s*$")


MATCHING = {}

MATCHING["context"] = re.compile(r"\[(\d+)\]")
MATCHING["basic"] = re.compile(r"(FORWARD|BACK|LEFT|RIGHT)\s+(\d+)")
MATCHING["command"] = re.compile(r"(?:\[(\d+)\]|(FORWARD|BACK|LEFT|RIGHT)\s+(\d+))")
MATCHING["statement"] = re.compile(r"(\[\d+\]|(?:FORWARD|BACK|LEFT|RIGHT)\s+\d+)\s+(THEN|AFTER)\s+(\[\d+\]|(?:FORWARD|BACK|LEFT|RIGHT)\s+\d+)")
MATCHING["compound"] = re.compile(r"(?:(\[\d+\]|(?:FORWARD|BACK|LEFT|RIGHT)\s+\d+)\s+(THEN|AFTER)\s+(\[\d+\]|(?:FORWARD|BACK|LEFT|RIGHT)\s+\d+))\s+((?:\[\d+\]|(FORWARD|BACK|LEFT|RIGHT)\s+\d+))")
MATCHING["useless_parentheses"] = re.compile(r"\(\s*((?:FORWARD|BACK|LEFT|RIGHT)\s+\d+)\s*\)")
