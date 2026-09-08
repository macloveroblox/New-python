phonebook = {'Anirach': '777-1111', 'Mikey': '777-2222', 'Donald': '777-3333', 'Pluto': '777-444'}

heroesdict = {}
heroesdict['Hulk'] = '888-1111'
heroesdict['Iron man'] = '888-2222'
print(heroesdict.get('Hulk', 'Key not found'))
print(heroesdict.get('Hulk', 'Key not found'))

for key, value in phonebook.items():
    print(key, value)
print(phonebook.keys())
print(phonebook.values())

print(phonebook.pop('Mikey', 'Element not found'))
print(phonebook.pop('Mikey', 'Element not found'))
print(phonebook)
print(phonebook.popitem())
print(phonebook)
phonebook.clear()
print('After Clear')
print(phonebook)