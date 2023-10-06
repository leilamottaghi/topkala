
from .models import Category

def global_categories(request):
    main_categories = Category.objects.filter(parent=None).exclude(title="شگفت‌انگیزها")
    sub_categories = Category.objects.filter(parent__isnull=False)
    amazing_category = Category.objects.get(title="شگفت‌انگیزها")
    
    return {
        'main_categories': main_categories,
        'sub_categories': sub_categories,
        'amazing_category': amazing_category,
    }
