# Sliding Window Algorithm
# Optimized way to find the greatest difference between two points in
# a list or array subtracting right from left. Gets rid of the use
# of nested loops for a single loop by using two pointers. 
# 
# In this case since we need to find a sub range in the list of prices
# for this stock, we need to find the greatest number between two
# points in the list but as time moves linearly, the greater number must 
# exist later in the list, and the lower number must be in the beginning.
# So to find this, we have two pointers one left and one right, with left
# pointing to the first element in the list, and right pointing to the second.
# We look at both points and if the price at the left pointer is 
# less than the right pointer, we set the left pointer equal to the right
# pointer and the right pointer over by 1. If the value at the right pointer
# greater then we calculate the profit by subtracting prices[right] - prices[left].
# If this profit is greater than our set maxProfit variable than we 
# set this equal.  

def maxProfitStock(prices):
    leftPtr, rightPtr = 0, 1
    maxProfit = 0
    while rightPtr < len(prices):
        if prices[rightPtr] > prices[leftPtr]:
            currentProfit = prices[rightPtr] - prices[leftPtr]
            maxProfit = max(maxProfit, currentProfit)
        else:
            leftPtr = rightPtr
        rightPtr += 1
    return maxProfit

def main():
    prices = [6,2,8,33,67,3,6,21,100]
    print(f'Max Profit of the Stocks: {maxProfitStock(prices)}')

if __name__ == "__main__":
    main()