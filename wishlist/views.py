from django.shortcuts import render
from wishlist.models import ItemWishlist
data_wishlist_item = ItemWishlist.objects.all()
context = {
    'list_item': data_wishlist_item,
    'JulianJustin': 'Cinoy'
    
}

# Create your views here.
def show_wishlist(request):
    return render(request, "wishlist.html", context)