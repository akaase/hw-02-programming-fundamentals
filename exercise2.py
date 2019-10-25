# 1
meal_cost = 55
tip_percentage = 0.20
tip_amount = meal_cost * tip_percentage
print(tip_amount)

# 2
print('$' + str(tip_amount))
# or alternatively (Doesn't need type conversion in this case):
print(f'${tip_amount}')

# 3
print(f'The result of the multiplication is { 45628 * 7839 }')

# 4
my_str = 'Hello'
my_int = 5
print(my_str + str(my_int))

# 5
# (10 < 20 and 30 < 20) or not (10 == 11)
# ==> (True and False) or not (False)
# ==> (False) or True
# ==> True
print((10 < 20 and 30 < 20) or not (10 == 11))
