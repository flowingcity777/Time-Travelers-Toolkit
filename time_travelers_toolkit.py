# Add your Code below
import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

print(dt.date.today())
print(dt.datetime.now().time())

base_cost = Decimal('1777.77')
current_year = dt.date.today().year
target_year = randint(current_year + 1, current_year + 1000)
difference = target_year - current_year
cost_per_year = Decimal('77.77')
total_change = difference * cost_per_year

# Calculate the total cost including the base fair
final_cost = base_cost + total_change
final_cost = final_cost.quantize(Decimal('0.01'))

# Create a list of destination strings
destinations = ['Ancient Egypt', 'Medieval Europe', 'Futuristic Neo-Tokyo', 'The Renaissance', 'The Cretaceous Period']

# Use choice() to pick one destination from the list
selected_destination = choice(destinations)

# Generate and display the final travel confirmation message
message = custom_module.generate_time_travel_message(target_year, selected_destination, final_cost)
print(message)
