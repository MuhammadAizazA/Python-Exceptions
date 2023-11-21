import re

pattern=r'FY\d{4} (?:Q\d|S\d)[^\w]+[\w]+[^\w]+[\d]*(?:\.[\d]+)?(?:\s+(?!was\b)\S)?(?!\S)'

text="""
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.*-
"""

catogories=re.findall(pattern,text)


print(catogories)

