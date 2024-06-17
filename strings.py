# Various string types.

# Single quote within '...'
single_quoted_1 = "Your's truly"
double_quoted_1 = "Your's truly"

# Example double quotted: ".."
single_quoted_2 = "\"If you can't explain it simply, you don't understand it well enough.\" - Albert Einstein"
double_quoted_2 = "\"If you can't explain it simply, you don't understand it well enough.\" - Albert Einstein"

# Example formatted strings
formated_string_1 = f"They say {single_quoted_1}"
formated_string_2 = f"They say {single_quoted_1}"

# Print these strings
print(f"single_quoted_1: {single_quoted_1}")
print(f"double_quoted_1: {double_quoted_1}")
print(f"single_quoted_2: {single_quoted_2}")
print(f"double_quoted_2: {double_quoted_2}")
print(f"formated_string_1: {formated_string_1}")
print(f"formated_string_2: {formated_string_2}")

# Pre-formatted string
robert_frost_poem_1 = """
  Whose woods these are I think I know.   
  His house is in the village though;   
  He will not see me stopping here   
  To watch his woods fill up with snow."""

# Use escape characters: \n newline
robert_frost_poem_2 = "\n\tWhose woods these are I think I know.\n\tHis house is in the village though;\n\tHe will not see me stopping here\n\tTo watch his woods fill up with snow.\n"

print(f"robert_frost_poem_1: {robert_frost_poem_1}")
print(f"robert_frost_poem_2: {robert_frost_poem_2}")
