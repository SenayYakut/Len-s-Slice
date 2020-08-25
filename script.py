# to keep track what kind of pizza the store sells
toppings = ["pepperoni","pineapple","cheese","sausage",
"olives","anchovies","mushrooms"]

# to keep how much each kind of pizza slice costs
prices = [2,6,1,3,2,7,2]

num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) +  " different kinds of pizza!")

#List of pizzas with prices 
pizzas = list(zip(prices, toppings))

print(pizzas)

# pizzas from cheapest to most expensive
pizzas.sort()
# cheapest one
cheapest_pizza = pizzas[0]
# most expensive pizza
priciest_pizza = pizzas[-1]

#three cheapest
three_cheapest = pizzas[:3]
print(three_cheapest)

# number of 2 dollar pizzas
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)# to keep track what kind of pizza the store sells
toppings = ["pepperoni","pineapple","cheese","sausage",
"olives","anchovies","mushrooms"]

# to keep how much each kind of pizza slice costs
prices = [2,6,1,3,2,7,2]

num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) +  " different kinds of pizza!")

#List of pizzas with prices 
pizzas = list(zip(prices, toppings))

print(pizzas)

# pizzas from cheapest to most expensive
pizzas.sort()
# cheapest one
cheapest_pizza = pizzas[0]
# most expensive pizza
priciest_pizza = pizzas[-1]

#three cheapest
three_cheapest = pizzas[:3]
print(three_cheapest)

# number of 2 dollar pizzas
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)