class TextEditor:
    def __init__(self):
        self.text = ""
        self.cursor = 0

    def addText(self, text: str) -> None:
        prev_text = self.text
        cursor = self.cursor

        self.text = f"{prev_text[:cursor]}{text}{prev_text[cursor:]}"
        self.cursor = cursor + len(text)

    def deleteText(self, k: int) -> int:
        prev_text = self.text
        prev_cursor = self.cursor

        new_cursor = max(0, self.cursor - k)
        self.text = f"{prev_text[:new_cursor]}{prev_text[prev_cursor:]}"
        self.cursor = new_cursor

        return min(k, prev_cursor)

    def cursorLeft(self, k: int) -> str:
        prev_cursor = self.cursor
        new_cursor = max(0, self.cursor - k)
        self.cursor = new_cursor

        left_bound = max(0, new_cursor - 10)
        return self.text[left_bound:new_cursor]

    def cursorRight(self, k: int) -> str:
        prev_cursor = self.cursor
        new_cursor = min(len(self.text), self.cursor + k)
        self.cursor = new_cursor

        left_bound = max(0, new_cursor - 10)
        return self.text[left_bound:new_cursor]


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
