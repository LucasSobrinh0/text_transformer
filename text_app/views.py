from django.shortcuts import render, redirect

def index(request):
    if request.method == "POST":
        text = request.POST.get("text", "")
        operation = request.POST.get("operation", "")

        if operation == "uppercase":
            result = text.upper()
        elif operation == "lowercase":
            result = text.lower()
        elif operation == "capitalize":
            result = text.capitalize()
        elif operation == "title":
            result = text.title()
        elif operation == "reverse":
            result = text[::-1]
        else:
            result = text

        # Armazenar o texto original e o resultado na sessão
        request.session['original_text'] = text
        request.session['result'] = result

        # Redirecionar para a mesma página
        return redirect('index')

    # Tentar recuperar o texto original e o resultado da sessão se disponível
    original_text = request.session.get('original_text', '')
    result = request.session.get('result', '')
    return render(request, "index.html", {'result': result, 'original_text': original_text})
