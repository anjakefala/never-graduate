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

- whenever you see a list comprehension that loops over something and does not filter anything or change any item, but just makes a list
    - e.g. `rows = [line for line in reader]`
- you can replace it with the list constructor
    - `rows = list(rdr)

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

# python: command line arguments

- to grab command line arguments you can use the `sys` module
    - the command line arguments are held in a list: `sys.argv`. At index `0` is the name of the program

- if you use list unpacking, then you can assert for the number of items passed through the command line
    - `old_file, new_file = sys.argv[1:]

- `sys.maxsize` provides the largest positive integer supported by the platform -> thus the maximum size lists, strings, dicts, and many other containers can have

- to make the command-line functionality more robust, use `argparse` from the standard library
    - https://docs.python.org/3/howto/argparse.html

```
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('input_filename')
parser.add_argument('output_filename')
args = parser.parse_args()

with open(args.old_filename) as fp:
```

- why argparse is the better choice: https://www.python.org/dev/peps/pep-0389/#why-aren-t-getopt-and-optparse-enough

- the above example shows how to use argparse to parse two positional mandatory arguments

- to add optional arguments, with default values

```
parser.add_argument('--in-delimiter', dest='delimiter', default='|')
```

# python: csv reading and writing
- python comes with a `csv` module
- `rdr = csv.reader(fp, delimiter)`
    - `rows = [line for line in rdr]`
- `writer = csv.writer(fp)`
    - `writer.writerows(rows)`
- csv module works for any delimited data files, not just comma-delimited files
- the writer's writerows method takes an iterable and the reader object *is* an iterable

- to automatically attempt to detect the format of an input file, use the `csv` module's `Sniffer` class

```
dialect = csv.Sniffer().sniff(fp_read())
fp.seek(0)
```
- this entails sniffing the entire csv file and then seeking back to the beginning of the file so that you can start reading it again -> this is bc files are iterators

# python: CRLF vs LF
- python automatically takes all LF endings (`\n`) and converts them to CRLF endings (`\r\n`) on Windows systems

# python: file parsing
- if you use `with` statements, you do not need to remember to close your fp afterwards
`with open(filename, newline='') as fp:`
- be careful with nested `with` statements, where one is a reader, and the other a writer; if you provide the same filename for both input and output, you may get weird results bc you are writing to a file as you are reading it.
- files are iterators, whichs means they are stateful -> they keep track of where we are on them as we loop over them

# python: keyword (named) arguments in python - how to use them
source: https://treyhunner.com/2018/04/keyword-arguments-in-python/
- unlike many other programming languages, Python knows the names of the arguments functions accept
- functions can be called with a mix of positional and named arguments
- when we use keyword arguments
    - we can often leave out arguments that have default values
    - we can rearrange arguments in a way that makes them more readable
    - we call arguments by their names to make it more clear what they represent
- Python has a number of functions that take an unlimited number of positional arguments. These functions sometimes have arguments that can be provided to customise their functionality. Those arguments must be provided as named arguments to distinguish them from the unlimited positional arguments. 
- e.g. `print('comma', 'separated', 'words', sep=', ')

- to create a function that accepts any number of positional arguments with some keyword-only arguments -> use the `*` operator to capture all the positional arguments

```
def product (*numbers, initial=1):
    total = initial
    for n in numbers:
        total *= n
    return total
```

- `*numbers` -> captures all positional arguments given to the `product` function into a tuple which the `numbers` variable points to

- python allows functions to capture any keyword arguments provided to them using the `**` operator when defining the function

```
def format_attributes(**attributes):
    '''Return a string of comma-separated key-value pairs.'''
    return ", ".join(
        f"{param}: value"
        for param, value in attributes.items()
    )

- we can also pass arbitrary keyword arguments into our function using the `**` operator to unpack our dictionary items into keyword arguments in our function call
    - `items = {'name': 'Trey', 'website': 'http://treyhunner.com'}
    - `format_attributes(**items)`

- since python3.6 functions always preserve the order of the keyword arguments passed to them.
