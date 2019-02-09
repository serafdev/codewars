# Instructions

Write a function named `first_non_repeating_letter` that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input `'stress'`, the function should return `'t'`, since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input `'sTreSS'` should return `'T'`.

If a string contains all repeating characters, it should return an empty string (`""`) or `None` -- see sample tests.

## Solution

```python
def first_non_repeating_letter(string):
    unique_characters = [char for char in string if string.lower().count(char.lower()) == 1]
return unique_characters[0] if unique_characters else ''
```

We first build an array with every character that has a count of 1 using a condition in the list comprehension: `string.lower().count(char.lower()) == 1`

Then we just take the first element with `unique_characters[0]` if there is one, else, as asked in the instructions we return an empty string `''` (we could've also returned `None`)
