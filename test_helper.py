import datetime
import helper


def test_add():
    helper.items.clear()
    text = "Lorem ipsum"
    date = "2023-09-02"

    helper.add(text, date)

    item = helper.items[-1]
    assert isinstance(item.date, datetime.date)


def test_sort():
    helper.items.clear()
    todos = [
        ("Universum debuggen", "2023-09-06"),
        ("Sinn des Lebens entdecken", "2023-09-01"),
        ("Superheld werden", "2023-10-25"),
        ("Netto null", "2050-01-01"),
    ]

    for todo in todos:
        helper.add(todo[0], todo[1])

    for i in range(len(helper.items) - 1):
        assert helper.items[i].date < helper.items[i + 1].date


def test_category():
    helper.items.clear()
    todos = [
        ("Kabelsalat auflösen", "Hausarbeit"),
        ("Wäsche machen", "Hausarbeit"),
        ("Trash Core-Album aufnehmen", "Kunst"),
        ("Französisch lernen", "Hausaufgaben"),
    ]

    for todo in todos:
        helper.add(todo[0], category=todo[1])

    for item in helper.items:
        assert item.category in [t[1] for t in todos]


def test_description():
    helper.items.clear()
    todos = [
        (
            "Zeitmaschine bauen",
            "Vergangenheit kompilieren, Gegenwart laufen lassen, Zukunft debuggen",
        ),
        (
            "AI-Nebenprojekt",
            "Eine unglaublich nervige AI trainieren, die den Benutzer nur veräppelt",
        ),
    ]

    for todo in todos:
        helper.add(todo[0], description=todo[1])

    for item in helper.items:
        assert item.description is not None
        assert item.description != ""
