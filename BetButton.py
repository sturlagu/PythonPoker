from Button import Button


class BetButton(Button):
    IMG = "betButton"
    BUTTON_VALUE = 0

    def __init__(self, pos):
        super().__init__(self.IMG, pos, self.BUTTON_VALUE)

