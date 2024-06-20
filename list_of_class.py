class Color:
    """Colors with name and top of frequecy range"""
    def __init__(self, name, frequency) -> None:
        self.name = name
        self.frequency = frequency

# Initialize 
colors = [
    Color("Violet", 789),
    Color("Indigo", 680),
    Color("Blue", 668),
    Color("Green", 606),
    Color("Yellow", 526)
]
# Append colors
colors.append(Color(name="Orange", frequency=508))
colors.append(Color(name="Red", frequency=484))

# Helpers to iterate over properties
names = lambda objects: [obj.name for obj in objects]
frequencies = lambda objects: [obj.frequency for obj in objects]
names_frequencies = lambda objects: [f"{obj.name}:{obj.frequency}" for obj in objects]

# Print attributes
print(f"colors {len(colors)}: {names(colors)}")
print(f"frequencies {len(colors)}: {frequencies(colors)}")
print(f"names and frequencies {len(colors)}: {names_frequencies(colors)}")

# Sort based on frequency, use lambda
colors.sort(key=lambda color: color.frequency)
print(f"colors {len(colors)}: {names(colors)}")
