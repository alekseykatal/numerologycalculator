from NumerologyLifePathDetails import Numerology

# checks if the date is valid
def validDate(dob):
    # replaces the '/' into '-'
    dob = dob.replace('/', '-')
    try:
        month, day, year = map(int, dob.split('-'))

        if 1 <= month <= 12 and 1 <= day <= 31 and 1000 <= year <= 9999:
            # formats date into a correct format
            return "{:02d}/{:02}/{}".format(month, day, year)
    except ValueError:
        return False


# checks if the name is valid
def validName(name):
    return bool(name.strip())


def main():
    # loops until a valid name is entered
    while True:
        name = input("Enter your full birth name: ").strip()
        if validName(name):
            break
        else:
            print("Please enter a valid name.")

    # loops until a valid dob is entered
    while True:
        dob = input("Enter your birth date (mm-dd-yyyy): ").strip()
        dob_formatted = validDate(dob)
        if dob_formatted:
            break
        else:
            print("Please enter a valid date in the format mm-dd-yyyy.")

    # create a numerology object
    numerology = Numerology(name, dob_formatted)

    # print the results
    print(numerology)


main()
