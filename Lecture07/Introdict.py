phonebook = {'Anirach': '777-1111', 'Mikey': '777-2222', 'Donald': '777-3333'}

print(phonebook)

print(phonebook['Mikey'])
print(phonebook.get('Donald'))

key = 'Pluto'
if key in phonebook:
    print(phonebook['Pluto'])
else:
    print(key + ' not in phonebook')

phonebook['Simpson'] = '777-4567'
phonebook['Pluto'] = '777-4444'
phonebook['Mikey'] = '777-2122'

del phonebook['Simpson']
print(phonebook)
