from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404

# Create your views here.
def imagedetails(request,image_id):
    comments=Comment.objects.filter(image_id=image_id)


    try:
        image = Image.objects.get(id=image_id)
    except ObjectDoesNotExist:
         raise Http404()
    return render(request,"image.html",{"image":image,"comments":comments})