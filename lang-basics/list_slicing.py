"""
Learn about slicing the lists. You can splice a list using index pattern [start:end:step],
where start is inclusive, end is exclusive, step is increment:
start, start+step, start+2*step, start+3*step, ... <end 


Author: opendroid
Email: openweb@outlook.com
License: MIT
"""

# List spliting using [start:end:step]
first_100 = [i for i in range(101)]
first_quarter = first_100[0:26]
first_quarter_tens = first_quarter[::10]

print(f"first_100: {first_100}")
print(f"first_quarter: {first_quarter}")
print(f"first_quarter_tens: {first_quarter_tens}")

second_quarter = first_100[25:51]
second_quarter_odds = second_quarter[::2] # Skip by evey element
print(f"second_quarter: {second_quarter}")
print(f"second_quarter_odds: {second_quarter_odds}")
second_quarter_odds_reversed = second_quarter_odds[::-2]
print(f"second_quarter_odds_reversed: {second_quarter_odds_reversed}")
