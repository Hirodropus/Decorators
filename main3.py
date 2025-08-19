import types
from datetime import datetime

def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            function_name = old_function.__name__
            result = old_function(*args, **kwargs)
            log_entry = (f'В {current_time} - функция {function_name} c аргументами {args} и'
                         f' {kwargs} выполнилась и вернула {result}')
            print(log_entry)

            with open(path, 'a', encoding='utf-8') as log_file:
                log_file.write(log_entry + '\n')

            return result

        return new_function

    return __logger

def flat_generator(list_of_list):
    for item in list_of_list:
        if isinstance(item, list):
            yield from flat_generator(item)
        else:
            yield item


@logger('task_3.log')
def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):


        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

    return 'Тест пройден успешно'


if __name__ == '__main__':
    test_2()