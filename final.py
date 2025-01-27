username = input("Введите имя пользователя: ")
content = input("Введите содержание заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Введите дату создания (в формате дд-мм-гггг): ")
issue_date = input("Введите дату изменения (в формате дд-мм-гггг): ")
title = [input("Введите заголовок")]

title.append(input('Введите 2 заголовок')) #заголовки

print(title)

note = [
username,
content,
status,
created_date,
issue_date,
title
]

print("Имя пользователя:", note[0])
print("Содержание:", note[1])
print("Статус:", note[2])
print("Дата создания:", note[3])
print("Дата изменения:", note[4])
print("Заголовки:", note[5])