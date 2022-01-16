users = {
    'aeinestein':{
        'first': 'albert',
        'last': 'einestein',
        'location': 'princeton',
    },
    'mcuri': {
        'first': 'marie',
        'last': 'curie',
        'location': 'passy',
    },
}

for name,info in users.items():
    print(f"full name: {info['first']} {info['last']}")

for u_info in users.values():
    for key,detail in u_info.items():
        print(key, detail)
