from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import JobApplicationForm
from .models import JobApplication
from django.db.models import Q
from django.core.paginator import Paginator




# def landing_page(request):
#     """Landing page view"""
#     if request.user.is_authenticated:
#         return redirect('dashboard')
#     return render(request, 'landing.html')

@login_required
def job_list(request):
    q = request.GET.get("q")
    status = request.GET.get("status")

    jobs = JobApplication.objects.filter(owner=request.user).order_by("-created_at")

    if q:
        jobs = jobs.filter(
            Q(company__icontains=q) |
            Q(role__icontains=q)
        )

    if status:
        jobs = jobs.filter(status__iexact=status)

    paginator = Paginator(jobs, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "applications/job_list.html",
        {
            "page_obj": page_obj,
        }
    )





    jobs = JobApplication.objects.filter(owner = request.user).order_by('-created_at')
    return render(request,'applications/job_list.html',{'jobs':jobs})






@login_required
def job_create(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.owner = request.user
            job.save()
            return redirect('job_list')
        else:
            print(form.errors)
    else:
        form = JobApplicationForm()

    return render(request, 'applications/job_form.html', {
        'form': form
    })



# this part is for the editing the job  crud operation == edit

def  edit_job (request,pk):
    job = get_object_or_404(JobApplication,pk = pk , owner = request.user)

    if request.method == "POST":
        form = JobApplicationForm(request.POST, request.FILES, instance=job)

        if form.is_valid():
            form.save()
            return redirect("job_list")
    else:
        form = JobApplicationForm(instance=job)

    return render(request, "applications/edit_job.html",{"form":form,"job":job})



# for deleting the job

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import JobApplication


@login_required
def delete_job(request, pk):
    job = get_object_or_404(
        JobApplication,
        pk=pk,
        owner=request.user
    )

    if request.method == "POST":
        job.delete()
        return redirect("job_list")

    return render(
        request,
        "applications/delete_job_confirm.html",
        {"job": job}
    )



#  to see the job detail view

@login_required
def job_detail(request, pk):
    job = get_object_or_404(JobApplication, pk=pk, owner=request.user)
    return render(request, 'applications/job_detail.html', {'job': job})




@login_required
def dashboard(request):
    user_jobs = JobApplication.objects.filter(owner=request.user)

    total_jobs = user_jobs.count()

    status_counts = {
        "applied": user_jobs.filter(status__iexact="applied").count(),
        "interview": user_jobs.filter(status__iexact="interview").count(),
        "offer": user_jobs.filter(status__iexact="offer").count(),
        "rejected": user_jobs.filter(status__iexact="rejected").count(),
    }

    return render(
        request,
        "applications/dashboard.html",
        {
            "total_jobs": total_jobs,
            "status_counts": status_counts,
        }
    )
