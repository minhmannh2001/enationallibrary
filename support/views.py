from django.shortcuts import render


def hour_location(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    return render(request, 'hour_location.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user,})
