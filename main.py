__author__ = 'David Keck'


import quiz


def main():
    # open question and answer files
    try:
        answer_file = open('answers.txt', 'r')
        question_file = open('questions.txt', 'r')
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
    quiz.start(questions, answers)

    # give time to read results
    try:
        input("\nPress <Enter> to close.")
    except SyntaxError:
        pass

main()