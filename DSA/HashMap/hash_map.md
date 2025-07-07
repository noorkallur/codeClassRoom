# Hash Map
A hash map is a data structure that allows you to store and retrieve data efficiently using a key-value pair system

# General Hashmap Tips for Algorithm Problems

1. Use hashmap/`Counter` to store frequencies  
   - Great for counting letters, numbers, or any items in one pass.

2. Compare two hashmaps directly with `==`  
   - If keys and their counts match, `map1 == map2` returns `True`.

3. Remove zero‐count entries  
   - After decrementing, delete keys with count 0 to keep your map small and comparisons fast.

4. Use `get` (or `defaultdict`) for safe updates  
   ```python
   counts[ch] = counts.get(ch, 0) + 1
   ```
   avoids key‐errors and makes code concise.

5. Track complements for “two-sum”-type problems  
   - As you scan, store seen numbers in a map; for each new number, check if its complement is already in the map.

6. Store last-seen indices  
   - In string/array problems, map each element to its most recent index to compute spans or detect repeats in O(1).

7. Group by a hashmap key  
   - To group anagrams or similar items, use a sorted tuple or a count tuple as the key in your map.

8. Memoize recursive calls  
   - Cache function inputs → outputs in a map to turn exponential recursion into polynomial time.

9. Implement sliding windows with a hashmap  
   - Maintain counts of the current window; expand/contract pointers and update the map in O(1) per move.

10. Use prefix-sum maps for subarray sums  
    - Store `running_sum → index` so you can detect any subarray with a given sum in one pass.

---

Whenever you see a need to track occurrences, map one thing to another, or cache results—reach for a hashmap first!