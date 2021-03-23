import re

RE_EMAIL = re.compile(r"(^[a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")


def email_parse(email_address):
    email_match = RE_EMAIL.fullmatch(email_address)
    if email_match is None:
        raise ValueError(f'wrong email:{email_address!r}')
    username, domain = email_match.groups()
    email_data = {'username': username, 'domain': domain}
    return email_data


print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))
