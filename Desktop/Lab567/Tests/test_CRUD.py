from Domain.Library import get_id, get_title, get_category, get_price, get_discount
from Logic.CRUD import add_a_new_book_to_the_library, get_by_id, delete_a_book_from_the_library, modify_the_book, \
    modify_category_for_a_given_title, ordering_books_in_ascending_order_by_price


def test_add_a_new_book_to_the_library():
    lst = []
    lst = add_a_new_book_to_the_library("1", "The Little Prince", "short story", 25, "Gold", lst)

    assert len(lst) == 1
    assert get_id(get_by_id("1", lst)) == "1"
    assert get_title(get_by_id("1", lst)) == "The Little Prince"
    assert get_category(get_by_id("1", lst)) == "short story"
    assert get_price(get_by_id("1", lst)) == 25
    assert get_discount(get_by_id("1", lst)) == "Gold"


def test_delete_a_book_from_the_library():
    lst = []
    lst = add_a_new_book_to_the_library("1", "The Little Prince", "short story", 25, "Gold", lst)
    lst = add_a_new_book_to_the_library("2", "Don Quixote", "romance", 20, "None", lst)

    lst = delete_a_book_from_the_library("1", lst)

    assert len(lst) == 1
    assert get_by_id("1", lst) is None
    assert get_by_id("2", lst) is not None


def test_modify_the_book():
    lst = []
    lst = add_a_new_book_to_the_library("1", "The Little Prince", "short story", 25, "Gold", lst)
    lst = add_a_new_book_to_the_library("2", "Don Quixote", "romance", 20, "None", lst)

    lst = modify_the_book("1", "A Tale of Two Cities", "short story", 35, "Silver", lst)

    assert get_id(get_by_id("1", lst)) == "1"
    assert get_title(get_by_id("1", lst)) == "A Tale of Two Cities"
    assert get_category(get_by_id("1", lst)) == "short story"
    assert get_price(get_by_id("1", lst)) == 35
    assert get_discount(get_by_id("1", lst)) == "Silver"


def test_modify_category_for_a_given_title():
    lst = []
    lst = add_a_new_book_to_the_library("1", "The Little Prince", "short story", 25, "Gold", lst)
    lst = add_a_new_book_to_the_library("2", "Don Quixote", "romance", 20, "None", lst)

    lst = modify_category_for_a_given_title("The Little Prince", "long story", lst)
    lst = modify_category_for_a_given_title("Don Quixote", "adventure", lst)

    assert get_category(get_by_id("1", lst)) == "long story"
    assert get_category(get_by_id("2", lst)) == "adventure"


def test_ordering_books_in_ascending_order_by_price():
    lst = []
    lst = add_a_new_book_to_the_library("1", "The Little Prince", "short story", 25, "Gold", lst)
    lst = add_a_new_book_to_the_library("2", "Don Quixote", "romance", 20, "None", lst)
    lst = add_a_new_book_to_the_library("3", "Messi", "biography", 70, "silver", lst)

    lst = ordering_books_in_ascending_order_by_price(lst)

    assert get_id(lst[0]) == "2"
    assert get_title(lst[0]) == "Don Quixote"
    assert get_id(lst[1]) == "1"
    assert get_id(lst[2]) == "3"