# phase-3-wk-1-code-challenge

# Code Challenge Project

## Overview

This project consists of three Python files: `numbers.py`, `solve.py`, and `time_converter.py`. Each file contains functions that perform specific tasks related to numbers, string manipulation, and time conversion.

## Files

### 1. numbers.py

This file contains a function `numbers(a, b, c)` that checks if there is at least one positive number among the provided arguments. It returns `True` if at least one number is positive; otherwise, it returns `False`.

#### Usage

````python
print(numbers(2, 4, -3))     # True
print(numbers(-4, 6, 8))     # False
print(numbers(4, -6, 9))     # True
print(numbers(-4, 6, 0))     # False
print(numbers(4, 6, 10))     # True
print(numbers(-14, -3, -4))  # False

### 2. convert_hours.py
This file contains a function convert_to_24_hrs(hh, mm, time) that converts a time from 12-hour format to 24-hour format.
### Usage
```python
convert_to_24_hrs(1, 36, 'am')
convert_to_24_hrs(6, 36, 'am')
convert_to_24_hrs(12, 36, 'am')

### 3. consonant.py
This file contains functions related to string manipulation, including consonant-related calculations.

### Usage
Functions

solve(word)

Performs specific calculations based on the input word. It includes calculations related to alphabets and their corresponding values.

### Usage

``` python
solve('zodiacs')    # Output: 26
solve('strength')   # Output: 57

consonant_function(word)
Additional function within solve.py that specifically deals with consonants. Please refer to the function implementation for specific details.
````
