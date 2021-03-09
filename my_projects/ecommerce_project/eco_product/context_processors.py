from .models import Category

def menu_category(request):
    categories = Category.objects.all()
    return {'menu_categories':categories}