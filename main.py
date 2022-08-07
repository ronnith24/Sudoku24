"""
author: Ronnith Nandy
"""

from sudokuSolver import Sudoku
import pygame
import time

pygame.init()

c = 1

class SudokuBoard(object):
    def __init__(self, screen):
        self.sudoku = Sudoku()
        self.cells = []
        self.screen = screen
        self.wrong = 0
        self.won = False
        self.lost = False
        for i in range(9):
            self.cells.append([])
            for j in range(9):
                self.cells[i].append(Cell(screen, self.sudoku.grid[i, j], (i * 60 + (i // 3) * 4 + 1), (j * 60 + (j // 3) * 4 + 1), i, j))
    
    def state(self):
        if self.won:
            return 1
        elif self.lost:
            return -1
        else:
            return 0
    
    def update(self):
        """
        Input: None
        Returns: Updates the entire gui of the board and handles interaction with user
        """
        if self.sudoku.solved:
            self.won = True
            return
        if self.wrong > 3:
            self.lost = True
            return
        for i in range(9):
            for j in range(9):
                self.wrong += self.cells[i][j].manage(self.sudoku)
    
    def hint(self):
        (i, j, number) = self.sudoku.hint()
        self.cells[i][j].value = number
        self.cells[i][j].incorrect = False
        self.cells[i][j].correct = True
        self.cells[i][j].selected = False
        self.cells[i][j].draw()

class Cell(object):
    def __init__(self, screen, value, x, y, i, j):
        self.value = value
        self.rect = pygame.Rect((x + 1) * c, (y + 1) * c, 58 * c, 58 * c) #dimensions for the rectangle
        self.x = x
        self.y = y
        self.i = i
        self.j = j
        self.selected = False
        self.screen = screen
        if value != 0:
            self.correct = True
        else:
            self.correct = False
        self.incorrect = False
    
    def manage(self, sudoku):
        """
        Input: The Sudoku object which holds information of current sudoku
        Returns: Manages all interaction of user with this cell and returns 1 if user enters wrong number
        """
        if self.correct:
            self.draw()
            return 0
        
        wronged = False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                self.selected = self.rect.collidepoint(mouse)
                if not self.selected:
                    self.incorrect = False
            elif event.type == pygame.KEYDOWN:
                if self.selected:
                    number = 0
                    if event.key == pygame.K_1:
                        number = 1

                    if event.key == pygame.K_2:
                        number = 2

                    if event.key == pygame.K_3:
                        number = 3

                    if event.key == pygame.K_4:
                        number = 4

                    if event.key == pygame.K_5:
                        number = 5

                    if event.key == pygame.K_6:
                        number = 6

                    if event.key == pygame.K_7:
                        number = 7

                    if event.key == pygame.K_8:
                        number = 8

                    if event.key == pygame.K_9:
                        number = 9
                    
                    if number == 0:
                        continue
                    
                    if sudoku.update(self.i, self.j, number):
                        self.value = number
                        self.correct = True
                        self.selected = False
                        self.incorrect = False
                    else:
                        self.value = number
                        self.incorrect = True
                        wronged = True
        
        self.draw()
        return int(wronged)
                        
                        
    def draw(self):
        """
        Input: None
        Returns: Updates the tile
        """
        rect = pygame.Surface((60 * c, 60 * c))
        if self.correct or not self.incorrect:
            if (self.i // 3 + self.j // 3) % 2 == 0:
                rect.fill((51, 153, 255))
            else:
                rect.fill((255, 255, 255))
        if self.incorrect:
            rect.fill((255, 0, 0))
        self.screen.blit(rect, (self.x * c, self.y * c))
        thickness = 1 * c
        if self.selected:
            thickness = 4 * c
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect, thickness)
        if self.value != 0 and (self.correct or self.incorrect):
            font = pygame.font.SysFont('lato', 45 * c)
            text = font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text, ((self.x + 21) * c, (self.y + 16) * c))


SCENES = [0, 1, 2, 3]
scene = 0

screen = pygame.display.set_mode((551 * c, 598 * c))
pygame.display.set_caption("Sudoku24")
icon = pygame.image.load("./res/icon.png")
pygame.display.set_icon(icon)

screen.fill((0, 0, 0))
animate_welcome = True
hints_left = 0
state = 0

running = True
while running:
    events = pygame.event.get()
    # controls the functioning of home screen
    if scene == 0:
        font = pygame.font.SysFont('lato', 90 * c)
        welcome = "Welcome"
        if animate_welcome:
            for i in range(len(welcome)):
                text = font.render(welcome[:i + 1], True, (51, 153, 255))
                screen.blit(text, (140 * c, 225 * c))
                pygame.display.flip()
                time.sleep(0.3)
            animate_welcome = False
        enter_button = pygame.image.load("./res/playbutton.png")
        enter_button = pygame.transform.scale(enter_button, (50 * c, 50 * c))
        screen.blit(enter_button, (240 * c, 400 * c))
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if mouse[0] >= 240 * c and mouse[0] <= 290 * c and mouse[1] >= 400 * c and mouse[1] <= 450 * c:
                    scene = 1
                    screen.fill((0, 0, 0))
    elif scene == 1:
        screen.fill((0, 0, 0))
        background = pygame.image.load("./res/welcome screen2.jpg")
        background = pygame.transform.scale(background, (350 * c, 350 * c))
        screen.blit(background, (100 * c, 100 * c))
        play_button = pygame.image.load("./res/playbutton.png")
        play_button = pygame.transform.scale(play_button, (50 * c, 50 * c))
        screen.blit(play_button, (450 * c, 500 * c))
        
        # checking if button is pressed
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if mouse[0] >= 450 * c and mouse[0] <= 500 * c and mouse[1] >= 500 * c and mouse[1] <= 550 * c:
                    scene = 2
                    hints_left = 3
                    screen.fill((0, 0, 0))
                    font = pygame.font.SysFont('lato', 90 * c)
                    text = font.render(str("Loading..."), True, (51, 153, 255))
                    screen.blit(text, (140 * c, 225 * c))
                    pygame.display.flip()
                    board = SudokuBoard(screen)
                    start_time = time.time()
    elif scene == 2:
        # controls the main sudoku screen
        screen.fill((0, 0, 0))
        board.update()
        elapsed = time.time() - start_time
        passed_time = "Time: " + time.strftime("%H:%M:%S", time.gmtime(elapsed))
        # Displaying hint options
        hint_icon = pygame.image.load("./res/hint.png")
        hint_icon = pygame.transform.scale(hint_icon, (25 * c, 25 * c))
        screen.blit(hint_icon, (20 * c, 560 * c))
        mouse = pygame.mouse.get_pos()
        if mouse[0] >= 20 * c and mouse[0] <= 45 * c and mouse[1] >= 560 * c and mouse[1] <= 585 * c:
            font = pygame.font.SysFont('lato', 50 * c)
            text = font.render(str(hints_left), True, (255, 0, 0))
            screen.blit(text, (25 * c, 535 * c))
        # Displaying no. of chances left
        wrong_icon = pygame.image.load("./res/wrong.png")
        wrong_icon = pygame.transform.scale(wrong_icon, (25 * c, 25 * c))
        screen.blit(wrong_icon, (80 * c, 560 * c))
        if mouse[0] >= 80 * c and mouse[0] <= 105 * c and mouse[1] >= 560 * c and mouse[1] <= 585 * c:
            font = pygame.font.SysFont('lato', 50 * c)
            text = font.render(str(3 - board.wrong), True, (255, 0, 0))
            screen.blit(text, (85 * c, 535 * c))
        # Displaying time
        font = pygame.font.SysFont('lato', 25 * c)
        text = font.render(str(passed_time), True, (255, 255, 255))
        screen.blit(text, (415 * c, 565 * c))
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if mouse[0] >= 20 * c and mouse[0] <= 45 * c and mouse[1] >= 560 * c and mouse[1] <= 585 * c:
                    if hints_left > 0:
                        board.hint()
                        hints_left -= 1
        if board.state() != 0:
            scene = 3
            state = board.state()
    elif scene == 3: # the page seen by user when the user finishes the game
        screen.fill((0, 0, 0))
        if state == 1:
            font = pygame.font.SysFont('lato', 90 * c)
            text = font.render(str("You Win!"), True, (51, 153, 255))
            screen.blit(text, (150 * c, 225 * c))
        elif state == -1:
            font = pygame.font.SysFont('lato', 90 * c)
            text = font.render(str("You Lost!"), True, (255, 0, 0))
            screen.blit(text, (140 * c, 225 * c))
        main_menu = pygame.image.load("./res/Main menu.jpg")
        main_menu = pygame.transform.scale(main_menu, (100 * c, 100 * c))
        screen.blit(main_menu, (230 * c, 390 * c))
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if mouse[0] >= 230 * c and mouse[0] <= 330 * c and mouse[1] >= 390 * c and mouse[1] <= 490 * c:
                    scene = 1
                    screen.fill((0, 0, 0))
    
    pygame.display.flip()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
