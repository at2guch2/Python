# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 14:25:57 2020

pygame GUI for Sudoku

@author: Jun
"""
import pygame  #, sys
# from pygame.locals import *
from Sudoku_Generator import maker # , print_sudoku
pygame.font.init()
puzzle, solu = maker()
    
font = pygame.font.SysFont('ComicSansMs', 45)

# Window Size - Width has to be a multiple of 9
width = 540
height = 540

# Extension
ex = 100

# Colors
color = {'bl':[0,0,0], 'wh':[255,255,255], 'gr': [200,200,200], 're':[255,0,0],
         'input':[0,128,255], 'solu':[0,204,102], 'hover':[204,255,229]}

# Grid and numbers
square = width // 3
cell = square // 3

# Draws puzzle numbers 
def draw_num(draw_num_puzzle, draw_num_solu, solu_on, draw_num_display):
    x = cell // 2
    y = cell // 2
    for i in range(len(draw_num_puzzle)):
        for j in range(len(draw_num_puzzle[i])):
            # inputs are unique in that they're strings which can be used to separate
            # them from the original numbers
            num = draw_num_puzzle[i][j]
            if type(num) == str and num != ' ' and solu_on == True:
                text = font.render(str(draw_num_solu[i][j]), True, color['input'])
                draw_num_display.blit(text, (x - 12, y - 33))
            elif type(num) == str and num != ' ':
                text = font.render(str(num), True, color['input'])
                draw_num_display.blit(text, (x - 12, y - 33))
            elif type(num) == int and num != ' ':      
                text = font.render(str(num), True, color['bl'])
                draw_num_display.blit(text, (x - 12, y - 33))
            # fills in empty cells with red solution numbers
            elif num == ' ' and solu_on == True:
                text = font.render(str(draw_num_solu[i][j]), True, color['re'])
                draw_num_display.blit(text, (x - 12, y - 33))
            
            x += cell
        x = cell // 2
        y += cell 
              
# Draws the grid
def draw_grid():
    global display
    # Square lines
    for i in range(0, width, square): # vertical
        if i != 0:
            pygame.draw.line(display, color['bl'], (i, 0), (i, height), 4)
    for j in range(0, height, square): # horizontal
        if j != 0:
            pygame.draw.line(display, color['bl'], (0, j), (width, j), 4)
    
    # Cell Lines
    for i in range(0, width, cell): # vertical
        if i % square != 0:
            pygame.draw.line(display, color['bl'], (i, 0), (i, height), 1)
    for j in range(0, height, cell): # horizontal
        if j % square != 0:
            pygame.draw.line(display, color['bl'], (0, j), (width, j), 1)
    
    # Bottom Border
    pygame.draw.line(display, color['bl'], (0, height), (width, height), 4)
    
# Check solution button
def check_solu():
    global display
    x_solu = width // 2 - cell
    y_solu = (height+ex)-77
    
    x_new = width // 6 - cell
    y_new = y_solu
    # draw button
    pygame.draw.rect(display, color['bl'], (x_solu, y_solu, cell * 2, cell), 3)
    text = font.render('Solve', True, color['re'])
    display.blit(text, (x_solu + 2, y_solu - 6))
    
    # New puzzle button
    pygame.draw.rect(display, color['bl'], (x_new, y_new, cell * 2, cell), 3)
    text = font.render('New', True, color['input'])
    display.blit(text, (x_new + 15, y_new - 6))
    
# Returns mouse position
def click(click_pos):
    if click_pos[0] < width and click_pos[1] < height:
        col = click_pos[0] // cell
        row = click_pos[1] // cell
        return int(row),int(col)
    else:
        return None
    
def highlight(highlight_pos, highlight_display):
    # Cells get highlighted red once selected
    try:
        x, y = highlight_pos
        pygame.draw.rect(highlight_display, color['re'], (y * cell, x * cell, cell , cell), 2)
    except TypeError:
        print('Outside grid')
        
# Fills in number inputs
def fill_val(fill_val_display, val, fill_val_pos):
    x, y = click(fill_val_pos)
    text = font.render(str(val), 1, color['bl'])
    fill_val_display.blit(text, (x, y))

# Redraws the board whenever a cell is highlighted to get rid of old highlights
def redrawer(redrawer_puzzle, redrawer_solu, solu_on):
    global display
    display.fill(color['wh'])
    draw_grid()
    draw_num(redrawer_puzzle, redrawer_solu, solu_on, display)
    check_solu()
    
# Window + Title + Main Loop
def main():
    global display, pos
    main_puzzle, main_solu = maker()

    pygame.init()
    display = pygame.display.set_mode((width, height+ex))

    pygame.display.set_caption("Sudoku")
    key = None
    run = True
    select = False
    solu_on = False
    redrawer(main_puzzle, main_solu, solu_on)
    
    # Main Loop
    while run:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_KP_1:
                    key = 1
                if event.key == pygame.K_2 or event.key == pygame.K_KP_2:
                    key = 2
                if event.key == pygame.K_3 or event.key == pygame.K_KP_3:
                    key = 3
                if event.key == pygame.K_4 or event.key == pygame.K_KP_4:
                    key = 4
                if event.key == pygame.K_5 or event.key == pygame.K_KP_5:
                    key = 5
                if event.key == pygame.K_6 or event.key == pygame.K_KP_6:
                    key = 6
                if event.key == pygame.K_7 or event.key == pygame.K_KP_7:
                    key = 7
                if event.key == pygame.K_8 or event.key == pygame.K_KP_8:
                    key = 8
                if event.key == pygame.K_9 or event.key == pygame.K_KP_9:
                    key = 9
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                select = True
                # Grid Selection
                if pos[0] < width and pos[1] < height:
                    redrawer(main_puzzle, main_solu, solu_on)
                    highlight(click(pos), display)
                    key = None 
                # Solve button selection
                if width // 2 - cell + cell*2 > pos[0] > width // 2 - cell and (height+ex)-77 + cell > pos[1] > (height+ex)-77:
                    solu_on = True
                    redrawer(main_puzzle, main_solu, solu_on)
                # New Game button
                if width // 6 - cell + cell*2 > pos[0] > width // 6 - cell and (height+ex)-77 + cell > pos[1] > (height+ex)-77:
                    main_puzzle, main_solu = maker()
                    solu_on = False
                    redrawer(main_puzzle, main_solu, solu_on)
#                    print_sudoku(solu)
                    
                    
        # Takes input and updates puzzle with it so it won't get erased
        # Input numbers are unique in that they're strings. This is so drawNum
        # colors them blue instead of black
        if run and select == True and key is not None and pos[0] < width and pos[1] < height:
            row, col = click(pos)
            # Only draws numbers if you click on an empty cell
            if main_puzzle[row][col] == ' ' or type(main_puzzle[row][col]) == str:
                main_puzzle[row][col] = str(key)
                # If you're correct, the solution cell also changes to a str
                # This for an easier comparison later when I add a check solution button
                if main_solu[row][col] == key:
                    main_solu[row][col] = str(key)
                redrawer(main_puzzle, main_solu, solu_on)
                text = font.render(str(key), True, color['input'])
                display.blit(text, (col*cell+18, row*cell-3))

        if run:
            pygame.display.update()  # Refresh the screen to show the fill





if __name__ == '__main__':
    global display
    global pos
    main()
    
