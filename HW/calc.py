result = 0
operand = None
operator = None
operators = "-+/*"
wait_for_number = True

while True:
    val = input(">>> ")

    if val == "=":
        print(f"Result: {result}")
        break

    if wait_for_number:
        try:
            val = int(val)
            
            if operand == None:
                operand = val
                result = val
            else:
                if operator == "+":
                    result = float(result + val)
                elif operator == "-":
                    result = float(result - val)
                elif operator == "*":
                    result = float(result * val)
                elif operator == "/":
                    result = float(result / val)

            wait_for_number = False

        except ValueError:
            print(f"{val} is not a number. Try again.")
    else:
        try:
            val = int(val)
            print(f"{val} is not '+' or '-' or '/' or '*'. Try again.")
        except ValueError:
            if operators.find(val) == -1:
                print(f"{val} is not '+' or '-' or '/' or '*'. Try again.")
            else:
                operator = val
                wait_for_number = True