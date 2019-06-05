from random import shuffle

class Card:
    suits = ["черви", "пики", "крести", "бубны"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "валета", "даму", "короля", "туза"]

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " " + self.suits[self.suit]
        return v

class Deck:
    def __init__(self):
        self.cards = []

        for i in range(2, 15):
            for j in range(0, 4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.wins = 0
        self.name = name

class Game:
    def __init__(self):
        name1 = input("Введите имя первого игрока: ")
        name2 = input("Введите имя второго игрока: ")
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        self.deck = Deck()
        self.play_game()

    def wins(self, winner):
        w = "{} забирает карты".format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} кладет {}, а {} кладет {}".format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("Поехали!")
        while len(cards) >= 2:
            response = input("Нажмите X для выхода. Нажмите любую другую клавишу для начала игры.")
            if response == "X":
                break
            p1n = self.p1.name
            p2n = self.p2.name
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)

        print("Игра окончена. {} выиграл!".format(win), " ", "Счет: ", " ",
              self.p1.wins, " ", self.p2.wins)

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p2.wins > p1.wins:
            return p2.name
        return "Ничья"

game = Game()
i = input("Вам понравилось?")