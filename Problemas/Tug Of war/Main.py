
minDif = 9999999

def solver(teamA, teamB, S):
    n = len(teamA)
    memo = [[0] * (len(teamA) + 1) for _ in range(n + 1)]
    memo[0] = [teamA[x] for x in range(0, len(teamA))]
    memo[0].insert(0,0)
    print(memo)
        
    for i in range(1, n + 1):
        for w in range(S + 1):
            if teamA[i - 1] <= w:
                # Either take the item or leave it
                memo[i][w] = max(memo[i - 1][w], teamB[i - 1] + memo[i - 1][w - teamA[i - 1]])
            else:
                memo[i][w] = memo[i - 1][w]

    return memo[n][S]

def fun(n):
    people = [0]*n
    for x in range(0, n):
        people[x] = int(input())
        print(people[x])
        
    people.sort()
    
    solver(people, [], len(people) // 2)

def main():
    try:
        cases = int(input())
        for _ in range(0, cases):
            input() #Blank
            fun(int(input()))
            
    except EOFError:
        pass
    
if __name__ == "__main__":
    main()
    
    # python p0001.py <1.in> 1.out
    # escripe en 1.out con print