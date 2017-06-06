# pylint: disable=missing-docstring,invalid-name

import sys
import translator
from space_probe import SpaceProbe

# TODO compound contexts

def print_path(path):
    for x, y in path:
        print(f"Moved to ({x}, {y})")

if len(sys.argv) >= 2:
    source_file = sys.argv[1]
    source = open(source_file).read()
    commands = translator.translate(source)

    space_probe = SpaceProbe()
    path_traveled = space_probe.process_all(commands)

    print_path(path_traveled)
