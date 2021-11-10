from Tests.test_CRUD import test_add_a_new_book_to_the_library, test_delete_a_book_from_the_library, \
    test_modify_the_book, test_modify_category_for_a_given_title, test_ordering_books_in_ascending_order_by_price
from Tests.test_Library import test_create_the_book
from Tests.test_functionality import test_apply_the_discount, test_determine_all_categories, \
    test_determine_the_minimum_price_for_each_category, test_determine_titles_for_each_category, \
    test_shows_the_number_of_distinct_titles


def test_All():
    test_add_a_new_book_to_the_library()
    test_delete_a_book_from_the_library()
    test_modify_the_book()
    test_create_the_book()
    test_apply_the_discount()
    test_modify_category_for_a_given_title()
    test_determine_all_categories()
    test_determine_the_minimum_price_for_each_category()
    test_ordering_books_in_ascending_order_by_price()
    test_determine_titles_for_each_category()
    test_shows_the_number_of_distinct_titles()