from django.shortcuts import render, redirect
from .forms import UploadFileForm, DrawFruit
from .model import miModelo
from .models import Images
# Create your views here.


def index(request, name="Mundo"):
    return(
        render(request, "index.html",{
            "name" : name
        })
    )

def uploadImage(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            top3, metadataC = miModelo.predictImg(request.FILES['image'].file, decoded=True)
            Images.objects.create(name=request.POST["name"], image= metadataC, predict=top3[0][0])
            return showResults(request, top3, metadataC)
    else:
        form = UploadFileForm()
    return render(request, 'uploadImage.html', {'form': form})


def showResults(request, top3, img):
    return render(request, 'results.html', {
        'top3' : top3,
        'img' :  img
    })

def paint(request):
    if request.method == "POST":
        form = DrawFruit(request.POST)
        if form.is_valid():
            metadata = request.POST['metadata']
            top3 = miModelo.predictImg(metadata)
            Images.objects.create(name = request.POST['name'], image=metadata, predict=top3[0][0])
            return showResults(request, top3, metadata)
    else:
        form = DrawFruit()

    return render(request, 'paint.html', {
        "form" : form
    })