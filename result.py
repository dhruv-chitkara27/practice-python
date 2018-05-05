def check_answer(my_answer, answer):
    if my_answer == answer:
        return True
    else:
        return False

def check_answers(my_answers,answers):
    # Checks the five answers provided to a multiple choice quiz
    # and returns the results.
    results = []
    for i in range(len(my_answers)):
        results.append(check_answer(my_answers[i], answers[i]))
    count_correct = 0

    for result in results:
        if result:
            count_correct += 1

    score_string = "You scored " + str(count_correct) + " out of 5."
    if count_correct/len(results) > 0.7:
        return "Congratulations, you passed the test! " + score_string
    elif (len(results) - count_correct)/len(results) >= 0.3:
        return "Unfortunately, you did not pass. " + score_string
