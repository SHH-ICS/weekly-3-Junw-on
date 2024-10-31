size = input('large   extra large: ')
if size == "large":
    pizzasize = 6.00
elif size == "extra large":
    pizzasize = 10.00
else:
    print("Invalid pizza size entered. Please choose 'large' or 'extra large'.")

toppings = int(input('1   2   3   4: '))
if toppings == 1:
    toppingsprice = 1.00
elif toppings == 2:
    toppingsprice = 1.75
elif toppings == 3:
    toppingsprice = 2.50
elif toppings == 4:
    toppingsprice = 3.35
else:
    print("Invalid number of toppings entered. Please choose 1, 2, 3, or 4.")

hst = 0.13
subtotal = pizzasize + toppingsprice
tax = subtotal * hst
total = subtotal + tax

print(subtotal)
print(tax)
print(total)
