

def display_question(question, options):
    print(question)
    for i in range(len(options)):
        print(f'{i+1}. {options[i]}')

def get_user_answer():
    while True:
        user_answer = input('Enter your answer (1, 2, 3...): ')
        if user_answer.isdigit() and 1 <= int(user_answer) <= 3:
            return int(user_answer)
        print("Invalid input! Please enter a number between 1 and 3.")

def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def run_quiz(quiz):
    score = 0
    total_questions = len(quiz)

    for question, options, correct_answer in quiz:
        display_question(question, options)
        user_answer = get_user_answer()
        if check_answer(user_answer, correct_answer):
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")
            print(f"The correct answer is: {options[correct_answer - 1]}")
        print()

    final_score = (score / total_questions) * 100
    print(f"Your final score is: {final_score:.2f}% ({score}/{total_questions})")

if __name__ == "__main__":
   quiz = [
        ("What is the capital of France?", ["London", "Paris", "Berlin"], 2),  # Correct answer index: 2 (Paris)
        ("What is the largest planet in our solar system?", ["Jupiter", "Mars", "Earth"], 1),  # Correct answer index: 1 (Jupiter)
        ("Who wrote 'Romeo and Juliet'?", ["William Shakespeare", "Jane Austen", "Charles Dickens"], 1),  # Correct answer index: 1 (William Shakespeare)
        ("What is the capital of Nigeria?", ["Lagos", "Abuja", "Kano"], 2),  # Correct answer index: 2 (Abuja)
        ("What is the capital of Japan?", ["Tokyo", "Beijing", "Seoul"], 1),  # Correct answer index: 1 (Tokyo)
        ("Who is the current president of the United States?", ["Donald Trump", "Barack Obama", "Joe Biden"], 3),  # Correct answer index: 3 (Joe Biden)
        ("What is the capital of Australia?", ["Sydney", "Melbourne", "Canberra"], 3)  # Correct answer index: 3 (Canberra)
    ]

   run_quiz(quiz)
