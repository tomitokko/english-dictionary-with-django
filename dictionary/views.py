from fnmatch import translate
from django.shortcuts import render
from PyMultiDictionary import MultiDictionary, DICT_EDUCALINGO

# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')
    dictionary = MultiDictionary(search)
    dictionary.set_words_lang('en')
    meaning = dictionary.get_meanings(dictionary=DICT_EDUCALINGO)
    synonyms = dictionary.get_synonyms()
    antonyms = dictionary.get_antonyms()
        
    context = {
        'search': search,
        'meaning': meaning[0][0:2], # just made view for meaning from list 0 until 1
        'synonyms': synonyms[0][0:5], # just show 5 words as synonim
        'antonyms': antonyms[0][0:5], # just show 5 words as antonyms
    }

    return render(request, 'word.html', context)
