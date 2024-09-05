name:str = "Usama Thakur"
print(name)

message:str = "Pakistan Zindabad, PIAIC Paindabad"
print(message)

father_name:str = "Asad Thakur"
print(father_name)

print("usama")  # Print the string "usama" to the console
name = "usama Thakur"  # Assign the string "usama Thakur" to the variable name

print(name.capitalize())  # Capitalize the first letter of the string
print(name.casefold())  # Convert the string to lowercase for case-insensitive comparisons
print(name.center(40, "*"))  # Center the string within a field of width 40, padding with "*"
print(name.count("a"))  # Count the occurrences of "a" in the string
print(name.encode())  # Encode the string using the default UTF-8 encoding
print(name.endswith("r"))  # Check if the string ends with "r"
print(name.expandtabs(4))  # Replace tabs with 4 spaces (though there are no tabs in this string)
print(name.find("a"))  # Find the first occurrence of "a" in the string
print(name.format())  # Format the string (no placeholders to replace here)
print(name.format_map({}))  # Format the string using a dictionary (empty dictionary here)
print(name.index("a"))  # Find the first occurrence of "a", like find(), but raises an error if not found
print(name.isalnum())  # Check if the string is alphanumeric (contains only letters and numbers)
print(name.isalpha())  # Check if the string contains only alphabetic characters
print(name.isascii())  # Check if all characters in the string are ASCII
print(name.isdecimal())  # Check if the string contains only decimal characters
print(name.isdigit())  # Check if the string contains only digits
print(name.isidentifier())  # Check if the string is a valid Python identifier (variable name)
print(name.islower())  # Check if all characters in the string are lowercase
print(name.isnumeric())  # Check if the string contains only numeric characters
print(name.isprintable())  # Check if all characters in the string are printable
print(name.isspace())  # Check if the string contains only whitespace characters
print(name.istitle())  # Check if the string is in title case (each word capitalized)
print(name.isupper())  # Check if all characters in the string are uppercase
print(name.join(['*', '*']))  # Join the list elements with the string as separator
print(name.ljust(20))  # Left-justify the string within a field of width 20
print(name.lower())  # Convert the string to lowercase
print(name.lstrip())  # Remove leading whitespace from the string
print(name.maketrans("a", "b"))  # Create a translation table to replace "a" with "b"
print(name.partition(" "))  # Partition the string into three parts: before, separator, after
print(name.removeprefix("u"))  # Remove the prefix "u" from the string if it exists
print(name.removesuffix("r"))  # Remove the suffix "r" from the string if it exists
print(name.replace("a", "A"))  # Replace all occurrences of "a" with "A"
print(name.rfind("a"))  # Find the last occurrence of "a" in the string
print(name.rindex("a"))  # Find the last occurrence of "a", like rfind(), but raises an error if not found
print(name.rjust(20))  # Right-justify the string within a field of width 20
print(name.rpartition(" "))  # Partition the string into three parts: before, separator, after (searches from right)
print(name.rstrip())  # Remove trailing whitespace from the string
print(name.rsplit())  # Split the string into a list of words from the right (default is whitespace separator)
print(name.split())  # Split the string into a list of words (default is whitespace separator)
print(name.splitlines())  # Split the string into a list of lines
print(name.startswith("u"))  # Check if the string starts with "u"
print(name.strip())  # Remove leading and trailing whitespace from the string
print(name.swapcase())  # Swap the case of all characters in the string
print(name.title())  # Convert the string to title case (each word capitalized)
print(name.translate(str.maketrans("a", "A")))  # Replace "a" with "A" using a translation table
print(name.upper())  # Convert the string to uppercase
print(name.zfill(10))  # Pad the string with leading zeros until it reaches a width of 10
