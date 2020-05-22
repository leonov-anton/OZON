class Survey:
    """ Собирает ответы на вопросы """

    def __init__(self, quest):
        self.question = quest
        self.answers = []

    def show_question(self):
        print(self.question)

    def save_answer(self, answer):
        self.answers.append(answer)

    def show_resolts(self):
        print("Survey resolts: ")
        for answer in self.answers:
            print(f'- {answer}')

