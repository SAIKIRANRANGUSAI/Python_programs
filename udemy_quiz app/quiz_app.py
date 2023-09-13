import time
from dataclasses import dataclass
from random import choice, shuffle  # shuffle is a list(reorganize the order of the list items)

# @dataclass will holds them data values they are different from regular class.
@dataclass(slots=True)   # slots will help us to speed up the process of accessing the varible inside the data class
class Question:   # this block is data class and it holds the info of each question
    question: str
    answers: list[str]
    correct_answer: str

def random_question(questions: list[Question])-> int:
    question: Question = choice(questions)   # choosing the question from the choise
    print(f'{question.question}')

    shuffle(question.answers)

    for answer in question.answers:
        print('-', answer)

    user_input: str = input('\n your answer: >>').lower().strip()  # lower() your input should be in lower case itself.
                                                                  # strip() is used to remove the unwanted spaces between the answer. ex= " hello" =="hello"

    if user_input == question.correct_answer:  #logic of the program
        print('correct!\n')
        questions.remove(question)
        return 1
    else:   # capatalize() is used to  covert the 1st character of string is in uppercase remaining all in lower case.
        print(f'wrong, the answer was: {question.correct_answer.capitalize()}\n')
        questions.remove(question)

        return 0


def run_quiz(questions: list[Question]):  # This block is used to get calculate the score of user(correct answers).
    total_score: int = 0
    while questions:
        score: int = random_question(questions=questions)
        total_score += score
        time.sleep(1.5)
    else:
        print('final score:', total_score)


def get_questions()-> list[Question]:
    return [
        Question(question='how are you?',
                 answers=['good', 'bad', 'ok', 'potato'],
                 correct_answer='good'),
        Question(question='what is your name',
                 answers=['sai', 'kiran', 'rangu', 'rsk'],
                 correct_answer='rsk'),
        Question(question='what time it is?',
                 answers=['12:30pm', '1:00pm', '2:00pm', '12:00pm'],
                 correct_answer='12:00pm'),
        Question(question='what is 1 +1?',
                 answers=['the answer', 'the question'],
                 correct_answer='the question'),
    ]

def main():
    questions: list[Question] = get_questions()
    run_quiz(questions=questions)


if __name__ == '__main__':
    main()