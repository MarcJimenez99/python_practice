def maxProfit(prices):
    if len(prices) < 2:
            return 0
    dictionary = {}
    for i in range (0, len(prices)-1, 1):
        purchase_pt = prices[i] * -1
        profit = purchase_pt + prices[i+1]
        for j in range (i+1, len(prices), 1):
            if (purchase_pt + prices[j]) > profit:
                profit = purchase_pt + prices[j]
        if prices[i] in dictionary:
            if dictionary[prices[i]] < profit:
                dictionary[prices[i]] = profit
        else:
            dictionary[prices[i]] = profit
    print(prices)
    print(dictionary)
    if max(dictionary.values()) < 0:
        return 0
    else:
        return max(dictionary.values())

def better(prices):
    if len(prices) < 2:
            return 0
    i = 0
    # min price
    j = 1
    # max profit at min price
    profit = 0
    while j < len(prices):
        if (prices[i] > prices[j]):
            i += 1
            j += 1
        else:
            if (prices[j] - prices[i]) > profit:
                profit = prices[j] - prices[i]
            j += 1
    return profit
def main():
    prices = [7,1,5,3,6,4]
    
    result = better(prices)

    print (result)

if __name__ == "__main__":
    main()