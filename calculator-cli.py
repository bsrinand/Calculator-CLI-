def calculator():
    try:
        expression = input("Enter expression: ")
        result = eval(expression)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)

if _name_ == "_main_":
    calculator()
