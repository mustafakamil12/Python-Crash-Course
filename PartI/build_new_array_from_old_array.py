unconfirmed = ['alice', 'brian', 'candace']
confirmed = []
print(unconfirmed)

while unconfirmed:
    current_user = unconfirmed.pop()
    confirmed.append(current_user)

print(confirmed)
