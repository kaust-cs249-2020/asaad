#  5.6 The Manhattan Tourist Problem Revisited 

def ManhattanTourist(n, m, Down, Right):
    '''
    :params n: integer n
    :params m: integer m
    :params Down: path cost matrix of downward edges
    :params Right: path cost matrix of rightward edges
    :return: length of the longest path
    '''
    s = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1, n + 1):
        s[i][0] = s[i-1][0] + int(Down[i-1][0])
    for j in range(1, m + 1):
        s[0][j] = s[0][j-1] + int(Right[0][j-1])
    for i in range(1, n+1):
        for j in range(1, m+1):
            s[i][j] = max(s[i-1][j] + int(Down[i-1][j]), s[i][j-1] + int(Right[i][j-1]))
    return s[n][m]

if __name__ == "__main__":
    with open("Ch5/Ex2input.txt") as dataset:
        dims = dataset.readline().strip().split(" ")
        inputtext = dataset.read().split("-")
    n, m = [int(x) for x in dims]
    Down = [x.split(" ") for x in inputtext[0].strip().split("\n")]
    Right = [x.split(" ") for x in inputtext[1].strip().split("\n")]
    print(ManhattanTourist(n, m, Down, Right))

    