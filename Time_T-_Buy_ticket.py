class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        while any(tickets):
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    time += 1
                    if i == k and tickets[i] == 0:
                        return time
        return time
