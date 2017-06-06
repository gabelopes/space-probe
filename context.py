# pylint: disable=missing-docstring

class Context:
    def __init__(self, text):
        self.text = text
        self.source = text
        self.contexts = []

    def has_sub_contexts(self):
        return len(self.contexts) > 0

    def create_contexts(self):
        self.text = self.__create_contexts(self.text)
        self.__create_sub_contexts()

    def __create_contexts(self, text, start=0):
        parentheses_stack = []
        replaced_text = text

        for i, char in enumerate(text[start:]):
            index = i + start
            if char == "(":
                parentheses_stack.append(index)
            elif char == ")":
                start_index = parentheses_stack.pop()

                if not parentheses_stack:
                    (replaced_text, offset_index) = self.__create_context(text, start_index, index)
                    replaced_text = self.__create_contexts(replaced_text, start=offset_index + 1)
                    break

        return replaced_text

    def __create_context(self, text, start, end):
        context_identifier = len(self.contexts)
        context_text = text[start + 1:end]
        placeholder = f"[{context_identifier}]"
        replaced_text = self.__replace(text, placeholder, start, end)

        self.contexts.append(Context(context_text))

        return (replaced_text, end - (len(context_text) + 2) + len(placeholder))

    def __replace(self, text, placeholder, start, end):
        return text[0 : start] + placeholder + text[end + 1:]

    def __create_sub_contexts(self):
        for context in self.contexts:
            context.create_contexts()

    def __str__(self):
        text, size = self.text, len(self)
        return f"<{text}> [{size}]"

    def __sizeof__(self):
        return len(self.contexts)

    def __iter__(self):
        for context in self.contexts:
            yield context