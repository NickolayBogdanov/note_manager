titles = []

while True:
    titles.append(input("введите заголовок (чтобы остановить введите стоп или не вводите ничего): "))
    title = titles[-1]
    if titles[-1] == ("стоп") or titles[-1] == (""):
        titles.pop(-1)
        break
print(titles)
