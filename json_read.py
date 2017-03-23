import json
import collections


d = collections.defaultdict(int)

with open('newsafr.json', encoding='utf-8') as newsafr:
 data_newsafr = json.load(newsafr)
 dictlist_newsafr = []
 for key, value in data_newsafr.items():
  for c in value['channel']['item']:
    for i in c['description']['__cdata'].split(" "):
      if len(i) > 6:
       d[i] += 1
      else:
        continue



newsafr = sorted(d.items(), key=lambda x: x[1], reverse=True)[0:10]

d = collections.defaultdict(int)

with open('newscy.json', encoding='utf-8') as newscy:
 data_newscy = json.load(newscy)
 dictlist_newscy = []
 for key, value in data_newscy.items():
  for c in value['channel']['item']:
    for i in c['description']['__cdata'].split(" "):
      if len(i) > 6:
       d[i] += 1
      else:
        continue

newscy = sorted(d.items(), key=lambda x: x[1], reverse=True)[0:10]

d = collections.defaultdict(int)

with open('newsfr.json', encoding='utf-8') as newsfr:
 data_newsfr = json.load(newsfr)
 dictlist_newsfr = []
 for key, value in data_newsfr.items():
  for c in value['channel']['item']:
    for i in c['description']['__cdata'].split(" "):
      if len(i) > 6:
       d[i] += 1
      else:
        continue

newsfr = sorted(d.items(), key=lambda x: x[1], reverse=True)[0:10]

d = collections.defaultdict(int)

with open('newsit.json', encoding='utf-8') as newsit:
 data_newsit = json.load(newsit)
 dictlist_newsit = []
 for key, value in data_newsit.items():
  for key_under, name in value['channel'].items():
    for i in name:
      if len(i) > 6:
       d[i] += 1
      else:
        continue

newsit = sorted(d.items(), key=lambda x: x[1], reverse=True)[0:10]

print('10 самых часто употребляемых слов из файла newsafr.json: ', newsafr)
print('\n10 самых часто употребляемых слов из файла newscy.json: ', newscy)
print('\n10 самых часто употребляемых слов из файла newsfr.json: ', newsfr)
print('\n10 самых часто употребляемых слов из файла newsit.json: ', newsit)