# Function goes here


def string_checker(question, to_check):
    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item(0):
                return item

        print("Can only be circle, square, rectangle, triangle, parallelogram or trapezium")


# *** Main routine starts here ****

available_shapes = ["circle", "square", "rectangle", "triangle", "parallelogram", "trapezium"]

ask_user = string_checker("choose a shape to use:", available_shapes)
print(ask_user)