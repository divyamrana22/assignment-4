import random

def multiplication_game():
    num_correct = 0
    for i in range(10):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        answer = num1 * num2
        user_answer = int(input(f"Question {i+1}: {num1} x {num2} = "))
        if user_answer == answer:
            print("Right!")
            num_correct += 1
        else:
            print(f"Wrong. The answer is {answer}.")
    print(f"You got {num_correct} out of 10 correct.")

multiplication_game()