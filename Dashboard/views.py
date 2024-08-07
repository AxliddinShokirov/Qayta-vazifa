from django.shortcuts import render
from Front import models
from django.shortcuts import render ,redirect

# Create your views here.
def dashboard(request):

    return render(request, 'dashboard/index.html')
def Blog_name(request):
    blogs = models.Blog_name.objects.last()
    context = {}
    context['blogs'] = blogs
    return render(request, 'dashboard/base.html', context)




def bannercrud(request):
    banners=models.Banner.objects.all()
    return render(request, 'deshboard/banner.html', {'banners':banners})
from django.shortcuts import render, redirect



def listBanner(request):
    banners = models.Banner.objects.all()
    context = {}
    context['banners'] = banners

    return render(request, 'dashboard/banner/bannerlist.html', context)





def createBanner(request):
    if request.method == 'POST':
        print("JKJKASJKJKAFJKAJKJKJKJK",request.FILES.get('img'))
        banner = models.Banner.objects.create(
            title = request.POST['title'],
            sub_title = request.POST['sub_title'],
            img = request.FILES.get('img')
        )
        return redirect('listbanner')
    return render(request, 'dashboard/banner/create.html')


def updateBanner(request, id):
    data = models.Banner.objects.get(id=id)

    context = {
        'data': data
    }

    if request.method == 'POST':
        data.title = request.POST.get('title', data.title)
        data.sub_title = request.POST.get('sub_title', data.sub_title)
        img_file = request.FILES.get('image')
        data.img = img_file
        
        for key, value in request.FILES.items():
            print(f'File key: {key}, File: {value}')

        data.save()
        return redirect('listbanner')
    
    return render(request, 'deshboard/crude/banner/update.html', context)




def deleteBanner(request, id):
    models.Banner.objects.get(id=id).delete()
    return redirect('listbanner')

# list +-+-
# detail +-+-
# create +-+-
# update +-+-
# delete +-+-


def listCategory(request):
    queryset = models.Category.objects.all()
    context = {}
    context['queryset'] = queryset

    return render(request, 'dashboard/Category/category_list.html', context)


def detailCategory(request, id):
    queryset = models.Category.objects.get(id=id)
    context = {}
    context['queryset'] = queryset

    return render(request, 'deshboard/crude/category/detail.html', context)


def createCategory(request):
    if request.method == 'POST':
        models.Category.objects.create(
            name=request.POST['name'],
            title=request.POST['title'],
            image=request.POST['img']

        )
        return redirect('category_list')
    return render(request, 'dashboard/Category/category_creat.html')


def updateCategory(request, id):
    vegi = models.Category.objects.get(id=id)

    context = {
        'vegi': vegi
    }

    if request.method == 'POST':
        vegi.name = request.POST['name']
        vegi.save()
        return redirect('listCategory')
    return render(request, 'deshboard/crude/category/detail.html', context)



def deleteCategory(request, id):
    models.Category.objects.get(id=id).delete()
    return redirect('category_list') 


# list ---
# detail ---
# create ---
# update ---
# delete ---


def listGym(request):
    queryset = models.Gym.objects.all()
    context = {}
    context['queryset'] = queryset
    return render(request, 'dashboard/Prodact/prodact_list.html',context)


def detailProduct(request, id):
    queryset = models.Product.objects.get(id=id)
    print('queryset',queryset )
    print('id', id)
    # querysetImg = models.ProductImg.objects.filter(product_id = id)
    context = {}
    context['queryset'] = queryset
    # context['querysetImg'] = querysetImg
    # context['images'] = models.ProductImg.objects.filter(product=queryset)
    return render(request, 'back-office/product/detail.html',context)


def createGym(request):
    context = {}
    context['categorys'] = models.Gym.objects.all()
    if request.method == 'POST':
        models.Gym.objects.create(
            name = request.POST['name'],
            title = request.POST['title'],
            image=request.FILES.get('image')
         
          
        )

        # images = request.FILES.getlist('images')

        # for image in images:
        #     models.ProductImg.objects.create(
        #         img = image,
        #         product = product
        #     )
        # return redirect('listProduct')
    return render(request, 'dashboard/Prodact/prodact.html', context)


def deleteGym(request, id):
    models.Gym.objects.get(id=id).delete()
    return redirect('listGym')

