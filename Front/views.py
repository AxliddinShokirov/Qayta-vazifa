from django.shortcuts import render,redirect
from . import models

def front(request):

    products=models.Product.objects.all()
    catgory=models.Category.objects.all()
    contact=models.Contact.objects.last()
    info=models.Info.objects.all()
    img=models.Banner.objects.last()
    gym=models.Gym.objects.all()
    gyms=models.Gym.objects.last()
    reja=models.Reja.objects.last()
    banner=models.Banner.objects.all()
    
 
   
    
    return render(request, 'front/index.html', { 'products': products , 'catgory': catgory,
                                                 'contact': contact, 'info': info, 'img': img, 'gym': gym, 
                                                 'gyms': gyms,'reja': reja, 'banner': banner})
def coach(request):
    coach=models.Coach.objects.all()
    return render(request, 'front/coach/coach.html', {'coach': coach})

# def 
# 





