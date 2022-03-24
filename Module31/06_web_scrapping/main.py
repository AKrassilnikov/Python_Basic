
import re
import requests
result = requests.get('http://www.columbia.edu/~fdc/sample.html')
text = result.text
with open("file.txt",'w') as file:
    file.write(text)
headers = []
with open("file.txt",'r') as file:
    for string in file:
        if string.startswith("<h3 id"):
            result = re.findall(r'>(.*?)<',string)
            print(result)



