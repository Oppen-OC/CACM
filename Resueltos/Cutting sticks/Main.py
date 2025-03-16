import math

def min_cut_cost(l, cut_positions):
    cuts = [0] + cut_positions + [l]
    n = len(cuts)
    
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n):  # The length of the segment
        for i in range(n - length):
            j = i + length
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], (cuts[j] - cuts[i]) + dp[i][k] + dp[k][j])

    return dp[0][-1]


def main():
    try:
        while True:
            global cost
            cost = 0
            l = int(input())
            if l == 0:
                return
            
            n = int(input())
            c = list(map(int, input().strip().split()))

            
            print("The minimun cutting is:", min_cut_cost(l, c))
            
    except EOFError:
        pass
    
if __name__ == "__main__":
    main()
    
    # l = tamaño del palo, termina en caso de ser 0
    # n = número de cortes
    # c = array de posiciones donde se tienen que realizar los cortes

    # El output debe ser el coste minimo de realizar estos cortes

    # Estrategia: siempre realizar el corte mas al centro del tronco