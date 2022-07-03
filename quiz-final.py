#----------- This is the Import Section, Where all 
# librarys including pygame, are installed -------
import pygame
import time
from pygame import mixer
import csv
import random

#-------------------------------------------------


# These two lines of code initilize the features from the librays
# This means that the cde is now activley looking for syntax from these liabrarys

# Pygame for the gameplay

pygame.init()

# Mixer for the music
mixer.init()

#-------------------------------------------------

#---------- VARIABLES ----------------------------


# These are permanent values that stay the same throughout 
# the entire code. It just saves me from having to rember them and hard code them in.

# Width and height of the game windowin pixel size
WIDTH,HEIGHT = 890,500

# These are the heights of the buttons in the game.
QUEST_W,QUEST_H = WIDTH//2,50

# These are the positions of the buttons on the screen
ANSW_1_W,ANSW_1_H  = WIDTH // 2 , 130
ANSW_2_W,ANSW_2_H = WIDTH // 2 , 280
ANSW_3_W,ANSW_3_H = WIDTH //2 , 430

# These are Lists that have the RGB Code in them.
RED = (233,40,40)
WHITE = (255,255,255)
BLACK = (0,20,20)
AQUA_GREEN = (21,183,140)
LIGHT_RED_01 = (255,102,102)
LIGHT_RED_02 = (240,105,105)
KAHOOT_ORANGE = (255,255,255)
GREEN = (0,204,0)
GREY = (160,160,160)
BLUE = (0,142,204)



#----------------- Class ------------------------


# This class is used to store all the details about the questions in
# For easy access.

class text():
    def __init__(self,text,answer_01,answer_02,answer_03,correct_answer):
        self.text = text
        self.answer_01 = answer_01
        self.answer_02 = answer_02
        self.answer_03 = answer_03
        self.correct_answer = correct_answer


#------------ Reads Line From CSV Function ------------------

def read_line(file_path, line_num):
    with open(file_path, "r") as file:

        reader = csv.reader(file)

        for _ in range(line_num-1):
            next(reader)
        return next(reader)

#---------------- Music --------------------------


# This code plays the music when the program starts.

mixer.music.load('Main_Theme.mp3')
print("The music started playing")
mixer.music.play()


#------------------- SET UP ----------------------

# This is a function I use at the end to pause the game for 3 seconds
fpsClock = pygame.time.Clock()


# This creates the window for the game  
WIN = pygame.display.set_mode((WIDTH , HEIGHT))
# This Give The Window A Title
pygame.display.set_caption("LOTR QUIZ")

#This creates a variable for scoreand sets score to 0
#At the start every time the code is run.
score = 0


# This loads the background Window.
background = pygame.image.load('background_1.png')

#------------------- FONTS -----------------------


# These are the fonts used in the game for text.
font_titles = pygame.font.Font('BRIDGE.ttf',60)
font_sub = pygame.font.Font('BRIDGE.ttf',45)
font_little = pygame.font.Font('BRIDGE.ttf',25)




#TITLE SCREEN ----------------------------------------------------------------------------

#On the title screen we have threetexts pieces
#the first variable renders the text size and font.
title_text = font_titles.render('Lord of the Rings',True,BLACK,LIGHT_RED_01)
#the second piece creates a rectangle that goes around it.
TitletextRect = title_text.get_rect()
TitletextRect.center = (WIDTH//2,HEIGHT//2-100)

sub_text = font_sub.render('QUIZ',True,BLACK,LIGHT_RED_02)
sub_text_rect = sub_text.get_rect()
sub_text_rect.center = (WIDTH//2,HEIGHT//2-35)


#this set of code is repeated twice so that there is the second color for when you hover over it.
play_text = font_little.render('Begin?',True,BLACK,WHITE)
play_text_rect = play_text.get_rect()
play_text_rect.center = (WIDTH//2,HEIGHT//2+20)

play_text_light = font_little.render('Begin?',True,BLACK,AQUA_GREEN)
play_text_rect_light = play_text_light.get_rect()
play_text_rect_light.center = (WIDTH//2,HEIGHT//2+20)

#This enables the title screen at the start

title_screen = True

# This sets positions and zize of the question rectangles.
button_01 = pygame.Rect(50,80,790,100)       
button_02 = pygame.Rect(50,230,790,100)
button_03 = pygame.Rect(50,380,790,100)

# Program starts at the first question
question_num = 0

# begin is enabled when start is clicked finnshed is enabled when program is done.
begin = False
finnshed = False



#this opens the file and loads 
file = open('Questions_ltr_quiz.csv')
type(file)




#This bit imports ten random numbers
random_list = random.sample(range(1,21),10)
print(random_list)


#This bit gets those specific lines and adds them to a class.
# So it opens the quiz file and prints the questions that match up to the csv file.


    
question = read_line('Questions_ltr_quiz.csv',random_list[0])


#--------------------------- questions ------------------------------


# This puts the current questions details through a class for easy access
current_question = text(question[0],question[1],question[2],question[3],question[4])


# This is the start of the pygame loop with all the conventions in place.



# while runnning starts the loop because its true
running = True
while running:
    #player hasnt answered the question
    answered  = False
    # This section checks for events.
    for event in pygame.event.get():
        #If the 'x' button pressed game will colse
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #THIS CHECKS WHERE THE MOUSE CICKED AND IF THE MOUSE CLICKED A BUTTON
            if WIDTH // 2 - 50 <= mouse_position[0] <= WIDTH//2+50 and HEIGHT//2 + 5 <= mouse_position[1] <= HEIGHT // 2 + 45 and title_screen == True:
               
                begin     = True
                pygame.time.delay(50)
                
                
                
            # this checks if the user pressed anser 1
            
            if 50 <= mouse_position[0] <= 840 and 80 <= mouse_position[1] <= 180 and title_screen == False:
                response = 1
                print("You picked option 1")
                if current_question.correct_answer == "1":
                    score += 1
                    print(score)
                answered = True
            # answer 2
            if 50 <= mouse_position[0] <= 840 and 230 <= mouse_position[1] <= 330 and title_screen == False:
                response = 2
                print("You picked option 2")
                if current_question.correct_answer == "2":
                    score += 1
                    print(score)
                answered = True

            #answer 3
            if 50 <= mouse_position[0] <= 840 and 380 <= mouse_position[1] <= 480 and title_screen == False:
                response = 3
                print("You picked option 3")
                if current_question.correct_answer == "3":
                    score += 1
                    print(score)
                answered = True

    # this disables the title screen if begin buttin is pressed     
    if begin == True:
        title_screen = False

    question_draw = font_little.render(current_question.text,True,BLACK,WHITE)
    question_rect = question_draw.get_rect()
    question_rect.center = (QUEST_W,QUEST_H)

    answer_1 = font_little.render(current_question.answer_01,True,WHITE)
    answer_1_rect = answer_1.get_rect()
    answer_1_rect.center = (ANSW_1_W,ANSW_1_H)

    answer_2 = font_little.render(current_question.answer_02,True,WHITE)
    answer_2_rect = answer_2.get_rect()
    answer_2_rect.center = (ANSW_2_W,ANSW_2_H)

    answer_3 = font_little.render(current_question.answer_03,True,WHITE)
    answer_3_rect = answer_3.get_rect()
    answer_3_rect.center = (ANSW_3_W,ANSW_3_H)

    score_rend = font_titles.render("Score {} out of 10".format(score),True,BLACK,WHITE)
    score_rect = score_rend.get_rect()
    score_rect.center = (WIDTH//2,HEIGHT//2)

    score_rend_count = font_little.render("{} out of 10".format(score),True,BLACK,WHITE)
    score_rect_count = score_rend_count.get_rect()
    score_rect_count.center = (WIDTH - 60,HEIGHT - 480)

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

        pygame.draw.rect(WIN,BLUE,button_03,2)

        WIN.blit(score_rend_count,score_rect_count)

       

       # This drawsthe highlightedclors when there hovered over.
            

        if 50 <= mouse_position[0] <= 840 and 80 <= mouse_position[1] <= 180:
            pygame.draw.rect(WIN,BLACK,button_01)

        if 50 <= mouse_position[0] <= 840 and 230 <= mouse_position[1] <= 330:
            pygame.draw.rect(WIN,GREY,button_02)

        if 50 <= mouse_position[0] <= 840 and 380 <= mouse_position[1] <= 480:
            pygame.draw.rect(WIN,BLUE,button_03)


            # This changes the questions 
        
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

            # Changes the question number
            question_num += 1
        
        # When finnshed is not true it blits on all the questions.
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