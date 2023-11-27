# Programming

## Algorithms
A set of rules or steps used to solve a problem

## Data Structures
A particular way of organizing data in a computer

## What is Not a "Collection"?

- simple variables whose value is overwritten with each new assignment

## A List Is a Kind of Collection

- A collection allows us to put many values in a single "variable"
- With a collection we can group mutiple values under a single concept

## List Constants
The elements are separated by commas, a list can be empty

Examples:

- [1,2,3]
- ['red', 'yellow' , 'orange']
- [1,2, [3,4], 5]
- []


## Lists Are Mutable
We can change an element of a list using the index operator

With len() function, we can get the number of elements in the list

## Range
In Python 3, range() returns an object, not a list, which is  more efficient in terms of memory.

```python
for i in range(5):
    print(i)
```