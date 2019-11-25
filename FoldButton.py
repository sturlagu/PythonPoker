from Button import Button


class FoldButton(Button):
    IMG = "foldButton"
    BUTTON_VALUE = -1

    def __init__(self, pos):
        super().__init__(self.IMG, pos, self.BUTTON_VALUE)
