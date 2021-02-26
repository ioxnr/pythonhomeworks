def get_number(x):
    if '+' in x:
        return x[1]
    elif '-' in x:
        return x[1]


sentence = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(sentence):
    number = get_number(sentence[i])
    if sentence[i].isdigit() or number is not None and number.isdigit():
        if sentence[i].isdigit():
            sentence[i] = sentence[i].zfill(2)
        elif number is not None and number.isdigit():
            sentence[i] = sentence[i][0] + number.zfill(2)
        sentence.insert(i, '"')
        sentence.insert(i + 2, '"')
        i += 2
    i += 1

in_quote = False
result = ''

for i, string in enumerate(sentence):
    if string == '"':
        in_quote = not in_quote

    result += string

    if not (in_quote or i == len(sentence) - 1):
        result += ' '

print(result)
