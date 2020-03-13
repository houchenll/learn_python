print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError as e:
        print("You can't divide by zero!")
    else:
        # else 执行依赖于try正常执行的代码；
        # else 可使用定义在try中的answer
        print(answer)
