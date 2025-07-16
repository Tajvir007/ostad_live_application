from django.shortcuts import render

# Create your views here.
def manage_club(request):
    return render(request, 'superadmin/others/manage-clubs.html')