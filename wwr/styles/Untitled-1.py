def numbers(number):
    if isinstance (number, float):
        answer = print(f"{number} is a decimal point and is not even")
        return answer
    if number%2 == 0:
        answer = f"{number} is even"
    else:
        answer = f"{number} is odd"
    print(answer)
    return answer

numbers(6.5)
