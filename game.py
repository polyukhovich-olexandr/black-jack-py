from random import shuffle


class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def card_value(self):
        """Повертає кількість очок, що дає карта"""
        if self.rank in "TJQK":
            # По 10 за десятку, валета, даму та короля
            return 10
        else:
            # Повертає потрібну кількість очок за будь-яку іншу картку
            # Туз спочатку дає одне очко.
            return " A23456789".index(self.rank)

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)


class Hand(object):
    def __init__(self, name):
        # Ім'я гравця
        self.name = name
        # Спочатку рука порожня
        self.cards = []

    def add_card(self, card):
        """Додає карту на руку"""
        self.cards.append(card)

    def get_value(self):
        """Метод отримання числа очок на руці"""
        result = 0
        # Кількість тузів на руці.
        aces = 0
        for card in self.cards:
            result += card.card_value()
            # Якщо на руці є туз - збільшуємо кількість тузів
            if card.get_rank() == "A":
                aces += 1
        # Вирішуємо рахувати тузи за 1 очко або за 11
        if result + aces * 10 <= 21:
            result += aces * 10
        return result

    def __str__(self):
        text = "%s's contains:\n" % self.name
        for card in self.cards:
            text += str(card) + " "
        text += "\nHand value: " + str(self.get_value())
        return text


class Deck(object):
    def __init__(self):
        # Ранги
        ranks = "23456789TJQKA"
        # Масті
        suits = "DCHS"
        # Генератор списків, що створює колоду з 52 карт.
        self.cards = [Card(r, s) for r in ranks for s in suits]
        # Перетасовуємо колоду. Не забудьте імпортувати функцію shuffle із модуля random
        shuffle(self.cards)

    def deal_card(self):
        """Функция сдачи карты"""
        return self.cards.pop()
