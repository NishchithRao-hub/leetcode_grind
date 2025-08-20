class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R, D = deque(), deque()
        n = len(senate)

        for idx, team in enumerate(senate):
            if team == 'R':
                R.append(idx)
            else:
                D.append(idx)

        while R and D:
            Rturn = R.popleft()
            Dturn = D.popleft()

            if Rturn < Dturn:
                R.append(Rturn + n)
            else:
                D.append(Dturn + n)

        return "Radiant" if R else "Dire"

# Time -> O(n)
# Space -> O(n)
        
