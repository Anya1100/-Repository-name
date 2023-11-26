# TODO Напишите функцию для поиска индекса товара
def find_index(spisok, tovar):
    try:
        elem_idx = spisok.index(tovar)
    except ValueError:
        print(f"Товар '{tovar}' не найден в списке.")
    else:
        print(f"Первое вхождение товара '{tovar}' имеет индекс {elem_idx}.")



items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
find_index(items_list, 'банан')
find_index(items_list, 'груша')
find_index(items_list, 'персик')

