from django.shortcuts import render
from django.views import View
# Create your views here.



class AboutView(View):
    def get(self, request):
        return render(request, 'topkalaMag/about.html')


class CategoriesView(View):
    def get(self, request):
        return render(request, 'topkalaMag/categories.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'topkalaMag/contact.html')


class IndexView(View):
    def get(self, request):
        return render(request, 'topkalaMag/index.html')


class SearchResultsView(View):
    def get(self, request):
        return render(request, 'topkalaMag/search-results.html')


class SinglePostView(View):
    # def get(self, request, pk):
    #     post = YourModelName.objects.get(pk=pk)  # Replace 'YourModelName' with the actual name of your model
    #     return render(request, 'your_template_name.html', {'post': post})
    def get(self, request):
        return render(request, 'topkalaMag/single-post.html')


class Error404View(View):
    def get(self, request):
        return render(request, 'topkalaMag/404.html')
