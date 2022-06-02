import csv
import random
file = open('Questions_ltr_quiz.csv')
type(file)

csvreader = csv.reader(file)


skip = random.randrange(0,2)
if skip == 1:
    next(csvreader)
    question_01 = next(csvreader)
else:
    question_01 = next(csvreader)
    next(csvreader)
skip = random.randrange(0,2)
if skip == 1:
    next(csvreader)
    question_02 = next(csvreader)
else:
    question_02 = next(csvreader)
    next(csvreader)
skip = random.randrange(0,2)
if skip == 1:
    next(csvreader)
    question_03 = next(csvreader)
else:
    question_03 = next(csvreader)
    next(csvreader)
skip = random.randrange(0,2)
if skip == 1:
    next(csvreader)
    question_04 = next(csvreader)
else:
    question_04 = next(csvreader)
    next(csvreader)
skip = random.randrange(0,2)
if skip == 1:
    next(csvreader)
    question_05 = next(csvreader)
else:
    question_05 = next(csvreader)
    next(csvreader)
skip = random.randrange(0,2)
if skip == 1:
    next(csvreader)
    question_06 = next(csvreader)
else:
    question_06 = next(csvreader)
    next(csvreader)
skip = random.randrange(0,2)
if skip == 1:
    next(csvreader)
    question_07 = next(csvreader)
else:
    question_07 = next(csvreader)
    next(csvreader)
skip = random.randrange(0,2)
if skip == 1:
    next(csvreader)
    question_08 = next(csvreader)
else:
    question_08 = next(csvreader)
    next(csvreader)
skip = random.randrange(0,2)
if skip == 1:
    next(csvreader)
    question_09 = next(csvreader)
else:
    question_09 = next(csvreader)
    next(csvreader)
    skip = random.randrange(0,2)
if skip == 1:
    next(csvreader)
    question_10 = next(csvreader)
else:
    question_10 = next(csvreader)
    next(csvreader)


print(question_01)
print(question_02)
print(question_03)
print(question_04)
print(question_05)
print(question_06)
print(question_07)
print(question_08)
print(question_09)
print(question_10)

csvreader.close()