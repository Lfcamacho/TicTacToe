import pygame
import time
import random
import functions_tictactoe as tic
pygame.font.init()

WIDTH, HEIGHT = 300, 300
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

WIN.fill((255,255,255))

PLAYER_FONT = pygame.font.SysFont("comicsans", 150)
MAIN_FONT = pygame.font.SysFont("comicsans", 50)


class Game():

    def __init__(self):

        self.board = [['', '', ''],['', '', ''],['', '', '']]


        randnum = random.randint(0,1)
        self.players = ('x', 'o')
        self.turn = self.players[randnum]
        self.color = ((0,0,255),(255,0,0))
        self.colorturn = self.color[randnum]
        self.end = False


        for i in range(1,3):

            coord = round(WIDTH * i / 3)
            pygame.draw.line(WIN, (0,0,0),(coord,0), (coord,HEIGHT), 3)
            pygame.draw.line(WIN, (0,0,0),(0,coord), (WIDTH,coord), 3)  

    def draw(self, pos):

        label = PLAYER_FONT.render(self.turn, 1, self.colorturn)
        position = self.get_position(pos, label)

        if tic.validate(self.board, self.row, self.col):

            WIN.blit(label, (position[0], position[1]))
            self.board[self.row][self.col] = self.turn

            if tic.has_won(self.board) or tic.is_full(self.board):
                self.finish()

            else:
                self.change_turn()

    def finish(self):

        self.end = True

        if tic.has_won(self.board):
            finish_text = f"{self.turn}'s have won"
        else:
            finish_text = "It's a tie"

        white = pygame.Surface((WIDTH,HEIGHT))
        white.set_alpha(220)
        WIN.blit(white, (0,0))

        finish_label = MAIN_FONT.render(finish_text, 1, (255,255,255))
        x = round(WIDTH / 2 - finish_label.get_width() / 2)
        y = round(HEIGHT / 2 - finish_label.get_height() / 2)
        WIN.blit(finish_label, (x,y))


    def get_position(self, pos, label):

        w = label.get_width() / 2
        h = label.get_height() / 2

        if pos[0] < WIDTH / 3:
            xpos = WIDTH / 6 - w
            self.col = 0

        elif pos[0] > WIDTH * 2 / 3:
            xpos = WIDTH *5 / 6 - w
            self.col = 2

        else:
            xpos = HEIGHT / 2 - w
            self.col = 1

        if pos[1] < HEIGHT / 3:
            ypos = HEIGHT / 6 - h
            self.row = 0

        elif pos[1] > HEIGHT * 2 / 3:
            ypos = HEIGHT *5 / 6 - h
            self.row = 2

        else:
            ypos = HEIGHT / 2 - h
            self.row = 1

        return [round(xpos), round(ypos)]

    def change_turn(self):

        if self.turn == 'x':
            self.turn = self.players[1]
            self.colorturn = self.color[1]
        else:
            self.turn = self.players[0]
            self.colorturn = self.color[0]
            


def main():

    WIN.fill((255,255,255))
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    tictactoe = Game()


    while run:
        clock.tick(FPS)
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                tictactoe.draw(event.pos)
            if tictactoe.end and event.type == pygame.MOUSEBUTTONDOWN:
                run = False

def menu():

    run = True
    FPS = 60
    clock = pygame.time.Clock()

    title = "TIC TAC TOE"
    title_label = MAIN_FONT.render(title, 1, (0,0,0))
    x = round(WIDTH / 2 - title_label.get_width() / 2)
    y = 30
    WIN.blit(title_label, (x,y))

    while run:
        clock.tick(FPS)
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()

        
menu()

