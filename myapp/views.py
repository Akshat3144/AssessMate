from django.shortcuts import render,redirect
from .models import UploadedFile
from django.contrib import messages
from .forms import Fileform
from django.http import JsonResponse
from . import core2


from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def MU(request):
    return render(request,'MU.html')

def EMA(request):
    return render(request,'EMA.html')

def register(request):
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']

def feedback(request):
    return render(request,"Feedback.html")

def assignment(request):
    return render(request,"Assignments.html")

def login(request):
    return render(request,"pages-login.html")

def register(request):
    return render(request,"pages-register.html")

def random(request):
    text = request.POST['text']
    return render(request,'random.html')

def profile(request):
    return render(request,'users-profile.html')

def my_function(request):
    files = UploadedFile.objects.all()
    result = core2.rein_force(files[0],files[1],files[2])
    return JsonResponse({'result':result})

def plagerism(request):
    return render(request,'plagerism.html')


def teaching(request):
    if request.method == 'POST':
        form = Fileform(request.POST, request.FILES)
        if form.is_valid():
            form.save()


    context = {'form': Fileform()}
    return render(request,'teaching.html',context)

# def upload_form(request):
#
#     return render(request,'teaching.html',context)

def upload_pdf(request):
    if request.method == 'POST':
        pdf_file = request.FILES.get('pdf_upload')
        # Additional validation (optional)
        if pdf_file and pdf_file.content_type == 'application/pdf':
            # Save the uploaded file
            new_file = UploadedFile(file=pdf_file)
            new_file.save()
            messages.success(request, 'PDF uploaded successfully.')
            return redirect('upload_pdf')  # Redirect to same page after success
        else:
            messages.error(request, 'Invalid file format. Please upload a PDF file.')

    context = {}
    return render(request, 'upload_pdf.html', context)

def list_files(request):
    files = UploadedFile.objects.all()
    context = {'dogs':files}
    return JsonResponse(context)

def performance(request):
    return render(request, 'performance.html')

def attend(request):
    return render(request, 'Attendence.html')