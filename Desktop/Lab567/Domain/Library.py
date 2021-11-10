def create_the_book(id, title, category, price, discount):
    """
    With this function we create a book
    :param id: string
    :param title: string
    :param category: string
    :param price: float
    :param discount: string
    :return: the book, dictionary type
    """
    return {
        'id': id,
        'title': title,
        'category': category,
        'price': price,
        'discount': discount
    }


def get_id(book):
    """
    Getter for the book id
    :param book: dictionary
    :return: the book id
    """
    return book['id']


def get_title(book):
    """
    Getter for the book title
    :param book: dictionary
    :return: the book title
    """
    return book['title']


def get_category(book):
    """
    Getter for the book category
    :param book: dictionary
    :return: the book category
    """
    return book['category']


def get_price(book):
    """
    Getter for the book price
    :param book: dictionary
    :return: the book price
    """
    return book['price']


def get_discount(book):
    """
    Getter for the book discount
    :param book: dictionary
    :return: the book discount
    """
    return book['discount']


def to_string(book):
    """
    With this function we convert a dictionary into a string, for a better representation
    :param book: dictionary
    :return: string
    """
    return "id: {}, title: {}, category: {}, price: {}, discount: {}".format(
        get_id(book),
        get_title(book),
        get_category(book),
        get_price(book),
        get_discount(book)
    )
