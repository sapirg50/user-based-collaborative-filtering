class Question:
    def __init__(self, question, options, function, question_type="close"):
        self.question = question
        self.options = options
        self.type = question_type
        self.function = function

    def ask(self):
        if self.type == "close":
            try:
                print(self.question)
                for i, option in enumerate(self.options):
                    print(f'({i + 1}) {option}')
                x = int(input())
                if 1 <= x <= len(self.options):
                    return self.options[x - 1]
                else:
                    print("not valid")
                    exit(-1)
            except ValueError:
                print("not integer")
                exit(-1)
        elif self.type == "open":
            try:
                print(self.question)
                x = int(input())
                return x
            except ValueError:
                print("not integer")
                exit(-1)
        else:  # type == "range"
            try:
                print(self.question)
                print(f'נא לבחור בין {self.options[0]} ל-{self.options[1]}')
                x = int(input())
                if self.options[0] <= x <= self.options[1]:
                    return x
                else:
                    print("not valid")
                    exit(-1)
            except ValueError:
                print("not integer")
                exit(-1)


q1 = Question("מהו המגדר שלך?", ["זכר", "נקבה", "לא רוצה לומר"], "replace")
q2 = Question("מהו גילך (נא להזין מספר שלם)", None, "min max", "open")
q3 = Question("מהו איזור מגורייך?", ["מרכז", "צפון", "דרום"], "replace")
q4 = Question("כמה חשובה לך הרמה האקדמית?", [1, 5], "min max", "range")
q5 = Question("כמה חשוב לך היחס האישי?", [1, 5], "min max", "range")
q6 = Question("האם אתה מעדיף מכללה או אוניברסיטה?", ["מכללה", "אוניברסיטה", "לא משנה לי"], "replace")
q7 = Question("דרג את החשיבות שלך עבור ההווי הסטודנטיאלי", [1, 5], "range", "min max")
q8 = Question("בבחירת מוסד הלימודים, האם חשוב לך להישאר קרוב לבית?", ["כן", "לא"], "replace")
q9 = Question("בבחירת מוסד הלימודים, האם היה חשוב לך להישאר קרוב לבית?",
              ["מדעי המחשב", "פסיכולוגיה", "אומנות", "הנדסה", "משפטים", "סיעוד", "מנהל עסקים", "כלכלה/חשבונאות", "אחר"],
              "replace")
q10 = Question("כמה אתה מעוניין לשלם עבור שכר לימוד בשנה?",
               ["10,000 - 20,000", "20,000 - 30,000", "30,000 - 40,000", "40,000 ומעלה"], "min max")

question_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
