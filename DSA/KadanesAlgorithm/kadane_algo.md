# Kadane's Algorithm

## Overview
Kadane's Algorithm is a popular algorithm used to solve the "Maximum Subarray Problem." The goal of this problem is to find the contiguous subarray within a one-dimensional array of numbers (which can include both positive and negative numbers) that has the largest sum.

## How It Works
1. Start with two variables:
    - `subArraySum`: Tracks the sum of the current subarray.
    - `CurrentElement`: value of the current element.
2. Iterate through the array:
    - For each element, decide whether to add it to the current subarray or start a new subarray with the current element.
    - How to identify wheter to start the Freshly or add to `subArraySum`?
    - if `subArraySum` + `CurrentElement` > `CurrentElement`
    - The net result is positve, Extend
    - else, The net result is negative, Start New `subArraySum`
3. At the end of the iteration, Return the maxSubSum

## Key Points
- The algorithm runs in **O(n)** time complexity, making it very efficient.
- It works by maintaining a running sum and resetting it when it becomes negative, as negative sums would decrease the total sum of any future subarray.

## Example
Given an array: `[−2, 1, −3, 4, −1, 2, 1, −5, 4]`
- The maximum sum subarray is `[4, −1, 2, 1]` with a sum of `6`.

## Use Cases
Kadane's Algorithm is commonly used in:
- Financial analysis to find the best period for maximum profit.
- Signal processing to detect the strongest signal segment.
- Competitive programming and coding interviews.

## Limitations
- Kadane's Algorithm only works for one-dimensional arrays. For multi-dimensional arrays, variations of the algorithm are required.
- It assumes at least one non-negative number in the array. If all numbers are negative, the algorithm can be modified to return the largest single element.

## Implementation
The algorithm is simple to implement and requires only a few lines of code. It is a fundamental algorithm that every programmer should understand.