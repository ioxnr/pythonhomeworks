def num_translate_adv(number):
    if number[0].isupper():
        if number.lower() in translation:
            return translation[number.lower()].capitalize()
        else:
            return None
    if number in translation:
        return translation[number]
    else:
        return None


translation = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять", "six": "шесть",
               "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}

print(num_translate_adv("One"))
print(num_translate_adv("eight"))
print(num_translate_adv("Four"))
print(num_translate_adv("eleven"))
print(num_translate_adv("Seven"))
print(num_translate_adv("Fourteen"))
