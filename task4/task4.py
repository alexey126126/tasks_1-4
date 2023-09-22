text = "Это    текст    с     множеством пробелов! И      разными   знаками препинания.Которые нужно обработать?"

# замена нескольких пробелов на один

text = " ".join(text.split())

# убираем пробелы перед знаками препинания
punctuation = [".", "!", "?", ",", ";"]
for p in punctuation:
    text = text.replace(" " + p, p)

# добавляем пробелы после знаков препинания
for p in punctuation:
    text = text.replace(p, p + " ")
text = text.replace("  ", " ")
print(text)