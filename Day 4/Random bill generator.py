import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

generate_bill = random.randint(0,4)
print (friends[generate_bill])

# or use print(random.choice(friends))