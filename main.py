__author__ = 'David Keck'


import quiz
import os


def main():

    print("Welcome to PyStudy!\n")
    print("The following tests are installed:")

    # get dir names
    tests = (os.walk('.').next()[1])

    # print available tests
    for i, test in enumerate(tests):
        print('{}: {}'.format(i+1, test))

    ans = int(input("\nWhich test would you like to take? "))

    # open question and answer files
    try:
        answer_file = open(tests[ans-1] + '/answers.txt', 'r')
        question_file = open(tests[ans-1] + '/questions.txt', 'r')
    except IOError:
        print("Error: one or more files cannot be found.")
        return 0

    # read data into arrays
    try:
        with answer_file:
            answers = answer_file.read().splitlines()
        with question_file:
            questions = question_file.read().splitlines()
    finally:
        answer_file.close()
        question_file.close()

    # start the quiz
    quiz.start(questions, answers, tests[ans-1])

    # give time to read results
    try:
        input("\nPress <Enter> to close.")
    except SyntaxError:
        pass

main()