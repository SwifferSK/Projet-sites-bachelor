from django.shortcuts import render, get_object_or_404
from .models import Project


def index(request):
    return render(request, 'index.html')


def project_det(request, slug):
    project = get_object_or_404(Project, slug=slug)
    projects = Project.objects.all()
    if project:
        auth = project.author.username
        if auth[0].lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
            author = f"d'{auth}"
        else:
            author = f"de {auth}"

    context = {'project': project,
               'title': project.title,
               'author': author,
               'projects': projects}

    return render(request, 'project_detail.html', context)
