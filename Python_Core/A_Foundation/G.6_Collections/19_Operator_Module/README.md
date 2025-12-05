# Operator Module
Purpose: Efficient function equivalents for standard operators, essential for functional programming and sorting.
## Key Concepts
- \itemgetter()\: Fetch by index/key (fast)
- \ttrgetter()\: Fetch by attribute name
- \methodcaller()\: Call a method by name
- Mathematical operators: \dd\, \mul\, \itemgetter\ vs lambda
## Use Cases
- Sorting lists of dicts or objects: \sorted(data, key=itemgetter('id'))\
- Grouping with \itertools.groupby\
"@ -Encoding UTF8
        Set-Content -Path (Join-Path e:\MIU\codes\Python_Programming\Python_Core\A_Foundation\G.6_Collections\19_Operator_Module "main.py") -Value @"
from operator import itemgetter, attrgetter, methodcaller
def main():
    data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    # Sort by age using itemgetter (faster/cleaner than lambda x: x['age'])
    sorted_data = sorted(data, key=itemgetter('age'))
    print("Sorted by age:", sorted_data)
    # Multiple keys
    # sorted(data, key=itemgetter('age', 'name'))
if __name__ == "__main__":
    main()
