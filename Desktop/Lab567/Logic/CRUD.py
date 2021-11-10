from Domain.Library import create_the_book, get_id, get_title, get_category, get_price, get_discount


def add_a_new_book_to_the_library(id, title, category, price, discount, lst):
    """
    With this function we add a new book to the library(lst)
    :param id: string
    :param title: string
    :param category: string
    :param price: float
    :param discount: string
    :param lst: list
    :return: the new list
    """
    if get_by_id(id, lst) is not None:
        raise ValueError("The id entered exists!")
    book = create_the_book(id, title, category, price, discount)
    return lst + [book]


def get_by_id(id, lst):
    """
    With this function we test if the id is in lst
    :param id: string
    :param lst: list
    :return: the book(if the id is in lst) or None(if the id is not in lst)
    """
    for book in lst:
        if get_id(book) == id:
            return book
    return None


def get_by_title(title, lst):
    """
    With this function we test if the title is in lst
    :param title: string
    :param lst: list
    :return: the book(if the title is in lst) or None(if the title is not in lst)
    """
    for book in lst:
        if get_title(book) == title:
            return book
    return None


def get_by_any_discount(lst):
    """
    With this function we test if the discount is in lst
    :param lst: list
    :return: the book(if the discount is in lst) or None(if the discount is not in lst)
    """
    for book in lst:
        if get_discount(book) == "silver" or get_discount(book) == "gold":
            return book
    return None


def get_by_price(price, lst):
    """
    With this function we test if price is in lst
    :param price: float
    :param lst: list
    :return: the book(if the price is in lst) or None(if the price is not in lst)
    """
    for book in lst:
        if get_price(book) == price:
            return book
    return None


def get_by_category(category, lst):
    """
    With this function we test if category is in lst
    :param category: string
    :param lst: list
    :return: the book(if the category is in lst) or None(if the category is not in lst)
    """
    for book in lst:
        if get_category(book) == category:
            return book
    return None


def delete_a_book_from_the_library(id, lst):
    """
    With this function we delete a book from lst
    :param id: string
    :param lst: list
    :return: the new list
    """
    if get_by_id(id, lst) is None:
        raise ValueError("The id entered does not exists!")
    return [book for book in lst if get_id(book) != id]


def modify_the_book(id, title, category, price, discount, lst):
    """
    With this function we modify the book from lst
    :param id: string
    :param title: string
    :param category: string
    :param price: float
    :param discount: string
    :param lst: list
    :return: the new list
    """
    try:
        new_list = []
        if get_by_id(id, lst) is None:
            raise ValueError("The id entered does not exists!")
        for book in lst:
            if get_id(book) == id:
                new_book = create_the_book(id, title, category, price, discount)
                new_list.append(new_book)
            else:
                new_list.append(book)
        return new_list
    except ValueError as ve:
        print("Error {}".format(ve))


def modify_category_for_a_given_title(title, category, lst):
    """
    With this function we modify the category of a book for a given title
    :param title: string
    :param category: string
    :param lst: list
    :return: the new list
    """
    try:
        new_list = []
        for book in lst:
            if get_title(book) == title:
                id = get_id(book)
                price = get_price(book)
                discount = get_discount(book)

                new_book = create_the_book(id, title, category, price, discount)
                new_list.append(new_book)
            else:
                new_list.append(book)
        return new_list
    except ValueError as ve:
        print("Error {}".format(ve))


def ordering_books_in_ascending_order_by_price(lst):
    """
    With this function we order books in ascending order by price
    :param lst: list of books
    :return: the new ordered list
    """
    length = len(lst)
    for i in range(length - 1):
        for j in range(i, length):
            if get_price(lst[j]) < get_price(lst[i]):
                lst[j], lst[i] = lst[i], lst[j]
    return lst