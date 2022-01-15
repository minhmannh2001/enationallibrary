from django.shortcuts import render


def services_wrapper(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    return render(request, 'services/services-wrapper.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user
    })


def services_pickup(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    return render(request, 'services/services-pickup.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user
    })


def services_reserveRoom(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    return render(request, 'services/services-reserveRoom.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user
    })


def services_historyRoom(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    return render(request, 'services/services-historyRoom.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user
    })