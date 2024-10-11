from .models import *

def common_context(request):
    home = Home.objects.all()
    category = Category.objects.all()
    return {
        'home': home,
        'category': category
    }
