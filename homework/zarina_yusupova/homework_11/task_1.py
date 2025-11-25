class Book:
    page_material = 'бумага'
    has_text = True

    def __init__(self, title, author, number_of_pages, isbn, is_reserved):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.is_reserved = is_reserved

    def reserve(self):
        self.is_reserved = True

    def info(self):
        inform = (f''
                  f'Название: {self.title}, Автор: {self.author}, страниц: {self.number_of_pages}, '
                  f' материал: {self.page_material}'
                  )
        if self.is_reserved:
            print(inform + ', зарезервирована')
        else:
            print(inform)


book1 = Book('Престуление и наказание', 'Достоевский', 500, 123456789, False)
book2 = Book('Анна Каренина', 'Толстой', 800, 111111111, False)
book3 = Book('Отцы и Дети', 'Тургенев', 450, 222222222, False)
book4 = Book('Мастер и Маргарита', 'Булгаков', 500, 333333333, False)
book5 = Book('Тихий Дон', 'Шолохов', 1800, 444444444, False)
book4.reserve()

my_books = [book1, book2, book3, book4, book5]
for book in my_books:
    book.info()


class SchoolBooks(Book):
    has_tasks = True

    def __init__(self, title, author, number_of_pages, isbn, is_reserved, subject, group):
        super().__init__(title, author, number_of_pages, isbn, is_reserved)
        self.subject = subject
        self.group = group

    def info(self):
        inform = (f''
                  f'Название: {self.title}, Автор: {self.author}, страниц: {self.number_of_pages}, '
                  f' предмет: {self.subject}, класс: {self.group}'
                  )
        if self.is_reserved:
            print(inform + ', зарезервирована')
        else:
            print(inform)


school_book1 = SchoolBooks(
    'Алгебра', 'Иванов', 500, 111, False, 'Математика', 9
)
school_book2 = SchoolBooks(
    'Геометрия', 'Петров', 400, 124, False, 'Математика', 8
)
school_book3 = SchoolBooks(
    'География', 'Сидоров', 550, 122, False, 'География', 5
)
school_book2.reserve()

my_school_books = [school_book1, school_book2, school_book3]
for school_book in my_school_books:
    school_book.info()
