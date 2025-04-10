# Prefix Sum
[practice problems](https://medium.com/@maityamit/prefix-sum-summary-with-practice-questions-sheet-1d-2d-on-leetcode-83c8deb4f713)
## Introduction
The prefix sum is a powerful technique used in computer science and competitive programming to preprocess an array for efficient range queries. It involves creating a new array where each element at index `i` contains the sum of all elements from the start of the array up to index `i`.

## Applications
- Efficient range sum queries.
- Solving subarray problems.
- Optimizing algorithms for cumulative data.

## Algorithm

### Steps to Compute Prefix Sum
1. Initialize an array `prefix` of the same size as the input array.
2. Set `prefix[0] = arr[0]`.
3. For each index `i` from 1 to `n-1`:
    ```
    prefix[i] = prefix[i-1] + arr[i]
    ```

### Range Sum Query
To find the sum of elements between indices `l` and `r`:
- If `l == 0`: `sum = prefix[r]`
- Otherwise: `sum = prefix[r] - prefix[l-1]`

## Example

### Input
Array: `[2, 4, 6, 8, 10]`

### Prefix Sum Array
```
prefix[0] = 2
prefix[1] = prefix[0] + 4 = 6
prefix[2] = prefix[1] + 6 = 12
prefix[3] = prefix[2] + 8 = 20
prefix[4] = prefix[3] + 10 = 30
```
Result: `[2, 6, 12, 20, 30]`

### Range Query Example
Find the sum of elements from index `1` to `3`:
```
sum = prefix[3] - prefix[0] = 20 - 2 = 18
```

## Example usage
```
arr = [2, 4, 6, 8, 10]
prefix = compute_prefix_sum(arr)
print("Prefix Sum Array:", prefix)
print("Sum from index 1 to 3:", range_sum(prefix, 1, 3))
```

## Complexity
- **Preprocessing Time:** `O(n)`
- **Range Query Time:** `O(1)`
- **Space Complexity:** `O(n)`

## Advantages
- Reduces time complexity for multiple range queries.
- Simple and easy to implement.

## Limitations
- Requires additional space for the prefix sum array.
- Not suitable for dynamic arrays where elements change frequently.

## Related Topics
- Difference Array
- Fenwick Tree (Binary Indexed Tree)
- Segment Tree

## Tips for Solving LeetCode Questions with Prefix Sum

1. **Understand the Problem Statement**  
    Carefully read the problem to identify if it involves range queries, subarray sums, or cumulative data. Prefix sum is particularly useful in these scenarios.

2. **Precompute the Prefix Sum Array**  
    Before solving the problem, compute the prefix sum array to reduce the time complexity of range queries.

3. **Handle Edge Cases**  
    Pay attention to edge cases such as empty arrays, single-element arrays, or queries that span the entire array.

4. **Optimize Space Usage**  
    If the problem allows, use the input array itself to store the prefix sums to save space.

5. **Use Modular Arithmetic**  
    For problems involving large numbers or modulo operations, compute prefix sums modulo the given number to avoid overflow.

6. **Apply Sliding Window Technique**  
    Combine prefix sum with the sliding window technique for problems involving fixed-size subarrays.

7. **Binary Search with Prefix Sum**  
    For problems requiring specific subarray sums, use binary search on the prefix sum array to find the desired range efficiently.

8. **Debug with Small Examples**  
    Test your implementation with small, simple examples to ensure correctness before submitting.

9. **Leverage Hash Maps**  
    For problems involving subarray sums equal to a target, use a hash map to store prefix sums and their frequencies for quick lookups.

10. **Practice Common Patterns**  
     Solve multiple prefix sum problems on LeetCode to recognize patterns and improve your problem-solving skills.
