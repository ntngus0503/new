from django.shortcuts import render
import random



def baseball(request):
    return render(request, 'baseball.html')

def baseballresult(request):
    full_text = request.GET['fulltext']

    word_list = full_text.split()

    lotto = random.sample(range(0,5),4)

    strike = 0
    ball = 0


    for i in range(0,4):
        if word_list[i] == str(lotto[i]):
            strike += 1
        for a in range(0,4):
            if word_list[a] == str(lotto[i]) and a != i: #그냥 a와 i는 숫자를 포함한 개념으로 보임
                ball += 1

    return render(request, 'baseballresult.html', {'fulltext' : full_text, 'split' : word_list, 'strike' : strike, 'ball' : ball})
