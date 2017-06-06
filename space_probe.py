# pylint: disable=missing-docstring,invalid-name

class SpaceProbe:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def process_all(self, commands):
        path = []

        for command in commands:
            path.append(self.process(*command))

        return path

    def process(self, command, offset):
        if command == "FORWARD":
            self.y += offset
        elif command == "BACK":
            self.y -= offset
        elif command == "RIGHT":
            self.x += offset
        elif command == "LEFT":
            self.x -= offset
        else:
            raise "Unsupported command"

        return self.get_position()

    def get_position(self):
        return (self.x, self.y)

    def __str__(self):
        (x, y) = self.get_position()
        return f"({x}, {y})"
