# Write a Python program to combine values in python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300},
# {'item': 'item1', 'amount': 750}]

sample_data = [{'item': 'item1', 'amount': 400},{'item': 'item2', 'amount': 300},
               {'item': 'item1', 'amount': 750}
]

my_dict = {}

for entry in sample_data:
    item = entry['item']
    amount = entry['amount']

    if item in my_dict:
        my_dict[item] += amount
    else:
        my_dict[item] = amount

print(my_dict)