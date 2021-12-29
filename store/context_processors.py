from .models import Category


def categories(request):    
    return {                
        'categories': Category.objects.all()
    }
# this view will available on every page. 
#Check settings.py->template->options->store.context_processors.categories    