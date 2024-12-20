class Numerology:
    def __init__(self, sName, sDOB):
        # dict that has each letter connected to its number
        self.letter_values = {
            'a': 1, 'j': 1, 's': 1,
            'b': 2, 'k': 2, 't': 2,
            'c': 3, 'l': 3, 'u': 3,
            'd': 4, 'm': 4, 'v': 4,
            'e': 5, 'n': 5, 'w': 5,
            'f': 6, 'o': 6, 'x': 6,
            'g': 7, 'p': 7, 'y': 7,
            'h': 8, 'q': 8, 'z': 8,
            'i': 9, 'r': 9
        }

        # stores the name and dob
        self.name = sName
        self.dob = sDOB

        # grabs all the digits from the dob, while ignoring the non digit characters
        self.digit = [int(char) for char in self.dob if char.isdigit()]

        # creates var to store data and for them to be calculated later
        self._life_path = None
        self._birth_day = None
        self._attitude = None
        self._soul = None
        self._personality = None
        self._power_name = None

        # starts the calculations
        self.calculateNumerology()

    # performs the main calculations
    def calculateNumerology(self):
        vowels, consonants = "", ""
        for char in self.name.lower():
            if char in 'aeiou':
                vowels += char
            elif char.isalpha():
                consonants += char

        # performs the calculations
        self._life_path = self.calculateLifePath()
        self._birth_day = self.calculateBirthDay()
        self._attitude = self.calculateAttitude()
        self._soul = self.calculateSoul(vowels)
        self._personality = self.calculatePersonality(consonants)
        self._power_name = self.calculatePowerName()

    # returns the users name
    @property
    def Name(self):
        return self.name

    # returns the users dob
    @property
    def Birthdate(self):
        return self.dob

    # retursn the life path number
    @property
    def LifePath(self):
        return self._life_path

    # returns the birth day number
    @property
    def BirthDay(self):
        return self._birth_day

    # returns the attitude number
    @property
    def Attitude(self):
        return self._attitude

    # returns the soul number
    @property
    def Soul(self):
        return self._soul

    # returns the personality number
    @property
    def Personality(self):
        return self._personality

    # returns the power name number
    @property
    def PowerName(self):
        return self._power_name

    # caculates the life path number
    def calculateLifePath(self):
        total = sum(self.digit)
        return self.singleDigit(total)

    # calculates the birthday number
    def calculateBirthDay(self):
        _, day, _ = self.dob.split('/')
        return self.singleDigit(int(day))

    # calculates the attitude number
    def calculateAttitude(self):
        month, day, _ = self.dob.split('/')
        month_total = sum(int(digit) for digit in month)
        day_total = sum(int(digit) for digit in day)
        return self.singleDigit(month_total + day_total)

    # calculates the soul number
    def calculateSoul(self, vowels):
        soul_value = sum(self.letterValue(char) for char in vowels)
        return self.singleDigit(soul_value)

    # calculates the personality number
    def calculatePersonality(self, consonants):
        personality_value = sum(self.letterValue(char) for char in consonants)
        return self.singleDigit(personality_value)

    # calculates the powername number
    def calculatePowerName(self):
        return self.singleDigit(self._soul + self._personality)

    # reduces a number to a single digit
    def singleDigit(self, num):
        while num > 9:
            num = sum(int(digit) for digit in str(num))
        return num

    # returns the numerology value of a given letter
    def letterValue(self, char):
        return self.letter_values.get(char, 0)

    # uses a dict to store all the answers
    @property
    def LifePathDescription(self):
        descriptions = {
            1: "The Independent: Wants to work/think for themselves",
            2: "The Mediator: Avoids conflict and wants love and harmony",
            3: "The Performer: Likes music, art and to perform or get attention",
            4: "The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful",
            5: "The Adventurer: Likes to travel and meet others, often an extrovert",
            6: "The Inner Child: Is meant to be a parent and/or one that is young at heart",
            7: "The Naturalist: Enjoy nature and water and alternative life paths, open to spirituality",
            8: "The Executive: Gravitates to money and power",
            9: "The Humanitarian: Helps others and/or experiences pain and learns the hard way"
        }
        return descriptions.get(self.LifePath, "Life Path number is unkown.")

    # returns the numerology results
    def __str__(self):
        return ("\n"
                f"Client Name: {self.Name}\n"
                f"Client DOB: {self.Birthdate}\n"
                f"Life Path Number: {self.LifePath:>3}\n"
                f"Birth Day Number: {self.BirthDay:>3}\n"
                f"Attitude Number: {self.Attitude:>4}\n"
                f"Soul Number: {self.Soul:>8}\n"
                f"Personality Number: {self.Personality}\n"
                f"Power Name Number: {self.PowerName:>2}\n"
                f"Life Path Detail: {self.LifePathDescription:>3}")

