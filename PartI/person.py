def build_person(first_name, last_name, middle_name='', age=None):
    """Return a dictionary of information about a person."""
    if middle_name:
        person = {'first': first_name, 'middle': middle_name, 'last': last_name}
    else:
        person = {'first': first_name, 'last': last_name}

    if age:
        person['age'] = age

    return person

musician = build_person('jimi', 'hendrix', middle_name='Lee', age=80)
print(musician)
