# pylint: disable=missing-docstring,too-few-public-methods

class Tree:
    def __init__(self, root=None):
        self.root = root


class Branch:
    def __init__(self, element, left=None, right=None, malformed=False):
        self.element = element
        self.left_branch = left
        self.right_branch = right
        self.malformed = malformed

    def is_leaf(self):
        return not self.has_left_branch() and not self.has_right_branch()

    def has_left_branch(self):
        return self.left_branch is not None

    def has_right_branch(self):
        return self.right_branch is not None

    def __str__(self):
        return str(self.context)
