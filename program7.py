def lemonade_change(bills):
    five_dollars = 0
    ten_dollars = 0
    
    for bill in bills:
        if bill == 5:
            five_dollars += 1
        elif bill == 10:
            if five_dollars > 0:
                five_dollars -= 1
                ten_dollars += 1
            else:
                return False
        elif bill == 20:
            if ten_dollars > 0 and five_dollars > 0:
                ten_dollars -= 1
                five_dollars -= 1
            elif five_dollars >= 3:
                five_dollars -= 3
            else:
                return False
    
    return True

# Example usage
if __name__ == "__main__":
    bills = [5, 5, 5, 10, 20]
    result = lemonade_change(bills)
    print("Can provide correct change:", result)
