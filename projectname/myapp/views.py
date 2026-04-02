from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Candidate

  
from django.shortcuts import render, get_object_or_404
from .models import Candidate

def student_detail(request, id):
    student = get_object_or_404(Candidate, id=id)
    return render(request, 'student_list.html', {'student': student})