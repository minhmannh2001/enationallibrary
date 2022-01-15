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


def support_catalog(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    return render(request, 'support/support-catalog.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user
    })


def support_contactUs(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    return render(request, 'support/support-contactUs.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user
    })


def support_libraryFees(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    return render(request, 'support/support-libraryFees.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user
    })


def support_renewals(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    return render(request, 'support/support-renewals.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user
    })


def support_wrapper(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    return render(request, 'support/support-wrapper.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user
    })


def support_card(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    return render(request, 'support/support-card.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user
    })