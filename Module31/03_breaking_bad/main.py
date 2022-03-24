import json
import requests
result = requests.get('https://www.breakingbadapi.com/api/deaths')
text = json.loads(result.text)
with open('episode.json','w') as file:
    json.dump(text[63],file,indent=4)
with open('episode.json','r') as j_file:
    for i in j_file.readlines():
        print(i,end='')




