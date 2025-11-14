
import time 
import random 
import faker 
import This_is_the_thing_you_need_to_change.py
COGS_PERCENTAGE = 0.20

class queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

cafe_name = random.choice(cafe_names)

def coffee_shop_simulation(num_customers, day_number):
    q = queue()
    fake = faker.Faker()
    daily_profit = 0.0

    print(f"\n--- Day {day_number}: {cafe_name} opens for business ---")
    print()
    
    for i in range(num_customers):
        customer_name = fake.name()
        q.enqueue(customer_name)
        print(f"Customer {i+1}: {customer_name} has joined the service line.")
        arrival_interval = random.uniform(0.5, 2.0)
        time.sleep(arrival_interval)

    print("\n--- All customers have arrived. Service is beginning. ---")

    while not q.isEmpty():
        serving_gap = random.uniform(0.5, 1.0)
        time.sleep(serving_gap)
        customer = q.dequeue()
        serving_time = random.uniform(2, 5)
        
        random_coffee = random.choice(list(coffees.keys()))
        price_batches = coffees[random_coffee]
        coffee_price = random.choice(price_batches) 

        coffee_cost = coffee_price * COGS_PERCENTAGE
        profit = coffee_price - coffee_cost
        daily_profit += profit

        print(f"\nNow serving: {customer}")
        print(f"{customer}'s order: {random_coffee}, Price: ${coffee_price:.2f}")
        print(f"Serving time: {serving_time:.2f} seconds.")
        time.sleep(serving_time)
        print(f"Completed serving {customer}.")

    print(f"\n--- Day {day_number} ends. Coffee shop is closing. ---")
    return daily_profit

def multi_day_simulation(num_days, num_customers_per_day):
    total_profit = 0.0
    daily_profits = []
    for day in range(1, num_days + 1):
        daily_profit = coffee_shop_simulation(num_customers_per_day, day)
        total_profit += daily_profit
        daily_profits.append(daily_profit)
        print(f"\n--- End of Day {day} ---")
        if total_profit != 0:
            continue
        else:
            print("You went bankrupt. Try adjusting prices to better match the fact that everything has an equal chance of happening.")
            quit
        print(f"Daily Profit: ${daily_profit:.2f}")
        print(f"Cumulative Profit: ${total_profit:.2f}")
        print("------------------------")

    print("\n\n=== MULTI-DAY SIMULATION COMPLETE ===")
    print(f"Total simulated days: {num_days}")
    print(f"Total cumulative profit across all days: ${total_profit:.2f}")
    print("\n--- Daily Profit Breakdown ---")
    for i, profit in enumerate(daily_profits, 1):
        print(f"Day {i}: ${profit:.2f}")

if __name__ == "__main__":
    multi_day_simulation(num_days=3, num_customers_per_day=10)
