__author__ = 'David Keck'


from random import *
import random
import settings


def welcome(n, name):
    print("\nYou have selected " + name + ".")
    print('Your quiz will consist of {} questions.'.format(n))
    print("Type \"exit\" at anytime to quit.\n")


def randomize(questions, answers):
    # zip questions and answers
    combined = list(zip(questions, answers))

    # shuffle order for random tests
    random.shuffle(combined)

    # unzip shuffled question/answer tuples back into lists
    questions[:], answers[:] = zip(*combined)


def random_answers(answers, n):

    # holds randomly selected answers + correct answer
    random_choices = []

    # remove correct answer so it does not get listed again
    appended_answer_key = answers[:]
    appended_answer_key.pop(n)

    for i in range(settings.CHOICES-1):
        # randomly select multiple choice answers
        random_index = randrange(0, len(appended_answer_key))
        random_choices.append(appended_answer_key[random_index])

        # remove the randomly selected answer so it doesn't get listed again
        appended_answer_key.pop(random_index)

    # add the correct answer
    random_choices.append(answers[n])

    # shuffle all answers so location of correct answer is random
    random.shuffle(random_choices)

    for i in range(len(random_choices)):
        print('{}: {}'.format(i+1, random_choices[i]))

    return random_choices


def get_answer(random_choices, answers, n):

    try:
        ans = int(input("\nPlease enter your answer: "))
    except(ValueError, TypeError, NameError):
        return -1

    while ans > settings.CHOICES or ans < 1:
        try:
            ans = int(input("\nThat's not an accepted input. Try again: "))
        except(ValueError, TypeError, NameError):
            return -1

    # if the answer is correct
    if random_choices[ans-1] == answers[n]:
        print(random.choice(settings.ENCOURAGEMENT))
        return 0

    else:
        print("That is incorrect. :(")
        print('The correct choices is: {}\n'.format(answers[n]))
        return ans


def start(questions, answers, name):

    welcome(len(questions), name)
    randomize(questions, answers)

    # hold missed question/answer in list
    missed_questions = []
    missed_answers = []

    for i in range(len(questions)):
        print('Question {}: {}\n'.format(i+1, questions[i]))

        # get the result of each question
        ans = get_answer(random_answers(answers, i), answers, i)

        # user did not enter an integer
        if ans == -1:
            print("\nNow exiting quiz...")
            break

        # question was missed
        if ans != 0:
            missed_questions.append(questions[i])
            missed_answers.append(answers[i])

    if len(missed_questions) != 0:
        for i in range(len(missed_questions)):
            print('You missed this question: {} {}'.format(missed_questions[i], missed_answers[i]))

    else:
        print("\nYou missed zero questions! You are ready for the exam! :D")