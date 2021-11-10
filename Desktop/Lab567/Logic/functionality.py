from Domain.Library import get_discount, get_price, get_id, get_title, get_category, create_the_book
from Logic.CRUD import get_by_category


def apply_the_discount(lst):
    """
    With this function we create a discount for every silver/gold book
    :param lst: list
    :return: the updated prices
    """
    if len(lst) < 1:
        raise ValueError("Introduce a book, firstly!")
    new_list = []
    for book in lst:
        if get_discount(book) == "silver":
            id = get_id(book)
            title = get_title(book)
            category = get_category(book)
            price = get_price(book) - get_price(book) / 20
            discount = get_discount(book)

            new_book = create_the_book(id, title, category, price, discount)
            new_list.append(new_book)
        elif get_discount(book) == "gold":
            id = get_id(book)
            title = get_title(book)
            category = get_category(book)
            price = get_price(book) - get_price(book) / 10
            discount = get_discount(book)

            new_book = create_the_book(id, title, category, price, discount)
            new_list.append(new_book)
        else:
            new_list.append(book)

    return new_list


def determine_all_categories(lst):
    """
    With this function we determine all the categories
    :param lst: list
    :return: a list of all categories
    """
    lst2 = []  # in this list we put all categories
    for book in lst:
        lst2.append(get_category(book))
    result = []  # in this list we eliminate all duplicates from lst2
    for category in lst2:
        if category not in result:
            result.append(category)
    return result  # our final list of categories


def determine_the_minimum_price_for_each_category(lst):
    """
    With this function we determine the minimum price for each category
    :param lst: list
    :return: a list of minimum prices for each category
    """
    lst_of_minimum_price = []
    lst2 = determine_all_categories(lst)
    for category in lst2:
        lowest_price = get_price(get_by_category(category, lst))  # lowest price of each category
        for book in lst:
            if category == get_category(book) and get_price(book) < lowest_price:
                lowest_price = get_price(book)
        lst_of_minimum_price.append(lowest_price)
    return lst_of_minimum_price


def determine_titles_for_each_category(category, lst):
    """
    With this function we determine titles for category
    :param category: string
    :param lst: list
    :return: a list of titles for category
    """
    list_of_titles = []
    for book in lst:
        if get_category(book) == category:
            list_of_titles.append(get_title(book))
    return list_of_titles


def shows_the_number_of_distinct_titles(lst):
    """
    With this function we show the number of distinct titles for each category
    :param lst: list
    :return: the number of distinct titles for each category
    """
    lst2 = determine_all_categories(lst)
    the_list_of_numbers = []
    for category in lst2:
        list_of_titles_for_category = determine_titles_for_each_category(category, lst)
        a_set = set(list_of_titles_for_category)
        number_of_unique_elements = len(a_set)
        the_list_of_numbers.append(number_of_unique_elements)
    return the_list_of_numbers
