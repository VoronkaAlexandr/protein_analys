import requests
url = 'https://www.uniprot.org/uniprot/Q7Z2W4'

BASE = 'http://www.uniprot.org'
KB_ENDPOINT = '/uniprot/'

payload = {'query': 'Q7Z2W4',
            'format': 'tab',
            'columns': 'id,entry_name,sequence,feature(BETA STRAND),feature(HELIX),feature(TURN),comment(SIMILARITY)'}
result = requests.get(BASE + KB_ENDPOINT, params=payload)
f = open('proteinQ7Z2W4.xlsx', 'w')
if result.status_code == 200:
    f.write(result.text)
else:
    print('Что-то пошло не так, в прочем как обычно')
f.close()

payload2 = {'query': 'name:"antiviral" AND taxonomy:HUMAN AND keyword:"Zinc-finger [KW-0863]"',
            'format': 'list'}
result2 = requests.get(BASE + KB_ENDPOINT, params=payload2)
f2 = open('zincfing.txt', 'w')
if result2.status_code == 200:
    print(result2.text)
    f2.write(result2.text)
else:
    print('Что-то пошло не так, в прочем как обычно')
f2.close()