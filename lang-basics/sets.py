"""
This module provides comprehension sets: unordered collection with no duplicates.


Author: opendroid
Email: openweb@outlook.com
License: MIT
"""

set_a = {"apples", "oranges", "bananas", "apples", "cucumber", "oranges"}
set_b = set("apples")
print(f"set A: {set_a}")
print(f"set B: {set_b}")

# Intersection
fruits_ca = {
    "grapes",
    "lemons",
    "oranges",
    "tangerines",
    "plums",
    "grapes",
    "oranges",
    "tangerines",
}
fruits_fl = {
    "pineapples",
    "jackfruits",
    "oranges",
    "lychees",
    "papayas",
    "guavas",
    "tangerines",
    "jackfruits",
}

fruits_both_states = fruits_ca & fruits_fl
print(f"fruits_both_states: {fruits_both_states}")
fruits_ca_not_fl = fruits_ca - fruits_fl
print(f"fruits_ca_not_fl: {fruits_ca_not_fl}")
fruits_ca_or_fl_or_both = fruits_ca | fruits_fl
print(f"fruits_ca_or_fl_or_both: {fruits_ca_or_fl_or_both}")
fruits_ca_or_fl_not_both = fruits_ca ^ fruits_fl
print(f"fruits_ca_or_fl_not_both: {fruits_ca_or_fl_not_both}")
