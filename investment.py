shares = 10
purchase_price = 150

total_cost = shares * purchase_price

new_share_price = 175
current_value = shares * new_share_price

profit = current_value - total_cost
percentage_return = (profit / total_cost) * 100

print("Number of Shares:", shares)
print("Purchase Price per Share: $", purchase_price)
print("Total Investment Cost: $", total_cost)
print("New Share Price: $", new_share_price)
print("Current Investment Value: $", current_value)
print("Profit/Loss: $", profit)
print("Percentage Return:", round(percentage_return, 2), "%")