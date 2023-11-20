import re

regex_1 = r"[a{1}]"

test_str = "In the digital realm, creativity knows no bounds. Coders, designers, and artists alike embark on a journey to shape the future. Whether it's crafting intricate algorithms or painting vibrant landscapes, the world of technology and art converges. Every line baa of code, every stroke of the brush, begins with a spark of imagination. In this vast landscape, where possibilities unfold, the creative mind takes the lead. Welcome to the intersection of innovation and expression, where the journey begins with the click of a key or the stroke of a pen.bag cowwwwwwaaaaasdsasasd"

matches = re.finditer(regex_1, test_str)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

