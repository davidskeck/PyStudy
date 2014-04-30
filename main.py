__author__ = 'David Keck'


import quiz
import os


def main():

    print("Welcome to PyStudy!\n")
    print("The following tests are installed:")

    # get dir names
    tests = (os.walk('.').__next__()[1])

    # print available tests
    for i, test in enumerate(tests):
        print('{}: {}'.format(i+1, test))

    ans = int(input("\nWhich test would you like to take? "))

    while ans < 1 or ans > len(tests):
        ans = int(input("\nThat is not a valid test selection. Try again: "))

    test_name = tests[ans-1]

    # open question and answer files
    try:
        answer_file = open(test_name + '/answers.txt', 'r')
        question_file = open(test_name + '/questions.txt', 'r')
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

    if len(questions) != len(answers):
        print("There is a problem with your {} files.".format(test_name))
        print("Make sure that you have an equal number of questions and answers.")
        print("PyStudy will now close...")
        exit()

    # start the quiz
    quiz.start(questions, answers, test_name)

    # give time to read results
    try:
        input("\nPress <Enter> to close.")
    except SyntaxError:
        pass

main()