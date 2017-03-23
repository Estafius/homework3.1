import json
import collections


d = collections.defaultdict(int)

list_file = ['newsafr.json','newscy.json','newsfr.json','newsit.json']

for file in list_file:
 with open(file, encoding='utf-8') as json_content:
  data_file = json.load(json_content)
  dictlist_file = []
  if file != 'newsit.json':
   for key, value in data_file.items():
    for c in value['channel']['item']:
     for i in c['description']['__cdata'].split(" "):
       if len(i) > 6:
        d[i] += 1
       else:
        continue
  else:
    for key, value in data_file.items():
     for key_under, name in value['channel'].items():
      for i in name:
       if len(i) > 6:
        d[i] += 1
       else:
         continue
 top_10 = sorted(d.items(), key=lambda x: x[1], reverse=True)[0:10]
 print('\n10 самых часто употребляемых слов из файла ',file,': ', top_10,'\n')
