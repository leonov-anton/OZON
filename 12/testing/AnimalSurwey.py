from survey import survey

question = "Ваше любимое живатное?"
surv = survey(question)

surv.show_question()
print("Введите q для окончания программы")
while True:
    answer = input("Животное: ")
    if answer == 'q':
        break
    surv.save_answer(answer)

surv.show_resolts()