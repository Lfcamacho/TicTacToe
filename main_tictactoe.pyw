import pygame
import time
import random
import textwrap
import functions_tictactoe as tic
pygame.font.init()

WIDTH, HEIGHT = 400, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

WIN.fill((255,255,255))

PLAYER_FONT = pygame.font.SysFont("comicsans", 200)
MAIN_FONT = pygame.font.SysFont("comicsans", 70)
DESCRIPTION_FONT = pygame.font.SysFont("comicsans", 25)
START_FONT = pygame.font.SysFont("comicsans", 30)


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
            pygame.draw.line(WIN, (0,0,0),(coord,0), (coord,HEIGHT), 5)
            pygame.draw.line(WIN, (0,0,0),(0,coord), (WIDTH,coord), 5)  


    def player(self, pos):

        row,col = self.get_boardposition(pos)

        if tic.valid(self.board, row, col):

            self.board[row][col] = self.turn
            self.draw(row,col)
            self.game_state()

    
    def game_state(self):

        if tic.has_won(self.board) or tic.is_full(self.board):
            self.finish()
        else:
            self.change_turn()


    def draw(self, row, col):

        label = PLAYER_FONT.render(self.turn, 1, self.colorturn)
        x,y = self.get_guiposition(row, col, label)
        WIN.blit(label, (x, y))


    def finish(self):

        self.end = True

        if tic.has_won(self.board):
            finish_text = f"{self.turn}'s won"
        else:
            finish_text = "It's a tie"

        white = pygame.Surface((WIDTH,HEIGHT))
        white.set_alpha(220)
        WIN.blit(white, (0,0))

        finish_label = MAIN_FONT.render(finish_text, 1, (255,255,255))
        x = round(WIDTH / 2 - finish_label.get_width() / 2)
        y = round(HEIGHT / 2 - finish_label.get_height() / 2)
        WIN.blit(finish_label, (x,y))

        replay = "(Press the mouse to play again)"
        replay_label = DESCRIPTION_FONT.render(replay, 1, (255,255,255))
        x = round(WIDTH / 2 - replay_label.get_width() / 2)
        y = 230
        WIN.blit(replay_label, (x,y))

        

    def get_guiposition(self, row, col, label):

        gap = WIDTH / 3
        x = col * gap + (gap - label.get_width()) / 2
        y = row * gap + (gap - label.get_height()) / 2

        return round(x), round(y) 


    def get_boardposition(self, pos):

        gap = WIDTH / 3
        col = int(pos[0] // gap)
        row = int(pos[1] // gap)
        return row, col 


    def change_turn(self):

        if self.turn == 'x':
            self.turn = self.players[1]
            self.colorturn = self.color[1]
        else:
            self.turn = self.players[0]
            self.colorturn = self.color[0]

    def computer_move(self):

        row,col = tic.computer(self.board)
        self.board[row][col] = self.turn
        self.draw(row,col)
        self.game_state()
            


def main():

    WIN.fill((255,255,255))
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    tictactoe = Game()


    while run:
        clock.tick(FPS)
        pygame.display.update()

        if tictactoe.end:
            run = False
        else:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    tictactoe.player(event.pos)

            if tictactoe.turn == 'x':
                tictactoe.computer_move()

def menu():

    run = True

    title = "TIC TAC TOE"
    title_label = MAIN_FONT.render(title, 1, (0,0,0))
    x = round(WIDTH / 2 - title_label.get_width() / 2)
    y = 40
    WIN.blit(title_label, (x,y))

    description = textwrap.wrap("Try to beat the computer in classic Tic Tac Toe. The game will randomly choose who starts playing. You are the o's, good luck!", 40)
    y = 100

    for word in description:

        description_label = DESCRIPTION_FONT.render(word, 1, (0,0,0))
        x = 30
        y = y + description_label.get_height()
        WIN.blit(description_label, (x,y))

    start = "Press the mouse to start..."
    start_label = START_FONT.render(start, 1, (0,0,0))
    x = round(WIDTH / 2 - start_label.get_width() / 2)
    y = 250
    WIN.blit(start_label, (x,y))


    while run:
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()

        
menu()

