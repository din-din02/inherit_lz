from book import EBook

title=input('Введите название книги:')
author=input('Введите автора книги:')
year=int(input('Введите год выпуска книги:'))
file_size=input('Введите размер книги:')
format=input('Введите формат книги(электронная или бумажная):')
free=input('Книгу можно получить бесплатно(да или нет)?')
a=EBook(title,author,year, file_size, format, free)
a.info()
a.actual()
a.is_available()
a.is_free()