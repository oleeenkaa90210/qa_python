import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2


    @pytest.mark.parametrize("book_name, expected_result", [
        ("Гордость и предубеждение", True),
        ("A" * 42, False),
        ("", False)
    ])
    def test_add_new_book(self, book_name, expected_result):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        result = book_name in collector.books_genre
        assert result == expected_result

    def test_set_book_genre_unknown_genre(self):
        collector = BooksCollector()
        book_name = 'Любовь и кошки'
        collector.add_new_book(book_name)

        unknown_genre = 'Мелодрама'
        collector.set_book_genre(book_name, unknown_genre)

        book_genre = collector.get_book_genre(book_name)

        assert book_genre == ''

    def test_set_books_genre_new_book(self):
        collector = BooksCollector()
        book_name = 'Картофельное пюре'
        collector.add_new_book(book_name)
        genre_name = 'Ужасы'
        collector.set_book_genre(book_name,genre_name)

        assert collector.get_book_genre(book_name) == genre_name


    def test_get_book_genre_non_existent_book(self):
        collector = BooksCollector()
        non_existent_book_name = 'Тыквенное пюре и цветы'
        genre = collector.get_book_genre(non_existent_book_name)

        assert genre is None

    def test_get_books_with_specific_genre_check_books_list(self):
        collector = BooksCollector()
        books_with_genres = [
            ('1', 'Ужасы'),
            ('2', 'Комедии'),
            ('3', 'Ужасы')
        ]
        for book, genre in books_with_genres:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        specific_genre = 'Ужасы'
        expected_books = ['1', '3']
        actual_books = collector.get_books_with_specific_genre(specific_genre)

        assert set(actual_books) == set(expected_books)

    def test_get_books_genre_with_specific_genre_check_genre_existent(self):
        collector = BooksCollector()

        expected_books_genre = {
            '1': 'Ужасы',
            '2': 'Комедии'
        }
        for book, genre in expected_books_genre.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        actual_books_genre = collector.get_books_genre()
        assert actual_books_genre == expected_books_genre

    def test_get_books_for_children_book_for_adults(self):
        collector = BooksCollector()
        books_with_genres = {
            'Колобок': 'Мультфильмы',
            'Астрал': 'Ужасы'
        }
        for book, genre in books_with_genres.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        books_for_children = collector.get_books_for_children()
        assert 'Астрал' not in books_for_children

    def test_add_book_in_favorites_one_book(self):
        collector = BooksCollector()
        book_name = 'Герой нашего времени'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)

        assert book_name in collector.favorites

    def test_add_book_in_favorites_twice(self):
        collector = BooksCollector()
        book_name = 'Герой'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)

        collector.add_book_in_favorites(book_name)

        assert collector.favorites.count(book_name) == 1

    def test_delete_book_from_favorites_one_book(self):
        collector = BooksCollector()
        book_name = 'Ева'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)

        assert book_name not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        books_name = ['Ева', 'Роман', 'Екатерина']

        for book in books_name:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)

        favorites_list = collector.get_list_of_favorites_books()
        assert set(books_name) == set(favorites_list)