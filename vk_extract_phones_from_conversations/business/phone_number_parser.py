# За регулярку спасибо https://habr.com/ru/articles/110731/ =)
import re


def try_to_parse_phone_number(string: str):
    pattern = re.compile(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$')
    match = pattern.search(string)
    return match.group() if match else None


def format_phone(string: str):
    tokens_to_remove = [" ", "-", "(", ")"]
    result = string
    for token in tokens_to_remove:
        result = result.replace(token, "")

    string_as_list = list(result)
    if string_as_list[0] == "8":
        string_as_list[0] = "7"
    elif string_as_list[0] == "+":
        string_as_list.pop(0)
    elif string_as_list[0] == "9":
        string_as_list.insert(0, "7")
    result = "".join(string_as_list)
    return result
