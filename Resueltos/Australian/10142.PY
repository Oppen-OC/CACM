import collections
import sys

def getWinner(voters, n):
    losers = set()
    currentVotes = [0] * (n + 1)

    while True:
        currentVotes = [0] * (n + 1)

        for voter in voters:
            for choice in voter:
                if choice not in losers:
                    currentVotes[choice] += 1
                    break  # solo el primer voto 

        currMax, maxP = -1, []
        currMin, minP = float('inf'), []

        for i in range(1, n + 1):
            if i not in losers:
                votes = currentVotes[i]

                if votes > currMax:
                    currMax, maxP = votes, [i]
                elif votes == currMax:
                    maxP.append(i)

                if votes < currMin:
                    currMin, minP = votes, [i]
                elif votes == currMin:
                    minP.append(i)

        if currMax > sum(currentVotes) / 2:
            return maxP

        if currMax == currMin:
            return maxP

        for p in minP:
            losers.add(p)

numOfTests = int(sys.stdin.readline().strip())
sys.stdin.readline()  # línea en blanco

for _ in range(numOfTests):
    n = int(sys.stdin.readline().strip())
    names = [sys.stdin.readline().strip() for _ in range(n)]

    voters = []
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        voters.append(list(map(int, line.split())))

    winners = getWinner(voters, n)
    print('\n'.join(names[e - 1] for e in winners))
    if _ < numOfTests - 1:
        print()  # línea en blanco entre casos
