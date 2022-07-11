from functools import reduce


# задание 1


def my_map(function, iterable, *iterables):
    try:
        some_object_iterator = iter(iterable)
        [my_map(function, iterable[i]) for i in range(len(iterable))]
    except TypeError:
        function(iterable)
    except RecursionError:
        function(iterable)

    if iterables:
        try:
            some_object_iterator = iter(iterables)
            [my_map(function, iterables[i]) for i in range(len(iterables))]
        except TypeError:
            function(iterables)
        except RecursionError:
            function(iterables)

# моя мапа лучше тем, что может итерировать в "глубину"
# там где обычная мапа выдвает ошибку, моя выдает результат:
# map(lambda x: print(x+1), [1, 2, 3, [4, 5]], 6, 7, [8, 9])
# TypeError: 'int' object is not iterable


my_map(lambda x: print(x+1), [1, 2, 3, [4, 5]], 6, 7, [8, 9])
my_map(lambda x: print(x*2), 'hello', ['w', 'o', 'r'], 'l', 'd', '!')


# задание 2

sum = 0


def my_reduce(function, iterable, *index):
    if index:
        try:
            some_object_iterator = iter(index[0])
            return print(f'Ошибка: начальный индекс не может быть {type(index)}')
        except TypeError:
            initializer = index[0]
            print(initializer)
            sum = function(initializer, iterable[0])
            for i in range(len(iterable)):
                if i != 0:
                    print(f'sum({sum})+iterable[i]({iterable[i]})= {sum + iterable[i]}')
                    sum = function(sum, iterable[i])
    else:
        sum = function(iterable[0], iterable[1])
        initializer = 1
        if len(iterable) > 2:
            for i in range(len(iterable)):
                if i > initializer:
                    sum = function(sum, iterable[i])

    print(sum)


b = [8, 1, 2, 3, 4, 5]
c = [1, 2]
d = [1, 2, 3, 4]


my_reduce(lambda a, x: a * x, d, 4)

sum1 = reduce(lambda a, x: a * x, d, 4)
print(sum1)




