calls = 0
def count_calls():  #изменяет значение переменной calls
    global calls
    calls = calls + 1



def string_info(string: str):  # Принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
    count_calls()
    l = len(string)
    upper = string.upper()
    lower = string.lower()
    return l, upper, lower


def is_contains(string: str, list_to_search: list):  # принимает два аргумента: строку и список
    count_calls()
    for item in list_to_search:
        if item.lower() == string.lower():
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)