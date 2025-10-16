our_dictionary=[{'id': '1', 'name':'zoro', 'age': '22'},
                {'id': '2', 'name':'shank', 'age': '24'},
                {'id': '3', 'name':'luffy', 'age': '26'},
                {'id': '4', 'name':'xebec', 'age': '20'}]

for keys in our_dictionary:
    print(keys['age']+'->'+keys['name']+'->'+keys['id'])