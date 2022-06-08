import csv
import random
#This opens the file 
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

set = 0
question_var = 'question_var'
#This bit gets those specific lines and adds them to a class.
# So it opens the quiz file and prints the questions that match up to the csv file.

for item in random_list:
    print(item)
    question = read_line('Questions_ltr_quiz.csv',random_list[set])
    print(question)
    set += 1