# 2019-01-29
## python looping`
resource: https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
- python's `for` loop is really a `foreach` loop
- when we do not care about indexes:
```
colours = ['salmon', 'violet', 'octamarine']
for colour in colours:
    print(colour)
```
- whenever we want indexes while looping, we should think of `enumerate`

```
blackwell_games = ['legacy', 'unbound', 'convergence', 'deception', 'epiphany']
for num, title in enumerate(blackwell_games, start=1):
    print('Game # {}: blackwell {}'.format(num, title))
```
- `enuemrate` returns an *iterable*
    - each element of the iterable is a tuple that contains the index of the item and the value of the item
    - it begins from index 0, unless otherwise specified with `start`

- whenever we need to loop over multiple lists at the same time, we should use `zip`
    - for e.g. we want `colours[i]` and `blackwell_games[i]`
    - `zip` takes multiple lists, and returns an iterable that provides a tuple of the corresponding elements of each list as we loop over it

```
for colour, ratio in zip(colours, ratios):
    print('{}% {}'.format(ratio * 100, colour))
```
- NOTE: `zip` with different size lists will stop after the shortest list runs out 
- NOTE: `zip` in Python2 returns a list but `zip` in Python 3 returns a lazy iterable

## python: generators and lazy evaluation
resource: http://naiquevin.github.io/python-generators-and-being-lazy.html

```
def generator(n):
    num = 0
    while num < n:
        yield num / 2
        num += 1

```
- `yield` is used like `return`, except the function returns a generator
- when you call the function, the code written in the function body does not run. It only returns the `generator` object
- to begin executing code, use the `next` method
```
>>> print(g.next())
0
>>> print(g.next())
1
```
- when the `next` is first called, the `yield` statement will be executed once, and a value will be returned
- then the control is returned back to the calling code

- generators support the `iterator protcol`
    - implement `next` and `__iter__` methods and raise `StopIteration` when no more values can be yielded

- generator expressions are similar to list comprehensions but they use round brackets `(` instead of square `[`

```
generator_object = (i*i for i in range(11)
```
- key distinctions between a generator and a list
    - that generators give our new values as they are requested, and does not keep the whole set of elements in memory
    - a generator can only be iterated over exactly once
    - a list can ge elements by index, a generator cannot

## python: multiple assignment and tuple unpacking
resource: https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/
- allows you to assign multiple variables at the same time in one line of code

```
x, y = (10, 20)
x, y = 'hi'
```
- anything that can be looped over can be 'unpacked' with multiple assignment

```
for key, value in diction.items():
```

- multiple assignment is strict and will complain if try to unpack in too few or too many variables
- in python 3, the `*` operator was added to the multiple assignment syntax, and allows us to capture the remaining items after unpacking a list

```
numbers = [1, 2, 3, 4, 5, 6]
first, *rest = numbers
print(rest)
[2, 3, 4, 5, 6]
*beginning, last = numbers
print(beginning)
[1, 2, 3, 4, 5]
head, *middle, tail = numbers
print(middle)
[2, 3, 4, 5]
```

- so now you can do things like

```
program_name, *arguments = sys.argv
```

- so if you see hard coded slice indexes in your code, consider whether multiple assignments can help clarify what those slices represent

- you can also unpack deeply - comes up when nesting looping utilities that each provide multiple items

```
items = [1, 2, 3, 4, 2, 1]
for i, (first, last) in enumerate(zip(items, reversed(items))):
    if first != last:
        raise ValueError()
```

- it allows us to make assertions about the size and shape of our iterables

## python: list comprehensions
- tool for transforming one iterable into another list
- during this transformation, elements can be conditionally included in the new list and each element can be transformed as needed

```
new_things = []
for ITEM in old_things:
    if condition_based_on(ITEM):
        new_things.append('something with ' + ITEM)
```

to

```
new_things = ['something with ' + ITEM for ITEM in old_things if condition_based_on(ITEM)]
```

- list comprehensions with nested looping
- the `for` clauses remain in the same order as in our original `for` loops

```
flattened = []
for row in matrix:
    for n in row:
        flattened.append(n)
```

to

```
flattened = [n for row in matrix for n in row]

flattened = [
    n
    for row in matrix
    for n in row
]
```

- note that you can also do `set` and `dictionary` comprehensions

## cute python tricks
- we want to ensure that each ith row in many different matrices is the same length
- we use a set bc set items are unique
    - if you pass in objects that are all equal, there should only be one item

```
matrix_shapes = {
    tuple(len(r) for r in matrix)
    for matrix in matrices
}
if len(set(matrix_shapes)) > 1:
    raise ValueError('Given matrices are not the same shape')
```
- Note: lists are not 'hashable' (bc they are mutable); tuples can be hashable

## python: easier classes
resource: https://treyhunner.com/easier-classes/#/
- `__repr__` allows you to ensure comparibility (does this equal this?)
    - NOTE: there is both __str__ and __repr__, look up the difference between them
    - you can turn how the class was instantiated into a string
    - for e.g.
    ```
    class Month:
        def __init__(self, year, month):
            self.year, self.month = year, month
        def __repr__(self):
            return 'Month(year={}, month={}'.format(self.year, self.month)
    ```
- `__eq__`, `__lt__`, `__gt__`, `__le__`, `__ge__` lets you ensure orderability

- another thing that would be lovely is iterability
- `__iter__`
e.g. 

```
p = Point(1, 2, 3)
x, y, z = p
```
- consider whether you want the attributes of the class to be mutable
- if you do, `__setattr__` is your friend
- also, consider if you want it to be hashable `__hash__` -> then you can put it into sets

```
class Point:
    def __iter__(self):
        yield from (self.x, self.y, self.z)
    def __setattr__(self, attribute, value):
        raise AtributeError('Object is immutable')
    __delattr__ = __setattr__
    def __hash__(self):
        return hash(tuple(self))
```
