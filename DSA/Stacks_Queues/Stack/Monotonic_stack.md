# Monotonic Stack
A monotonic stack is a stack that maintains its elements in a specific order, either increasing or decreasing.
## Example: Monotonic Stack in Action

Consider the following sequence of numbers: `1, 7, 9, 5`. Below is how a monotonic stack evolves when maintaining an increasing order:

1. Push `1` onto the stack: `[1]`
2. Push `7` onto the stack: `[1, 7]`
3. Push `9` onto the stack: `[1, 7, 9]`
4. Encounter `5`: Pop elements greater than `5` (i.e., `9, 7`), then push `5`: `[1, 5]`

This demonstrates how the stack adjusts to maintain its monotonic property.

(monotonic_stack)[https://www.geeksforgeeks.org/introduction-to-monotonic-stack-2/]