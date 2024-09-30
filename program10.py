def min_coins(coins, amount):
    
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0 

    
    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage
if __name__ == "__main__":
    coins = [1, 2, 5]  # Coin denominations
    amount = 11        # Total amount
    result = min_coins(coins, amount)
    print("Minimum number of coins required:", result)
