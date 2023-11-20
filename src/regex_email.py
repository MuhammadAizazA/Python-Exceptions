import re

regex = r"^[\w.]+@[A-Za-z]+\.[A-Za-z]+"

test_str = ("john.doe@example.com\n"
	"alice_smith123@gmail.com\n"
	"support@company.net\n"
	"contact_us@webpage.org\n"
	"sales.team@ecommerce-shop.com\n"
	"info+feedback@example.co.uk\n"
	"user123@subdomain.example\n"
	"marketing@company-name.biz\n"
	"webmaster@website.info\n"
	"social.media@socialnetwork.com")

matches = re.finditer(regex, test_str,flags=re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))


if __name__=="__main__":
    while(True):
        email=input("Enter email to check validity: ")
        if re.match(regex, email):
            print(f"{email} is a valid email address.")
        else:
            print(f"{email} is not a valid email address.")
        if email==('q' or 'Q'):
            break
