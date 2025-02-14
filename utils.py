from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
from datetime import datetime


def data_processing(kwargs: dict):
    current_date = datetime.now()
    first_cup = datetime.strptime(kwargs["first_cup"], "%Y-%m-%d")
    possible_cups = round(((int(current_date.year)) - int(first_cup.year)) / 4, 0)

    if kwargs["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")

    if int(first_cup.year) < 1930 or (int(first_cup.year) - 1930) % 4 != 0:
        raise InvalidYearCupError("there was no world cup this year")

    if kwargs["titles"] > possible_cups:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")