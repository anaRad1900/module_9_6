def all_variants(text):
    length = len(text)

    # Сначала выводим односивольные последовательности
    for i in range(length):
        yield text[i]

    # Затем выводим двусимвольные последовательности
    for start in range(length):
        if start < length - 1:
            yield text[start:start + 2]  # Генерация двусимвольных

    # И наконец, выводим трёхсимвольные последовательности
    for start in range(length):
        if start < length - 2:
            yield text[start:start + 3]  # Генерация трёхсимвольных


# Пример использования функции all_variants
a = all_variants("abc")
for i in a:
    print(i)