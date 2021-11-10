from Domain.Library import create_the_book, get_id, get_title, get_category, get_price, get_discount


def test_create_the_book():
    book = create_the_book("1", "Harap-Alb", "Stories", 15, "Silver")
    assert get_id(book) == "1"
    assert get_title(book) == "Harap-Alb"
    assert get_category(book) == "Stories"
    assert get_price(book) == 15
    assert get_discount(book) == "Silver"
