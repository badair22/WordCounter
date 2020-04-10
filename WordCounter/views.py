from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    entertext = request.GET['entertext']
    wordlist = entertext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #increse
            worddictionary[word] += 1
        else:
            #Add
            worddictionary[word] = 1

        sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'entertext':entertext, 'count':len(wordlist), 'sortedwords':sortedwords})
