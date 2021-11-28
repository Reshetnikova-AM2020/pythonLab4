class Books():
    listBooks = list()

    def __init__(self, author, title, publisher, year, price, in_sale):
        self.addbook(author, title, publisher, year, price, in_sale)

    def addbook(self, author, title, publisher, year, price, in_sale):
        book = dict()
        book.update({
            "author": author,
            "title": title,
            "publisher": publisher,
            "year": year,
            "price": price,
            "in_sale": in_sale})
        self.listBooks.append(book)

    def print_book(self, index):
        print(self.listBooks[index].get("title"))

    def find(self, title, author):
        findex = -1
        for index in range(0, len(self.listBooks)):
            if str(self.listBooks[index].get("title")) == str(title) and str(
                    self.listBooks[index].get("author")) == str(author):
                print(self.listBooks[index].get("price"))
                findex = index
        print("Номер книги", findex)
        if findex == -1:
            print("Введите информацию по книге: ")
            author = input("Автор: ")
            title = input("Название: ")
            publisher = input("Издательство: ")
            year = input("Год: ")
            price = input("Цена: ")
            self.addbook(author, title, publisher, year, price, False)
        for index in range(0, len(self.listBooks)):
            self.print_book(index)


def main():
    myBook = Books("Азимов", "Мир после войны", "Издательство", 1975, 1025, True)
    myBook.addbook("Пелевин", "Книга Пелевина", "Издательство1", 1980, 1500, True)
    myBook.addbook("Пелевин1", "Книга Пелевина1", "Издательство1", 1980, 1800, True)
    myBook.addbook("Пелевин2", "Книга Пелевина2", "Издательство1", 1980, 1400, True)
    myBook.addbook("Пелевин3", "Книга Пелевина3", "Издательство1", 1980, 1300, True)

    for index in range(0, len(myBook.listBooks)):
        myBook.print_book(index)

    myBook.find("Книга Пелевина1", "Пелевин")


main()
