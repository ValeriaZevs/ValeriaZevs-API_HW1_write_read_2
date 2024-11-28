with open('text.txt', 'r', encoding='UTF-8') as f:
    st, s = [], []
    cook_book = {}
    for i in f.readlines():  # Убираем пустые строчки и записываем списки (рецепты)
        if len(i) == 1:
            st.append(s)
            s = []
        else:
            s.append(i.rstrip('\n'))
    st.append(s)

    for i in st:  # Заполняем словарь значениями
        c = []  # Список словарей
        for j in i[2:]:
            sp = {'ingredient_name': '', 'quantity': '', 'measure': ''}
            line = j.split(' | ')
            sp['ingredient_name'], sp['quantity'], sp['measure'] = line[0], int(line[1]), line[2]
            c.append(sp)
        cook_book[i[0]] = c


def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    for i in dishes:
        ingredients = cook_book[i]
        for j in ingredients:
            if j['ingredient_name'] not in res:
                res[j['ingredient_name']] = {'measure': j['measure'], 'quantity': j['quantity'] * person_count}
            else:
                res[j['ingredient_name']]['quantity'] += (j['quantity'] * person_count)
    print(res)


get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)

