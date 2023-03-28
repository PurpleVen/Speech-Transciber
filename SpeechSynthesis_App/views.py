from django.shortcuts import render

# Create your views here.


# def speech_to_text(request):
#     # code to implement speech-to-text functionality
#     # store the result in a backend variable
#     text = "This is the text that was converted from speech."
#     return render(request, 'SpeechSynthesis.html', {'text': text})

def speech_to_text(request):
    return render(request, 'SpeechSynthesis.html')

