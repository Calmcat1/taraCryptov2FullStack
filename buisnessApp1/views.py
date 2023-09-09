from django.shortcuts import render, get_object_or_404
from .models import blogHeadlineTable, productsTable
from django.db.models import Max

# Create your views here.

# homepage
def home(request):
    
    context = {
        
    }

    return render(request, 'home.html', context)

#blogpage
def blogs(request):
    
    queryset = blogHeadlineTable.objects.all()
    
    context = {
        'queryset' : queryset
    }

    return render(request, 'blogs.html', context)

#productspage
def products(request):

    queryset = productsTable.objects.all()
    
 

    context = {
        'queryset' : queryset
    }

    return render(request,'products.html',context)


#feedback page
def feedback(request):

    context = {

    }
    return render(request, 'feedback.html', context)


# blogcontent page
def blogContent(request, id):

    query = get_object_or_404(blogHeadlineTable, id=id)
    maximum_id = blogHeadlineTable.objects.latest('id').id
    

    context = {
        'query' : query,
        'query_max_id' : maximum_id
    }

    return render(request, 'blogContent.html', context)


# productsContent
def productContent(request, id):

    query = get_object_or_404(productsTable, id=id)
    maximum_id = blogHeadlineTable.objects.latest('id')
    max_val = maximum_id.id

    context = {
        'query' : query,
        'query_max_id' : max_val
    }
   

    return render(request, 'productsContent.html', context)
