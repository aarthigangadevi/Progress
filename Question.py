class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# code for multiple choice test using class and objects
'''from Question import Question
question_prompts = [
    "what color is apple?\n(a) Red\n(b) Blue\n\n ",
    "what color is banana?\n(a) Red\n(b) yellow\n\n ",
    "what color is grape?\n(a) Green\n(b) Blue\n\n "
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a")
]


def run_test(questions):
    score=0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("you got " + str(score) + "/" + str(len(questions))+ "correct")

run_test(questions)'''