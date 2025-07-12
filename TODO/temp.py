import os

file_path = "C:\\Users\\messierj\\OneDrive - Conseil scolaire Viamonde\\Documents\\Code projects\\PyBattler v.2\\TODO\\pokedex.py"

# Read the file
with open(file_path, 'r') as file:
    file_content = file.read()

# Function to add quotes to unquoted keys
import re

def add_quotes_to_keys(content):
    # Regex pattern to find unquoted keys
    pattern = r'(\t)(\w+)(\s*:)'
    
    # Add quotes to keys using the regex pattern
    modified_content = re.sub(pattern, r'\1"\2"\3', content)
    return modified_content

# Modify the content
modified_content = add_quotes_to_keys(file_content)

# Write the modified content back to the file
with open(file_path, 'w') as file:
    file.write(modified_content)

# Confirmation message
print("Completed modification and saved the file successfully.")