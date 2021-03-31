from django.shortcuts import render

# Create your views here.


def index_view(request):
    return render(request, 'index.html')


def comment_create_view(request):
    if request.method == 'GET':
        return render(request, 'comment_create.html')
    elif request.method == 'POST':
        num1 = int(request.POST.get("num1"))
        num2 = int(request.POST.get("num2"))
        action = request.POST.get("action")
        if action == "+":
            result = f'{num1} + {num2} = {num1 + num2}'
        elif action == "-":
            result = f'{num1} - {num2} = {num1 - num2}'
        elif action == "*":
            result = f'{num1} * {num2} = {num1 * num2}'
        elif action == "/":
            result = f'{num1} / {num2} = {num1 / num2}'
        else:
            result = f'some mistake occured'

        return render(request, 'comment_create.html', {'result': result})
