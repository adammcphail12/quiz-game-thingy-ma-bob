import csv
file = open('Questions_ltr_quiz.csv')
type(file)

csvreader = csv.reader(file)

question_01 = []
question_01 = next(csvreader)
question_02 = []
question_02 = next(csvreader)

question_03 = []
question_03 = next(csvreader)

question_04 = []
question_04 = next(csvreader)

question_05 = []
question_05 = next(csvreader)

question_06 = []
question_06 = next(csvreader)

question_07 = []
question_07 = next(csvreader)

question_08 = []
question_08 = next(csvreader)

question_09 = []
question_09 = next (csvreader)

question_10 = []
question_10 = next(csvreader)


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