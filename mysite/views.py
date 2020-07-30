from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index2.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    if removepunc == "on":
        analyzed=""
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        params={"purpose":"removed punctuations","analyzed_text":analyzed}
        djtext=analyzed
        # return render(request, 'analyze2.html' ,params)

    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {"purpose": "Change To Uppercase", "analyzed_text": analyzed}
        djtext=analyzed
        # return render(request, 'analyze2.html', params)

    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed=analyzed+char.upper()
        params = {"purpose": "New Line Removed", "analyzed_text": analyzed}
        djtext=analyzed
        # return render(request, 'analyze2.html', params)

    if extraspaceremover=="on":
        analyzed=""
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {"purpose": "Extra space Removed", "analyzed_text": analyzed}
        djtext=analyzed


    if(removepunc != "on" and fullcaps !="on" and newlineremover!="on" and extraspaceremover!="on"):
        return HttpResponse("Please select any operation and try again")

    return render(request, 'analyze2.html', params)