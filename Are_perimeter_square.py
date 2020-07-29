# Function goes here


def num_checker(question):

    error = "it should contain greater numbers than zero"

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        # look at each character in string and if it's a number, complain
        for letter in response:
            if letter.isdigit():
                has_errors = "yes"
                break

        if response == "":
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response