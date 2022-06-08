import pygame
import time
from pygame import mixer
pygame.init()
mixer.init()
import csv
import random
file = open('Questions_ltr_quiz.csv')
type(file)

mixer.music.load('Main_Theme.mp3')
print("The music started playing")
mixer.music.play()
#window

WIDTH,HEIGHT = 890,500

FPS = 1
fpsClock = pygame.time.Clock()


#question height 
QUEST_W,QUEST_H = WIDTH//2,50

ANSW_1_W,ANSW_1_H  = WIDTH // 2 , 130
ANSW_2_W,ANSW_2_H = WIDTH // 2 , 280
ANSW_3_W,ANSW_3_H = WIDTH //2 , 430

#sets up a window
WIN = pygame.display.set_mode((WIDTH , HEIGHT))
#Names Window
pygame.display.set_caption("LOTR QUIZ")

score = 0


# RGB COLORS
RED = (233,40,40)
WHITE = (255,255,255)
BLACK = (0,20,20)
AQUA_GREEN = (21,183,140)
LIGHT_RED_01 = (255,102,102)
LIGHT_RED_02 = (240,105,105)
KAHOOT_ORANGE = (255,255,255)
GREEN = (0,204,0)

GREY = (160,160,160)
#Images 

background = pygame.image.load('background_1.png')

#Text & Fonts
font_titles = pygame.font.Font('BRIDGE.ttf',60)
font_sub = pygame.font.Font('BRIDGE.ttf',45)
font_little = pygame.font.Font('BRIDGE.ttf',30)

#TITLE SCREEN ----------------------------------------------------------------------------
title_text = font_titles.render('Lord of the Rings',True,BLACK,LIGHT_RED_01)
TitletextRect = title_text.get_rect()
TitletextRect.center = (WIDTH//2,HEIGHT//2-100)

sub_text = font_sub.render('QUIZ',True,BLACK,LIGHT_RED_02)
sub_text_rect = sub_text.get_rect()
sub_text_rect.center = (WIDTH//2,HEIGHT//2-35)

play_text = font_little.render('Begin?',True,BLACK,WHITE)
play_text_rect = play_text.get_rect()
play_text_rect.center = (WIDTH//2,HEIGHT//2+20)

play_text_light = font_little.render('Begin?',True,BLACK,AQUA_GREEN)
play_text_rect_light = play_text_light.get_rect()
play_text_rect_light.center = (WIDTH//2,HEIGHT//2+20)

title_screen = True

#Class for making textx------------------------------------------------------------------------

class text():
    def __init__(self,text,answer_01,answer_02,answer_03,correct_answer):
        self.text = text
        self.answer_01 = answer_01
        self.answer_02 = answer_02
        self.answer_03 = answer_03
        self.correct_answer = correct_answer






    

#question buttons that you can click.
button_01 = pygame.Rect(50,80,790,100)       
button_02 = pygame.Rect(50,230,790,100)
button_03 = pygame.Rect(50,380,790,100)



question_num = 0


begin = False
finnshed = False



#-------------------------csv----------------------------------------



#this system is much shorter then the older version 
file = open('Questions_ltr_quiz.csv')
type(file)

def read_line(file_path, line_num):
    with open(file_path, "r") as file:

        reader = csv.reader(file)

        for _ in range(line_num-1):
            next(reader)
        return next(reader)


#This bit imports ten random numbers
random_list = random.sample(range(1,21),10)
print(random_list)


#This bit gets those specific lines and adds them to a class.
# So it opens the quiz file and prints the questions that match up to the csv file.


    
question = read_line('Questions_ltr_quiz.csv',random_list[0])


#--------------------------- questions ------------------------------



current_question = text(question[0],question[1],question[2],question[3],question[4])




running = True
while running:
    answered  = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #THIS CHECKS WHERE THE MOUSE CICKED AND IF THE MOUSE CLICKED A BUTTON
            if WIDTH // 2 - 50 <= mouse_position[0] <= WIDTH//2+50 and HEIGHT//2 + 5 <= mouse_position[1] <= HEIGHT // 2 + 45 and title_screen == True:
               
                begin     = True
                pygame.time.delay(50)
                
                
                
                
            
            if 50 <= mouse_position[0] <= 840 and 80 <= mouse_position[1] <= 180 and title_screen == False:
                response = 1
                print("You picked option 1")
                if current_question.correct_answer == "1":
                    score += 1
                    print(score)
                answered = True


            if 50 <= mouse_position[0] <= 840 and 230 <= mouse_position[1] <= 330 and title_screen == False:
                response = 2
                print("You picked option 2")
                if current_question.correct_answer == "2":
                    score += 1
                    print(score)
                answered = True


            if 50 <= mouse_position[0] <= 840 and 380 <= mouse_position[1] <= 480 and title_screen == False:
                response = 3
                print("You picked option 3")
                if current_question.correct_answer == "3":
                    score += 1
                    print(score)
                answered = True
             
    if begin == True:
        title_screen = False

    question_draw = font_little.render(current_question.text,True,BLACK,WHITE)
    question_rect = question_draw.get_rect()
    question_rect.center = (QUEST_W,QUEST_H)

    answer_1 = font_little.render(current_question.answer_01,True,BLACK,WHITE)
    answer_1_rect = answer_1.get_rect()
    answer_1_rect.center = (ANSW_1_W,ANSW_1_H)

    answer_2 = font_little.render(current_question.answer_02,True,BLACK,WHITE)
    answer_2_rect = answer_2.get_rect()
    answer_2_rect.center = (ANSW_2_W,ANSW_2_H)

    answer_3 = font_little.render(current_question.answer_03,True,BLACK,WHITE)
    answer_3_rect = answer_3.get_rect()
    answer_3_rect.center = (ANSW_3_W,ANSW_3_H)

    score_rend = font_titles.render("Score {} out of 10".format(score),True,BLACK,WHITE)
    score_rect = score_rend.get_rect()
    score_rect.center = (WIDTH//2,HEIGHT//2)

    # Gets the mices postion
    mouse_position = pygame.mouse.get_pos()

    WIN.blit(background,(0,0))

    # If Title Screen is active

    if title_screen == True:
        WIN.blit(title_text,TitletextRect)
        WIN.blit(sub_text,sub_text_rect)

        if WIDTH // 2 - 50 <= mouse_position[0] <= WIDTH//2+50 and HEIGHT//2 + 5 <= mouse_position[1] <= HEIGHT // 2 + 45:
            WIN.blit(play_text_light, play_text_rect_light)
            question_num == 1
        else:
            WIN.blit(play_text, play_text_rect)
            
                
        #Buttons that are on the tilte screen
    else:

        

        pygame.draw.rect(WIN,BLACK,button_01,2)

        pygame.draw.rect(WIN,GREY,button_02,2)

        pygame.draw.rect(WIN,KAHOOT_ORANGE,button_03,2)

       
            

        if 50 <= mouse_position[0] <= 840 and 80 <= mouse_position[1] <= 180:
            pygame.draw.rect(WIN,BLACK,button_01)

        if 50 <= mouse_position[0] <= 840 and 230 <= mouse_position[1] <= 330:
            pygame.draw.rect(WIN,GREY,button_02)

        if 50 <= mouse_position[0] <= 840 and 380 <= mouse_position[1] <= 480:
            pygame.draw.rect(WIN,KAHOOT_ORANGE,button_03)
        
        if answered == True:
            if question_num == 0:
                question = read_line('Questions_ltr_quiz.csv',random_list[1])
                current_question = text(question[0],question[1],question[2],question[3],question[4])
            elif question_num == 1:
                question = read_line('Questions_ltr_quiz.csv',random_list[2])
                current_question = text(question[0],question[1],question[2],question[3],question[4])
            elif question_num == 2:
                question = read_line('Questions_ltr_quiz.csv',random_list[3])
                current_question = text(question[0],question[1],question[2],question[3],question[4])
            elif question_num == 3:
                question = read_line('Questions_ltr_quiz.csv',random_list[4])
                current_question = text(question[0],question[1],question[2],question[3],question[4])
            elif question_num == 4:
                question = read_line('Questions_ltr_quiz.csv',random_list[5])
                current_question = text(question[0],question[1],question[2],question[3],question[4])
            
            elif question_num == 5:
                question = read_line('Questions_ltr_quiz.csv',random_list[6])
                current_question = text(question[0],question[1],question[2],question[3],question[4])
            
            elif question_num == 6:
                question = read_line('Questions_ltr_quiz.csv',random_list[7])
                current_question = text(question[0],question[1],question[2],question[3],question[4])
            
            elif question_num == 7:
                question = read_line('Questions_ltr_quiz.csv',random_list[8])
                current_question = text(question[0],question[1],question[2],question[3],question[4])
            elif question_num == 8:
                question = read_line('Questions_ltr_quiz.csv',random_list[9])
                current_question = text(question[0],question[1],question[2],question[3],question[4])
            elif question_num == 9:    
                
                if answered == True:
                    WIN.blit(score_rend,score_rect)
                    finnshed = True

            
            question_num += 1
        
        if finnshed != True: 
            WIN.blit(question_draw,question_rect)
            WIN.blit(answer_1,answer_1_rect)
            WIN.blit(answer_2,answer_2_rect)
            WIN.blit(answer_3,answer_3_rect)

        

        



    

    #Updates The display
    pygame.display.update()


    fpsClock.tick(15)

    if finnshed == True:
        time.sleep(3)
        running = False