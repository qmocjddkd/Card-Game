import random 

cards = {"Шесть": 1, "Семь": 2, "Восемь": 3, "Девять": 4, "Десять": 5, "Валет": 6, "Дама": 7, "Король": 8, "Туз": 9}

class Create_Deck:
    def __init__(self):
        self.deck = [j for j in list(cards) for i in range(5)]
        random.shuffle(self.deck)  # shuffled the created deck

    def split_deck(self):
        d1 = []
        d2 = []
        d3 = []
        for x in range(12):
            d1.append(self.deck.pop())
            d2.append(self.deck.pop())
            d3.append(self.deck.pop())

        return d1, d2, d3


class Player:

    def __init__(self, name, deck):
        self.name = name
        self.deck = deck

    def draw(self): return self.deck.pop()

    def add_cards(self, added_cards):
        if isinstance(added_cards, list):
            self.deck.extend(added_cards)
        else:
            self.deck.append(added_cards)


def main():
    print("\t Добро пожаловать в 'Пъянницу'")
    print("\t Перемешаем, разделим и начнем!\n\n")
    play1, play2, play3 = Create_Deck().split_deck()
    p1 = Player("Игрок 1", play1)
    p2 = Player("Игрок 2", play2)
    p3 = Player("Игрок 3", play3)
    print(f"У {p1.name} игрока {len(p1.deck)} карт")
    print(f"У {p2.name} игрока {len(p2.deck)} карт")
    print(f"У {p3.name} игрока {len(p3.deck)} карт")
    gameover = False
    while not gameover:
        # списки с картами
        table = []
        
        if len(p1.deck) == 0:
            print("Игрок 1 пьянница!")
            gameover = 1
            break
        if len(p2.deck) == 0:
            print("Игрок 2 пьянница!")
            gameover = 1
            break
        if len(p3.deck) == 0:
            print("Игрок 3 пьянница!")
            gameover = 1
            break
        # взятие карт с собственной колоды и добавление в список
        table.extend([card1 := str(p1.draw()), card2 := str(p2.draw()), card3 := str(p3.draw())])
        print(f"Игрок 1: {card1}\nИгрок 2: {card2}\nИгрок 3: {card3}")

        # если у игроков одинаковые карты
        while card1 == card2 == card3 or card1 == card2 or card2 == card3 or card1 == card3:
            if len(p1.deck) < 3: print("Игрок 1 пьяница! Он залез в долги!"); gameover = 1; break
            if len(p2.deck) < 3: print("Игрок 2 пьяница! Он залез в долги!"); gameover = 1; break
            if len(p3.deck) < 3: print("Игрок 3 пьяница! Он залез в долги!"); gameover = 1; break

            if card1 == card2 == card3:
                print("У всех игроков одинаковые карты. Они переигрывают.")
                table.extend([str(p1.draw()), str(p2.draw()), str(p3.draw())])
                card1 = str(p1.draw())
                card2 = str(p2.draw())
                card3 = str(p3.draw())
                table.extend([card1, card2, card3])
                print(f"Новые карты: Игрок 1: {card1}, Игрок 2: {card2}, Игрок 3: {card3}")
            elif card1 == card2:
                print("Игрок 1 и Игрок 2 имеют одинаковые карты. Они переигрывают.")
                table.extend([str(p1.draw()), str(p2.draw())])
                card1 = str(p1.draw())
                card2 = str(p2.draw())
                table.extend([card1, card2])
                print(f"Новые карты: Игрок 1: {card1}, Игрок 2: {card2}")
            elif card2 == card3:
                print("Игрок 2 и Игрок 3 имеют одинаковые карты. Они переигрывают.")
                table.extend([str(p2.draw()), str(p3.draw())])
                card2 = str(p2.draw())
                card3 = str(p3.draw())
                table.extend([card2, card3])
                print(f"Новые карты: Игрок 2: {card2}, Игрок 3: {card3}")
            elif card1 == card3:
                print("Игрок 1 и Игрок 3 имеют одинаковые карты. Они переигрывают.")
                table.extend([str(p1.draw()), str(p3.draw())])
                card1 = str(p1.draw())
                card3 = str(p3.draw())
                table.extend([card1, card3])
                print(f"Новые карты: Игрок 1: {card1}, Игрок 3: {card3}")

        round_winner = max((card1, card2, card3), key=lambda c: cards[c])
        if round_winner == card1:
            p1.add_cards(table)
        elif round_winner == card2:
            p2.add_cards(table)
        else:
            p3.add_cards(table)

        print(f"У {p1.name} игрока {len(p1.deck)} карт")
        print(f"У {p2.name} игрока {len(p2.deck)} карт")
        print(f"У {p3.name} игрока {len(p3.deck)} карт")
    print("Игра завершена!")

if __name__ == "__main__":
    main()