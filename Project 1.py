def print_welcome_message():
    print("Welcome to my computer quiz!")

def get_user_choice():
    playing = input("Do you want to play? ")
    return playing.lower()

def ask_question(question, correct_answer):
    answer = input(question)
    if answer.lower() == correct_answer.lower():
        print('Correct!')
        return 1
    else:
        print('Incorrect!')
        return 0

def calculate_score(score):
    percentage = (score / 4) * 100
    return percentage

def print_results(score, percentage):
    print("You got", score, "question(s) correct!")
    print("You got", percentage, "%")

def play_quiz():
    print_welcome_message()

    playing = get_user_choice()
    if playing != "yes":
        quit()

    print("Okay! Let's play:)")
    score = 0

    score += ask_question("What does CPU stand for? ", "Central Processing Unit")
    score += ask_question("What does GPU stand for? ", "Graphics Processing Unit")
    score += ask_question("What does RAM stand for? ", "Random Access Memory")
    score += ask_question("What does PSU stand for? ", "Power Supply")

    percentage = calculate_score(score)
    print_results(score, percentage)

play_quiz()
