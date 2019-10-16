import random
from datetime import datetime


list1 = [random.randint(10000000000000000000, 10000000000000000500) for i in range(1000)]
list2 = [random.randint(10000000000000000000, 10000000000000000500) for i in range(1000)]
start = datetime.now().timestamp()
i = 0
while i < max(len(list1), len(list2)):
    if i < len(list1):
        if list1[i] in list2:
            pass
        else:
            print(f'в списке list2 отсутствуйт элемент {list1[i]}')
    if i < len(list2):
        if list2[i] in list1:
            pass
        else:
            print(f'в список list2 добавлен элемент {list2[i]}')
    i += 1


for ind1, item1 in enumerate(list1):
    for ind2, item2 in enumerate(list2):
        if item1 == item2:
            if ind1 == ind2:
                print(f'Элемент {item2} остался на своем месте')
            else:
                print(f'элемент {item1} с индекса {ind1} переместился на индекс {ind2}')
finish = datetime.now().timestamp()
print(finish - start)