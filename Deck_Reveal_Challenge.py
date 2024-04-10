class Solution:
    def deckRevealedIncreasing(self, deck):
        deck.sort()
        result = []
        for card in reversed(deck):
            if result:
                result.insert(0, result.pop())
            result.insert(0, card)
        return result
