class HudElement():
    def __init__(self, screen, font, text, count, position):
        self.screen = screen
        self.font = font
        self.text = text
        self.count = count
        self.position = position


    def draw(self):
        display_text = self.font.render(f"{self.text}: {self.count}", True, "White")
        #Display the text at coordinates
        self.screen.blit(display_text, self.position)
