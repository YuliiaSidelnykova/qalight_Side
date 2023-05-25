# Є рядок "Мені дуже подобається вивчати пайтон!
# Здається, це найлегша з потужних мов для вивчення"

str_a: str = '''Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення'''
print(str_a)
new_str: str = ''
new_word: str = ''
# 1. Розбити рядок на список окремих слів;
str_a.split(' ')
words_list: list = str_a.split(' ')
print(words_list)

# 2. Замінити в кожному слові усі голосні літери іншим символом,
# наприклад #
for word in words_list:
    word_by_chars = list(word)
    i=0
    for char in word_by_chars:
        if char in ('а', 'е', 'і', 'у', 'и', 'є', 'о', 'я', 'А', 'Е', 'І', 'У', 'И', 'Є', 'О', 'Я'):
            word_by_chars[i]='#'
        i+=1
    words_list = ''.join(word_by_chars)
    print(words_list)
# 3. Бонусне завдання: Відновити рядок зі списку,
# зі вже заміненими словами.
    new_str += ''.join(words_list)+' '
print(new_str)




