import random

def value(hand): #assume hand is a list of numbers
    if 11 in hand and sum(hand) > 21:
        total = sum(hand)

        for _ in range(hand.count(11)):
            total = total - 10
            if total < 21:
                return total
        return total
    else:
        return sum(hand)
def simulate2PlayerOpeningHands(trials):
    results = {}
    for _ in range(trials):
        deck = createDeck()
        random.shuffle(deck)
        playerHand = []
        dealerHand = []
        for _ in range(2):
            playerHand = playerHand.append(deck.pop())
            dealerHand = dealerHand.append(deck.pop())
        playerScore = value(playerHand)
        dealerScore = value(dealerHand)

        if playerScore not in results:
            results[playerScore] = 1
        else:
            results[playerScore] = results[playerScore] + 1

        if dealerScore not in results:
            results[dealerScore] = 1
        else:
            results[dealerScore] = results[dealerScore] + 1

    for score in results:
        results[value] = results[value]/trials
    return results


def simulate2PlayerBothHold(trials):
    wins = 0
    results = {}
    for _ in range(trials):
        deck = createDeck()
        random.shuffle(deck)
        playerHand = []
        dealerHand = []
        for _ in range(2):
            playerHand = playerHand.append(deck.pop())
            dealerHand = dealerHand.append(deck.pop())
        playerScore = value(playerHand)
        dealerScore = value(dealerHand)
#missing some code
    return wins
def createDeck():
    deck = []
    for value in range(2, 11):
        deck = deck + [value]*4

    deck = deck+ [10]*12 + [11]*4
    return deck

deck = createDeck()
random.shuffle(deck)
print(deck)
print(len(deck))

def printDictionaryInOrder(dictionary):
    for key in sorted(dictionary.keys()):
        print(key, dictionary[key])

results = simulate2PlayerOpeningHands(100000)
print(printDictionaryInOrder(results))

