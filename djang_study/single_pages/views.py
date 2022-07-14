from django.shortcuts import render


# Create your views here.
def loading(request):
    return render(
        request,
        'single_pages/loading.html'
    )


def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )