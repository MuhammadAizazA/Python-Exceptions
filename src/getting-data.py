import re

regex=r":\s([A-Za-z_-]+[\w]+)\s*[\w]+:\s*(\d{8})\s*[\w]+:\s*\$([\w.]*)"

text="""
Product: Laptop_2021 Code: 12345678 Price: $899.99
Product: Mouse-2022   Code: 98765432 Price: $15
Product: Keyboard_001 Code: 87654321 Price: $29.95
Product: Monitor-XYZ  Code: 13579024 Price: $399.50
Product: Smartphone-7 Code: 24680135 Price: $599.99
Product: Headphones42 Code: 11223344 Price: $49.99
Product: Camera_XYZ   Code: 55443322 Price: $199.75
Product: Printer_2023 Code: 77889900 Price: $129.50
Product: Tablet-A1    Code: 33221100 Price: $199
Product: Speaker-3    Code: 66554433 Price: $79.99
"""
data=re.findall(regex,text)


for x in data:
    print(f"Product Name is: {x[0]}\tProduct Code: {x[1]}\tPrice is: ${x[2]}")