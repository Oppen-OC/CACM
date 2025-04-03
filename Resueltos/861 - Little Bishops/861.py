import sys

class Solver:
    def __init__(self):
        self.N = 9
        self.black_ = [[0] * self.N for _ in range(self.N)]
        self.white_ = [[0] * self.N for _ in range(self.N)]
        self.n_new_black_ = [0] * self.N
        self.n_new_white_ = [0] * self.N
        self.Init()

    def Init(self):
        for i in range(self.N):
            self.black_[i][0] = self.white_[i][0] = 1  

        for i in range(1, self.N):
            self.n_new_black_[i] = i if i % 2 else self.n_new_black_[i - 1]
            self.n_new_white_[i] = i if i % 2 == 0 else self.n_new_white_[i - 1]

        for i in range(1, self.N):
            for j in range(1, i + 1):
                j_ = j - 1
                self.black_[i][j] = self.black_[i - 1][j] + self.black_[i - 1][j_] * (self.n_new_black_[i] - j_)
                self.white_[i][j] = self.white_[i - 1][j] + self.white_[i - 1][j_] * (self.n_new_white_[i] - j_)

    def Run(self, n, k):
        if k > 2 * n - 1:
            return 0
        return sum(self.black_[n][j] * self.white_[n][k - j] for j in range(k + 1) if j <= n and k - j <= n)


solver = Solver()

for line in sys.stdin:
    n, k = map(int, line.split())
    if n == 0 and k == 0:
        break
    print(solver.Run(n, k))
