from django.shortcuts import render, redirect
from .models import Categories, ReadMore


def index(request):
    category = request.GET.get('category')
    if category == None:
        photos = ReadMore.objects.all()
    else:
        photos = ReadMore.objects.filter(category__name__contains = category)

    categories = Categories.objects.all()

    dic = {'categories' : categories, 'photos': photos}
    return render(request, 'photos/index.html', dic)


def readmore(request, pk):
    return render(request, 'photos/readmore.html')


def add(request):
    categories = Categories.objects.all()

    if request.method == "POST":
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Categories.objects.get(id=data['category'])
        else:
            category = None

        photo = ReadMore.objects.create(
            category = category,
            text = data['description'],
            image = image,
        )

        return redirect('index')

    dic = {'categories': categories}
    return render(request, 'photos/add.html', dic)



