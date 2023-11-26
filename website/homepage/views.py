from django.shortcuts import render


def main(request):
    template = 'homepage/main.html'

    context = {
    }
    return render(request, template, context)
