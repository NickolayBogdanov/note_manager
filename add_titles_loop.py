titles = []

while True:
    titles.append(input(str("введите заголовок (чтобы остановить введите стоп или не вводите ничего): ")))
    print(titles[-1])
    if titles[-1] == str("стоп") or titles[-1] == str("") or titles[-1] == str(" "):
        titles.pop(-1)
        break
print(titles)
