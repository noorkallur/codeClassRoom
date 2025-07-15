# Important Python String Methods for Coding Interviews

Below is a curated list of built-in `str` methods you’ll frequently need. They’re organized by category for easy reference.

---

## Case Manipulation

* `s.lower()`  
  Converts all letters in `s` to lowercase.

* `s.upper()`  
  Converts all letters in `s` to uppercase.

* `s.capitalize()`  
  Makes the first character uppercase and the rest lowercase.

* `s.title()`  
  Capitalizes the first letter of each word.

* `s.swapcase()`  
  Swaps case: lowercase → uppercase, uppercase → lowercase.

* `s.casefold()`  
  Aggressive lowercase, useful for caseless comparisons.

---

## Testing & Inspection

* `s.isalpha()`  
  Returns `True` if all characters are letters and there’s at least one character.

* `s.isdigit()`  
  Returns `True` if all characters are digits and there’s at least one character.

* `s.isalnum()`  
  Returns `True` if all characters are letters or digits and there’s at least one character.

* `s.isspace()`  
  Returns `True` if all characters are whitespace and there’s at least one character.

* `s.istitle()`  
  Returns `True` if `s` is titlecased (each word starts with uppercase).

* `s.isupper()` / `s.islower()`  
  Returns `True` if all cased characters are in upper/lower case and there’s at least one cased character.

---

## Searching & Counting

* `s.find(substr)` / `s.rfind(substr)`  
  Returns the lowest/highest index of `substr` or `-1` if not found.

* `s.index(substr)` / `s.rindex(substr)`  
  Like `find`, but raises `ValueError` if `substr` is missing.

* `s.count(substr)`  
  Returns the number of non-overlapping occurrences of `substr`.

* `s.startswith(prefix)` / `s.endswith(suffix)`  
  Boolean checks for starting/ending substrings; support tuples for multiple options.

---

## Modification

* `s.replace(old, new, count=-1)`  
  Returns a new string where occurrences of `old` are replaced by `new`. Optional `count` limits replacements.

* `s.strip(chars=None)` / `s.lstrip(chars)` / `s.rstrip(chars)`  
  Removes leading/trailing (or both) characters in `chars` (defaults to whitespace).

---

## Splitting & Joining

* `s.split(sep=None, maxsplit=-1)` / `s.rsplit(sep, maxsplit)`  
  Splits `s` into a list; default splits on any whitespace.

* `s.splitlines(keepends=False)`  
  Splits at line boundaries, optionally keeping line breaks.

* `s.partition(sep)` / `s.rpartition(sep)`  
  Splits into a 3-tuple `(before, sep, after)` at the first/last occurrence.

* `sep.join(iterable)`  
  Joins elements of an iterable with separator `sep`.

---

## Padding & Alignment

* `s.ljust(width, fillchar=" ")` / `s.rjust(width, fillchar)`  
  Left/right-align text in a field of given width.

* `s.center(width, fillchar=" ")`  
  Centers text in a field of given width.

* `s.zfill(width)`  
  Pads numeric strings on the left with zeros to fill width.

---

## Formatting & Translation

* `s.format(*args, **kwargs)`  
  Positional and keyword replacement fields, e.g. `"Hi, {}!".format(name)`.

* `s.format_map(mapping)`  
  Similar to `format`, but takes a dictionary-like object.

* `str.maketrans(x, y=None, z=None)` & `s.translate(table)`  
  Creates and applies translation tables for character-by-character mappings.

---

