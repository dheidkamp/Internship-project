# Sum and multiplication of even and odd numbers.

def sum_even_and_product_odd(arr: list):
    sum_even = 0
    product_odd = 1

    for num in arr:
        if num % 2 == 0:
            sum_even += num

        else:
            product_odd *= num
    return [sum_even, product_odd]


print(sum_even_and_product_odd([1, 2, 3, 4, 5, 6, 7, 8]))


# Sum between range values


def sum_between_range(arr: list, min_val: int, max_val: int):
    sum_val = 0

    for val in arr1:
        if val >= min_val and val <= max_val:
            sum_val += val
    return sum_val


min_val = 1
max_val = 3
arr1 = [3, 2, 1, 4, 10, 8, 7, 6, 9, 5]
print(sum_between_range(arr1, min_val, max_val))
#


# Stock price 2
def buy_and_sell_stock(prices: list):
    profit = 0

    for i in range(len(prices) -1):
        if prices[i +1] - prices[i] > 0:
            profit += prices[i +1] - prices[i]

    return profit


test_prices = [7, 1, 5, 3, 6, 4]
print(buy_and_sell_stock(test_prices))

def plus_one(arr: list):
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):

        if arr[i] != 10:
            break
        else:
            arr[i]= 0
            arr[i-1] += 1

    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)

    return arr


test_data = [1, 9, 9]
print(plus_one(test_data))