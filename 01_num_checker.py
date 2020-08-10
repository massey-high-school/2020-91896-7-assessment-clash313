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

width = num_check("width of the shape? ")
length = num_check("length of the shape?")

available_shapes = ["circle", "square", "rectangle", "triangle", "parallelogram", "trapezium"]


print("num checker: {}".format(num_check))



