pets = ['dog', 'cat', 'fish', 'goldfish', 'cat', 'kangaro', 'cat']
print(f"pets list before removing cat = {pets}")

while 'cat' in pets:
    pets.remove('cat')

print(f"pets list after removing cat = {pets}")
