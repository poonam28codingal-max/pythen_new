price = 2.50
#define a function to calculate the difference between the amount given and price mentioned
def calculate_change(amount_given):
	return amount_given - price

c = calculate_change(4.00)
print("Change the customer is due", c)