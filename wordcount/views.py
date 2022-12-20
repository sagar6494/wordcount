from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    word_dic = {}
    for word in wordlist:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    sortedlist = sorted(word_dic.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltxt':fulltext, 'count':len(wordlist), 'sortedlist':sortedlist}) 


def about(request):
    return render(request, 'about.html') 