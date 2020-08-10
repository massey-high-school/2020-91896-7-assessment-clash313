# Function goes here
def unit_checker(preferred_unit):

    unit_to_check = preferred_unit

# Abbreviation lists

    centimetres = ["cm", "centimetres"]
    metres = ["m", "metres"]

    if unit_to_check == "":
        print("you choose {}".format(unit_to_check))
        return unit_to_check

    elif unit_to_check == "m" or unit_to_check.lower() in metres:
        return "metres"
    elif unit_to_check == "cm" or unit_to_check.lower() in centimetres:
        return "centimetres"

    else:
        print(unit_to_check)
        return unit_to_check

question_1 = unit_checker("unit ?")
print(question_1)