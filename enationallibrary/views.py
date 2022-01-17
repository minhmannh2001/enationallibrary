from django.shortcuts import render


def page_not_found_view(request, exception):
    return render(request, '404_page.html', status=404)


def server_error_view(request):
    return render(request, '500_page.html', status=500)