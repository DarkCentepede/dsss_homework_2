import random

def generate_random_integer(min_value, max_value):
    """
    Generate a random integer between min_value and max_value (inclusive).
    
    Parameters:
    min_value (int): The minimum value for the random integer.
    max_value (int): The maximum value for the random integer.

    Returns:
    int: A random integer within the specified range.
    """
    return random.randint(min_value, max_value)


def choose_random_operator():
    """
    Randomly select a mathematical operator from a predefined list.
    
    Returns:
    str: A randomly selected operator ('+', '-', '*', '/').
    """
    return random.choice(['+', '-', '*', '/'])


def calculate_expression(num1, num2, operator):
    """
    Calculate the result of a mathematical expression based on the provided numbers and operator.
    
    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operator (str): The mathematical operator.

    Returns:
    tuple: A tuple containing the expression as a string and the calculated result.
    """
    expression = f"{num1} {operator} {num2}"
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        # Prevent division by zero
        if num2 == 0:
            return expression, None  # Indicate an invalid operation
        result = num1 / num2
        
    return expression, result


def math_quiz():
    """
    Main function to run the math quiz game.
    
    The user will be presented with several math problems and must provide the correct answers.
    The user's score will be displayed at the end of the game.
    """
    score = 0
    total_questions = 3  # Number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 10)  # Changed to integer for consistency
        operator = choose_random_operator()

        problem, answer = calculate_expression(num1, num2, operator)
        
        if answer is None:  # Handle division by zero case
            print(f"\nQuestion: {problem} (Invalid operation due to division by zero)")
            continue

        print(f"\nQuestion: {problem}")

        while True:
            user_input = input("Your answer: ")
            try:
                user_answer = float(user_input)  # Allow for decimal answers
                break  # Exit loop if input is valid
            except ValueError:
                print("Invalid input
