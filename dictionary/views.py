from django.shortcuts import render, redirect
from PyDictionary import PyDictionary
from django.contrib import messages
import enchant
import requests, json
# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):
    if request.method == "POST":
        search = request.POST['search']
        search = search.lower()
        response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+search)
        obj = response.json()
        """dictionary = PyDictionary()
        meaning = dictionary.meaning(search)
        synonyms = dictionary.synonym(search)
        print(synonyms)
        antonyms = dictionary.antonym(search)"""
        meaning = json.dumps(obj[0]["meanings"][0]["definitions"][0]["definition"], sort_keys=True)
        synonyms = []
        for d in obj[0]["meanings"][0]["definitions"]:
            for dd in d["synonyms"]:
                synonyms.append(json.dumps(dd))
                if len(synonyms)==5:
                    break
            if len(synonyms)==5:
                break
        antonyms = []
        for d in obj[0]["meanings"][0]["definitions"]:
            for dd in d["antonyms"]:
                antonyms.append(json.dumps(dd))
                if len(antonyms)==5:
                    break
            if len(antonyms)==5:
                break
        context = {
            'meaning': meaning,
            'synonyms': synonyms,
            'antonyms': antonyms
        }
        return render(request, 'word.html', context)
    else:
        return render(request, 'index.html')
    
     