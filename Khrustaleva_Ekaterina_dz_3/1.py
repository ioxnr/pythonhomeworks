def num_translate(number):
    if number in translation:
        return translation[number]
    else:
        return None


translation = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять", "six": "шесть",
               "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}

print(num_translate("one"))
print(num_translate("eight"))
print(num_translate("four"))
print(num_translate("eleven"))
