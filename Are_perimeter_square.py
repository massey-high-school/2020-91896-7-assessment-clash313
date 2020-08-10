# Function goes here


# Number Checking Function
def num_check(question):

    error = "Please enter a number that is more than zero"

    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def string_checker(question, to_check):
    valid = False
    while not valid:

        response = input(question).lower()

        if response in to_check:
            return response

        else:
            for item in to_check:
                # checks if response is the first letter of an item in the list
                if response == item[0]:
                    # note: returns the entire response rather than just the first letter
                    return item

                print("Can only be circle, square, rectangle, triangle, parallelogram or trapezium")

# Main routine

history = []

# loop to get shape and do calculations...

    # ask for shape
available_shapes = ["circle", "square", "rectangle", "triangle", "parallelogram", "trapezium"]

ask_user = string_checker("choose a shape to use:", available_shapes)
print(ask_user)

    # get area

    # get perimeter

    # add shape, area and perimeter to list

    # add shape_details to history


# output entire history