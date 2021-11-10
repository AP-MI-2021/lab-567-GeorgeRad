from Domain.Library import to_string
from Logic.CRUD import add_a_new_book_to_the_library, delete_a_book_from_the_library, modify_the_book, \
    modify_category_for_a_given_title, ordering_books_in_ascending_order_by_price, get_by_id
from Logic.functionality import apply_the_discount, determine_all_categories, \
    determine_the_minimum_price_for_each_category, shows_the_number_of_distinct_titles


def menu():
    print("1. Add a new book to the library")
    print("2. Delete a book from library")
    print("3. Modify a book from library")
    print("4. Applying a 5% discount for all silver discounts and 10% for all gold discounts")
    print("5. Modify the category for a given title")
    print("6. Determine the minimum price for each category")
    print("7. Order books in ascending order by price")
    print("8. Shows the number of distinct titles for each category")
    print("u. Undo")
    print("r. Redo")
    print("a. Show the library")
    print("x. Out")


def add_the_book_ui(lst, undo_list, redo_list):
    """
    With this function we add a new book to the lst
    :param redo_list:
    :param undo_list:
    :param lst: list
    :return: the new list
    """
    try:
        id = input("Give the new id: ")
        if get_by_id(id, lst) is not None:
            raise ValueError("This id already exists in the list!")
        title = input("Give the new title: ")
        category = input("Give the new category: ")
        price = float(input("Give the new price: "))
        discount = input("Give the new discount: ")
        if discount != "silver" and discount != "gold":
            raise ValueError("The given discount is incorrect!")
        final_list = add_a_new_book_to_the_library(id, title, category, price, discount, lst)
        undo_list.append(lst)
        redo_list.clear()

        return final_list
    except ValueError as ve:
        print("Error {}".format(ve))
        return lst


def delete_a_book_ui(lst, undo_list, redo_list):
    """
    With this function we delete a book from lst
    :param redo_list:
    :param undo_list:
    :param lst: list
    :return: the new list
    """
    try:
        id = input("Give the id you want to delete: ")
        if get_by_id(id, lst) is None:
            raise ValueError("This id already exists in the list!")
        final_list = delete_a_book_from_the_library(id, lst)
        undo_list.append(lst)
        redo_list.clear()
        return final_list
    except ValueError as ve:
        print("Error {}".format(ve))


def modify_a_book_ui(lst, undo_list, redo_list):
    """
    With this function we modify a book from lst
    :param undo_list:
    :param redo_list:
    :param lst: list
    :return: the new list
    """
    try:
        id = input("Give the id: ")
        if get_by_id(id, lst):
            raise ValueError("This id already exists in the list!")
        title = input("Give the new title: ")
        category = input("Give the new category: ")
        price = float(input("Give the new price: "))
        discount = input("Give the new discount: ")
        final_list = modify_the_book(id, title, category, price, discount, lst)
        undo_list.append(lst)
        redo_list.clear()

        return final_list
    except ValueError as ve:
        print("Error {}".format(ve))


def apply_discount_ui(lst, undo_list, redo_list):
    undo_list.append(lst)
    redo_list.clear()
    return apply_the_discount(lst)


def modify_category_for_a_given_title_ui(lst):
    """
    We use this function to make an interaction with the user of the program, for "modify_category_for_a_given_title"
    :param lst: list
    :return: the new list
    """
    title = input("Give the title of the book whose category you want to change: ")
    category = input("Give the new category: ")

    lst = modify_category_for_a_given_title(title, category, lst)

    return lst


def show_the_minimum_price(list_of_categories, list_of_minimum_prices):
    """
    With this function we determine the minimum price for each category and show it
    :param list_of_categories: a list of categories
    :param list_of_minimum_prices: a list of minimum prices
    :return: a representation of the minimum prices
    """
    for i in range(len(list_of_categories)):
        print(list_of_categories[i], list_of_minimum_prices[i])


def show_the_number_of_title_for_each_category(lst):
    """
    With this function we show the number of titles for each category
    :param lst: a list
    :return: a representation of each number of distinct categories
    """
    list_of_categories = determine_all_categories(lst)
    list_of_numbers = shows_the_number_of_distinct_titles(lst)
    for i in range(len(list_of_categories)):
        print(list_of_categories[i], list_of_numbers[i])


def show_all(lst):
    """
    With this function we will show all the books from the library
    :param lst: list
    :return: the list
    """
    for book in lst:
        print(to_string(book))


def run_ui():
    lst = []
    menu()
    option = input("Give the option: ")
    undo_list = []
    redo_list = []
    while True:
        if option == "1":
            lst = add_the_book_ui(lst, undo_list, redo_list)
        elif option == "2":
            lst = delete_a_book_ui(lst, undo_list, redo_list)
        elif option == "3":
            lst = modify_a_book_ui(lst, undo_list, redo_list)
        elif option == "4":
            lst = apply_discount_ui(lst, undo_list, redo_list)
        elif option == "5":
            lst = modify_category_for_a_given_title_ui(lst)
        elif option == "6":
            list_of_categories = determine_all_categories(lst)
            list_of_minimum_prices = determine_the_minimum_price_for_each_category(lst)
            show_the_minimum_price(list_of_categories, list_of_minimum_prices)
        elif option == "7":
            lst = ordering_books_in_ascending_order_by_price(lst)
        elif option == "8":
            show_the_number_of_title_for_each_category(lst)
        elif option == "u":
            if len(undo_list) > 0:
                redo_list.append(lst)
                lst = undo_list.pop()
                print(lst)
            else:
                print("We can not do undo!")
        elif option == "r":
            if len(redo_list) > 0:
                undo_list.append(lst)
                lst = redo_list.pop()
                print(lst)
            else:
                print("We can not do redo!")
        elif option == "a":
            show_all(lst)
        elif option == "x":
            break
        else:
            print("Incorrect option! Please retry!")
        menu()
        option = input("Give the option: ")
