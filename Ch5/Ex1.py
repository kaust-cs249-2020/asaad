# 5.5 An Introduction to Dynamic Programming: The Change Problem
def DPChange(money, coins):
    '''
    :params money: amount of money to be returned, an integer
    :params coins: a list of available coin denomination, a list of integers
    :return: number of coins to be returned
    '''
    MinNumCoins = [0]
    for m in range(1, money+1):
        MinNumCoins.append(10000000000)
        for coin in coins:
            if m >= coin:
                if MinNumCoins[m - coin] + 1 < MinNumCoins[m]:
                    MinNumCoins[m] = MinNumCoins[m - coin] + 1
    return MinNumCoins[money]

if __name__=="__main__":
    money = 100000000
    coins = [15, 5, 3, 1]
    print(DPChange(money, coins))
