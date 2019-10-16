list1 = ['AAA', 'BAA', 'AAB', 'BAB', 'BBB', 'DAA']
list2 = ['AAB', 'AAA', 'BAA', 'BBB', 'ABA']
for i in list1:
    if i in list2:
        pass
    else:
        print(f'в списке list2 отсутствуйт элемент {i}')
for i in list2:
    if i in list1:
        pass
    else:
        print(f'в список list2 добавлен элемент {i}')

for ind1, item1 in enumerate(list1):
    for ind2, item2 in enumerate(list2):
        if item1 == item2:
            if ind1 == ind2:
                print(f'Элемент {item2} остался на своем месте')
            else:
                print(f'элемент {item1} с индекса {ind1} переместился на индекс {ind2}')
