# RegEx (Regular Expressions)

## Overview

Regular expressions (regex) are powerful patterns for searching, matching, and manipulating text. Python's `re` module provides comprehensive regex support for text processing tasks ranging from simple validation to complex parsing.

## Core Things to Learn

### 1. Basic Pattern Matching

```python
import re

# Search for pattern anywhere in string
match = re.search(r'world', 'Hello world')  # <Match object>

# Match pattern at start of string
match = re.match(r'Hello', 'Hello world')  # <Match object>
match = re.match(r'world', 'Hello world')  # None (not at start)

# Find all occurrences
matches = re.findall(r'\d+', 'I have 2 cats and 3 dogs')  # ['2', '3']

# Check if pattern exists (returns bool)
if re.search(r'python', text, re.IGNORECASE):
    print("Found Python!")
```

### 2. Pattern Syntax

**Basic Patterns:**
- `.` - Any character except newline
- `\d` - Digit (0-9)
- `\w` - Word character (letter, digit, underscore)
- `\s` - Whitespace (space, tab, newline)
- `^` - Start of string
- `$` - End of string

**Quantifiers:**
- `*` - 0 or more
- `+` - 1 or more
- `?` - 0 or 1
- `{n}` - Exactly n times
- `{n,m}` - Between n and m times

**Character Classes:**
- `[abc]` - Match a, b, or c
- `[^abc]` - Match anything except a, b, c
- `[a-z]` - Match lowercase letters
- `[A-Z]` - Match uppercase letters
- `[0-9]` - Match digits

### 3. Groups and Capturing

```python
import re

# Capture groups with ()
match = re.search(r'(\w+)@(\w+\.\w+)', 'user@example.com')
match.group(0)  # 'user@example.com' (full match)
match.group(1)  # 'user'
match.group(2)  # 'example.com'

# Named groups
match = re.search(r'(?P<user>\w+)@(?P<domain>\w+\.\w+)', 'user@example.com')
match.group('user')    # 'user'
match.group('domain')  # 'example.com'

# Non-capturing groups (?:...)
match = re.search(r'(?:Mr|Mrs|Ms)\. (\w+)', 'Mr. Smith')
match.group(1)  # 'Smith' (title not captured)
```

### 4. Flags (Modifiers)

```python
import re

# Case-insensitive matching
re.search(r'python', 'PYTHON', re.IGNORECASE)  # or re.I

# Multiline mode (^ and $ match line boundaries)
re.findall(r'^line', text, re.MULTILINE)  # or re.M

# Dot matches newline
re.search(r'start.*end', text, re.DOTALL)  # or re.S

# Verbose mode (allows comments and whitespace)
pattern = re.compile(r'''
    \d{3}    # Area code
    -        # Separator
    \d{4}    # Number
''', re.VERBOSE)  # or re.X

# Combine flags with |
re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
```

### 5. Substitution

```python
import re

# Replace pattern with string
result = re.sub(r'\d+', 'NUM', 'I have 2 cats')  # 'I have NUM cats'

# Replace with function
def double(match):
    num = int(match.group())
    return str(num * 2)

result = re.sub(r'\d+', double, 'I have 2 cats and 3 dogs')
# 'I have 4 cats and 6 dogs'

# Replace with backreferences
result = re.sub(r'(\w+) (\w+)', r'\2 \1', 'First Last')
# 'Last First'
```

### 6. Compiling Patterns

```python
import re

# Compile for reuse (more efficient)
pattern = re.compile(r'\d{3}-\d{4}')

# Use compiled pattern
match = pattern.search('Call 555-1234')
matches = pattern.findall(text)
result = pattern.sub('XXX-XXXX', text)
```

### 7. Raw Strings (Critical!)

```python
# ❌ BAD: Backslashes interpreted by Python first
pattern = '\d+'  # SyntaxError: invalid escape sequence

# ✅ GOOD: Raw string (r'...') - backslashes are literal
pattern = r'\d+'

# Example: matching Windows paths
pattern = r'C:\\Users\\.*'  # Without raw string: 'C:\\\\Users\\\\.*'
```

## Common Use Cases

1. **Email validation**: `r'^[\w\.-]+@[\w\.-]+\.\w+$'`
2. **Phone numbers**: `r'\d{3}-\d{3}-\d{4}'`
3. **URLs**: `r'https?://[\w\.-]+\.\w+'`
4. **Date extraction**: `r'\d{4}-\d{2}-\d{2}'`
5. **HTML tag removal**: `r'<[^>]+>'`
6. **Password validation**: `r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'`

## Python Libraries

| Function | Purpose | Returns |
|----------|---------|---------|
| `re.search()` | Find first match anywhere | Match object or None |
| `re.match()` | Match at start of string | Match object or None |
| `re.fullmatch()` | Match entire string | Match object or None |
| `re.findall()` | Find all matches | List of strings |
| `re.finditer()` | Find all matches (iterator) | Iterator of Match objects |
| `re.sub()` | Replace matches | Modified string |
| `re.split()` | Split by pattern | List of strings |
| `re.compile()` | Compile pattern | Pattern object |

## Best Practices

### 1. Always Use Raw Strings
```python
# ❌ BAD: Double backslashes needed
pattern = '\\d{3}-\\d{4}'

# ✅ GOOD: Raw string (r'...')
pattern = r'\d{3}-\d{4}'
```

### 2. Compile for Reuse
```python
# ❌ INEFFICIENT: Recompiles every iteration
for line in lines:
    if re.search(r'\d+', line):
        process(line)

# ✅ EFFICIENT: Compile once
pattern = re.compile(r'\d+')
for line in lines:
    if pattern.search(line):
        process(line)
```

### 3. Use Named Groups for Clarity
```python
# ❌ UNCLEAR: Numbered groups
match = re.search(r'(\d+)-(\d+)-(\d+)', date_str)
year = match.group(1)

# ✅ CLEAR: Named groups
match = re.search(r'(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+)', date_str)
year = match.group('year')
```

### 4. Validate Before Extracting
```python
# ❌ BAD: Crashes if no match
email = re.search(r'[\w\.-]+@[\w\.-]+', text).group()

# ✅ GOOD: Check first
match = re.search(r'[\w\.-]+@[\w\.-]+', text)
if match:
    email = match.group()
```

## Common Patterns

### Email Validation
```python
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.fullmatch(email_pattern, email):
    print("Valid email")
```

### Extract URLs
```python
url_pattern = r'https?://(?:www\.)?[\w\.-]+\.\w+[/\w\.-]*'
urls = re.findall(url_pattern, text)
```

### Password Strength
```python
# At least 8 chars, 1 uppercase, 1 lowercase, 1 digit
password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d@$!%*?&]{8,}$'
if re.fullmatch(password_pattern, password):
    print("Strong password")
```

### Remove HTML Tags
```python
clean_text = re.sub(r'<[^>]+>', '', html_string)
```

### Split by Multiple Delimiters
```python
result = re.split(r'[;,\s]\s*', 'apple, banana; cherry orange')
# ['apple', 'banana', 'cherry', 'orange']
```

## Performance Tips

1. **Compile patterns used multiple times**
2. **Use raw strings** to avoid escaping confusion
3. **Be specific** - `\d{3}` is faster than `\d+` when you know the length
4. **Avoid catastrophic backtracking** - test patterns on long strings
5. **Use non-capturing groups** `(?:...)` when you don't need the match

## Common Pitfalls

### Greedy vs Non-Greedy
```python
# Greedy: matches as much as possible
re.search(r'<.*>', '<b>bold</b> and <i>italic</i>').group()
# '<b>bold</b> and <i>italic</i>' (entire string!)

# Non-greedy: add ? after quantifier
re.search(r'<.*?>', '<b>bold</b> and <i>italic</i>').group()
# '<b>' (first tag only)
```

### Escaping Special Characters
```python
# Special chars: . ^ $ * + ? { } [ ] \ | ( )
# Must escape with \\ (or use re.escape())

# ❌ BAD: . matches any character
re.search(r'example.com', 'exampleXcom')  # Matches!

# ✅ GOOD: Escape the dot
re.search(r'example\.com', 'exampleXcom')  # No match

# ✅ AUTOMATIC: Use re.escape()
re.search(re.escape('example.com'), text)
```

## Visualize It

- [Regex101](https://regex101.com/) - Test and debug regex
- [RegExr](https://regexr.com/) - Learn regex interactively
- [Pythex](https://pythex.org/) - Python-specific regex tester

## References

- [Python re docs](https://docs.python.org/3/library/re.html)
- [Regular Expressions HOWTO](https://docs.python.org/3/howto/regex.html)
- [RegexOne tutorial](https://regexone.com/)
- Python roadmap — https://roadmap.sh/python

## Related Topics

- `D.3_Strings/1_Strings` - String basics
- `D.3_Strings/5_String_Methods` - String manipulation
- `I.8_Files_Data/9_Text_Processing` - Advanced text processing
- `Real_World_Applications/04_Data_Science` - Data cleaning with regex

