import json
import re
text_file = open("sample.txt", "w")
with open('data.json') as json_file:
    data = json.load(json_file)
    for p in data['creation']:
        creation_name = p['title']
        for creator in re.split(', |und',p['creator_name']):
            text_file.write('text: Wer hat "'+ creation_name+ '" erstellt?\tlabels: '+ creator+"\t\n")

