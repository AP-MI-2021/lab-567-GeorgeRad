from Domain.Library import get_price
from Logic.CRUD import add_a_new_book_to_the_library, get_by_id
from Logic.functionality import apply_the_discount, determine_all_categories, \
    determine_the_minimum_price_for_each_category, determine_titles_for_each_category, \
    shows_the_number_of_distinct_titles


def test_apply_the_discount():
    lst = []
    lst = add_a_new_book_to_the_library("1", "The Little Prince", "short story", 20, "gold", lst)
    lst = add_a_new_book_to_the_library("2", "Don Quixote", "romance", 20, "silver", lst)

    lst = apply_the_discount(lst)

    assert get_price(get_by_id("1", lst)) == 18
    assert get_price(get_by_id("2", lst)) == 19


def test_determine_all_categories():
    lst = []
    lst = add_a_new_book_to_the_library("1", "The Little Prince", "short story", 20, "gold", lst)
    lst = add_a_new_book_to_the_library("2", "Don Quixote", "romance", 20, "silver", lst)

    lst2 = determine_all_categories(lst)

    assert len(lst2) == 2
    assert lst2[0] == "short story"
    assert lst2[1] == "romance"


def test_determine_the_minimum_price_for_each_category():
    lst = []
    lst = add_a_new_book_to_the_library("1", "The Little Prince", "short story", 15, "gold", lst)
    lst = add_a_new_book_to_the_library("2", "Don Quixote", "short story", 20, "silver", lst)
    lst = add_a_new_book_to_the_library("3", "Leo Messi", "biography", 10, "gold", lst)
    lst = add_a_new_book_to_the_library("4", "Maria", "biography", 8, "None", lst)

    lst2 = determine_the_minimum_price_for_each_category(lst)

    assert len(lst2) == 2
    assert lst2[0] == 15
    assert lst2[1] == 8


def test_determine_titles_for_each_category():
    lst = []
    lst = add_a_new_book_to_the_library("1", "The Little Prince", "short story", 15, "gold", lst)
    lst = add_a_new_book_to_the_library("2", "Don Quixote", "short story", 20, "silver", lst)
    lst = add_a_new_book_to_the_library("3", "Leo Messi", "biography", 10, "gold", lst)
    lst = add_a_new_book_to_the_library("4", "Maria", "biography", 8, "None", lst)

    lst2 = determine_titles_for_each_category("short story", lst)

    assert len(lst2) == 2
    assert lst2[0] == "The Little Prince"
    assert lst2[1] == "Don Quixote"


def test_shows_the_number_of_distinct_titles():
    lst = []
    lst = add_a_new_book_to_the_library("1", "The Little Prince", "short story", 15, "gold", lst)
    lst = add_a_new_book_to_the_library("2", "Don Quixote", "short story", 20, "silver", lst)
    lst = add_a_new_book_to_the_library("3", "Leo Messi", "biography", 10, "gold", lst)
    lst = add_a_new_book_to_the_library("4", "Maria", "biography", 8, "None", lst)

    lst2 = shows_the_number_of_distinct_titles(lst)

    assert len(lst2) == 2
    assert lst2[0] == 2
    assert lst2[1] == 2
