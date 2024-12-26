# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

import re  # Importing the regex module

pattern = r"hello"  # Matching the exact string "hello"
text = "hello world"

match = re.match(pattern, text)  # Searches for the pattern in the text
if match:
    print("Found:", match.group())  # Output the matched portion
else:
    print("No match found")

#re.search(): Searches the entire string for a match.

match=re.search(pattern,text)

if match:
    print("Founded here:", match.group())  # Output the matched portion
else:
    print("No match found")

#dot(a.b) means this will match string which is a to b
pattern1 = r"i.*z"  # Matches 'i', zero or more characters, and 'z'
text1 = "Minhaz Uddin Minhaz"

matches = re.findall(pattern1, text1)  # Returns all matches as a list
if matches:
    print("Found here:", matches)  # Output the matched portions
else:
    print("No match found")

#match digits (\d)

pattern2=r"\d+" # Matches one or more digits
text2="ROOM 123, FLOOR 4,BUILDING 132"
matches=re.findall(pattern2,text2)
print(matches)
 
 #Match Word Characters (\w)
pattern3=r"\w+"
text3="Hello this is Minhaz"

matches=re.findall(pattern3,text3)
print(matches)

# ^: Matches start of the string

pattern4=r"^Hello"
text4="Hello World"

matches=re.search(pattern4,text4)
if matches:
    print(bool(matches))

# $: Matches end of the string
pattern5=r"Minhaz$"
text5="Minhaz Uddin Minhaz"

matches=re.search(pattern5,text5)
print(bool(matches))

