import requests

r = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en_US/set')
my_obj = r.json()

for i in my_obj[0]['meanings']:
    print(f"part of speech: {i['partOfSpeech']}")
    for definition in i['definitions']:
        if key == "definition": 
            print(value)
        elif key == "example":
            print(value)
        elif key == "synonyms":
            for synonym in synonyms:
                print(synonym)
        else:
            pass
    

{'partOfSpeech': 'noun', 
'definitions': [
    {'definition': 'An utterance of “hello”; a greeting.',
    'synonyms': ['greeting', 'welcome', 'salutation', 'saluting', 'hailing', 'address', 'hello', 'hallo'], 
    'example': 'she was getting polite nods and hellos from people'
    }
    ]
}