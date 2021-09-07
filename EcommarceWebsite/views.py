from django.shortcuts import render
from EcommarceWebsite.models import Information

# Create your views here.
def displayData(request):
    return render(request,'home.html')

def dataDisplayone(request):
    all_data=Information.objects.all()

    if request.method == "POST":
        search_data = request.POST.get('search')
        print(search_data)

        if search_data != '' and search_data is not None:
            all_data=all_data.filter(name_exact =search_data)
            #print(all_data)

    context = {
        'all_data':all_data
    }

    return render(request,'home.html',context)

def Checkout(request):
    return render(request,'checkout.html')