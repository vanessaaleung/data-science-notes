# Text Mining in Python
## Regex
### Character matches
  - `.`: wildcard, matches a single character
  - `^`: start of a string
  - `$`: end of a string
  - `[]`: matches one of the set of characters within []
  - `[^abc]`: matches a character that is not a, b, or, c
  - `a|b`: matches either a or b
  - `()`: scoping for operators
  - `\`: escape characters (\t, \n, \b)
  
### Character symbols
- `\b`: matches word boundary
- `\d`: any digit
- `\D`: any non-digit
- `\s`: any whitespaces
- `\S`: any non-whitespace
- `w`: alphanumeric
- `\W`: non-alphanumeric

### Repetitions
- `*`: matches 0+ times
- `+`: matches 1+ times
- `?`: matches 0 or 1 times
- `{n}`: exactly n times
- `{n,}: at least n repetitions
- `{,n}: at most n repetitions
- `{m, n}`: at least m and at most n

### Regex in Python
```python
import re
[w for w in text if re.search('@\w+', w)]
re.findall(r'[aeiou]', text)
```

## Non-ASCII Characters
### ASCII
_American Standard Code for Information Interchange_
- 7-bit long, 128 valid codes
- Range: 0x00 - 0x7F
- Includes alphabets(upper & lower), digits, punctuations, control characters, common symbols

### Unicode
_Industry standard for encoding and representing text_
- UTF-8: 1-4 bytes
  - Unicode Transformational Format - 8-bits
- UTF-16: one or two 16-bit code units
- UTF-32: one 32-bit code unit
