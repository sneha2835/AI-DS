def case(s, letter):
    index = s.lower().find(letter.lower())
    if index == -1:
        return s
    return s[:index].lower() + s[index:].upper()

string= input("Enter the string: ")
letter = input("Enter the letter: ")

if len(letter) != 1:
    print("Please enter a single letter.")
else:
    print("Result:", case(string, letter))