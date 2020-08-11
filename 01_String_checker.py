# Function goes here


def string_checker(question, to_check):
    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item

        print("Can only be circle, square, rectangle, triangle, parallelogram or trapezium")


# *** Main routine starts here ****

available_shapes = ["circle", "square", "rectangle", "triangle", "parallelogram", "trapezium"]

yes_no = ["yes", "no"]

circle = ["c", "circle"]
square = ["s", "square"]
rectangle = ["r", "rectangle"]
triangle = ["t", "triangle"]
parallelogram = ["p", "parallelogram"]
trapezium = ["trapezium"]

ask_user = string_checker("choose a shape to use:", available_shapes)
print("shape: {}".format(ask_user))
if ask_user == "square":
    square_length = ("What is the length?")
    perimeter = square_length *4
    print("the perimeter is {}".format(perimeter))


