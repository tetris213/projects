import pygame


def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((1280, 720))
    FPS = pygame.time.Clock()
    pygame.display.set_caption("Algo Demo")
    running = True

    DISPLAYSURF.fill("black")
    user_text = ""
    list = LinkedList(5)
    list.draw(DISPLAYSURF)
    input = list.get_input_field()
    while running:
        for event in pygame.event.get():
            # need to handle unselecting input FIELD
            # need to handle validation of input ONLY NUMBERS
            # better deleting
            # and clicking to other buttons
            # transfer value to first array
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input.collidepoint(event.pos):
                    list.toggle_active(DISPLAYSURF)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:1]

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                else:
                    user_text += event.unicode

            list.drawText(input, DISPLAYSURF, user_text)

            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        FPS.tick(60)
    pygame.quit()


class LinkedList(pygame.sprite.Sprite):
    array = []
    color = "white"
    color_selected = "purple"
    window_info = None
    lr_position = -175
    heigh_position = None
    push_btn = None
    pop_btn = None
    clear_btn = None
    input_field = None
    input_field_active = False
    font = None

    def __init__(self, number_of_cells):
        super().__init__()
        self.window_info = pygame.display.get_window_size()
        self.height_position = 4 * self.window_info[1] / 5
        self.font = pygame.font.Font("freesansbold.ttf", 12)
        self.init_array(number_of_cells)
        self.init_controls()

    def get_input_field(self):
        return self.input_field

    def toggle_active(self, DISPLAYSURF):
        if self.input_field is not None:
            self.input_field_active = not self.input_field_active
            pygame.draw.rect(DISPLAYSURF, self.color_selected, self.input_field)

        else:
            raise ValueError("INPUT FIELD IS NOT INITIALIZED")

    def init_array(self, number_of_cells):
        x = self.lr_position
        y = self.height_position
        for i in range(number_of_cells):
            x += self.window_info[0] / number_of_cells
            cell = pygame.Rect((x, y), (100, 100))
            self.array.append(cell)

    def init_controls(self):
        self.push_btn = pygame.Rect((1105, 100), (100, 50))
        self.pop_btn = pygame.Rect((905, 100), (100, 50))
        self.clear_btn = pygame.Rect((705, 100), (100, 50))
        self.input_field = pygame.Rect((505, 100), (100, 50))

    def drawText(self, rect, DISPLAYSURF, text):
        text_object = self.font.render(text, True, (0, 0, 0), (255, 255, 255))
        centered_text = text_object.get_rect(center=rect.center)
        pygame.Surface.blit(DISPLAYSURF, text_object, centered_text)

    def handleInput(self):
        pass

    def draw(self, DISPLAYSURF):
        for cell in self.array:
            pygame.draw.rect(DISPLAYSURF, self.color, cell)
        pygame.draw.rect(DISPLAYSURF, self.color, self.push_btn)
        pygame.draw.rect(DISPLAYSURF, self.color, self.pop_btn)
        pygame.draw.rect(DISPLAYSURF, self.color, self.clear_btn)
        pygame.draw.rect(DISPLAYSURF, "grey", self.input_field)
        self.drawText(self.push_btn, DISPLAYSURF, "PUSH")
        self.drawText(self.input_field, DISPLAYSURF, "INPUT")
        self.drawText(self.pop_btn, DISPLAYSURF, "POP")
        self.drawText(self.clear_btn, DISPLAYSURF, "CLEAR")


if __name__ == "__main__":
    main()
