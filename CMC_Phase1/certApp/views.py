from django.shortcuts import render, redirect
from certApp.models import Certificate
from certApp.forms import CertificateForm

# Create your views here.
def displayCertificate(request):
    certificate = Certificate.objects.all()
    return render(request, 'certApp/display.html', {'certificate':certificate}) #context = {'student':student}

def addCertificate(request):
    form = CertificateForm()
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/output')
    return render(request, 'certApp/create.html',{'form':form})

def getCertificate(request):
    pass

def deleteCertificate(request):
    certificate = Certificate.objects.get(id=id)
    certificate.delete()
    return redirect('/output')

def updateCertificate(request, id):
    certificate = Certificate.objects.get(id=id)
    if request.method == 'POST':
        form = CertificateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/output')
    return render(request, 'certApp/update.html', {'certificate':certificate})
