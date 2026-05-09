import os

filepath = r"s:\escape holidays\original_site\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace names
content = content.replace("Skyscape Holidays", "Escape Holidays")
content = content.replace("SKYSCAPE", "ESCAPE")
content = content.replace("Skyscape", "Escape")

# Replace Links/Emails
content = content.replace("skyscapeholidays.com", "escapeholidays.com")
content = content.replace("info@escapeholidays.com", "escapeholidays@gmail.com")

# Replace Phone Numbers
content = content.replace("9876543210", "9080066983")
content = content.replace("98765 43210", "9080066983")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Details updated successfully!")
