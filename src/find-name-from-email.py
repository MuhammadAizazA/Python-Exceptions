import re

pattern="https://twitter.com/([\w]+)"

text="""
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
"""

list_of_emails=re.findall(pattern,text)

print(list_of_emails)