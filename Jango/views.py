from django.shortcuts import render

def index(request):
    people = Person.objects.all()
    context = {
        'people': people,
    }
    return render(request, 'index.html', context)