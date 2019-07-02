from django.shortcuts import render
from projects.models import Project

'''
An index view that shows a snippet of information about each project
'''
def project_index(request):
    projects = Project.objects.all() # query: retriving all objects in the projects table
    
    '''
    Every view function you create needs to have a context dictionary.
    The context dictionary is used to send information to our template.
    '''
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


'''
A detail view that shows more information on a particular topic
'''
def project_detail(request, pk):
    project = Project.objects.get(pk=pk) # query: retriving object with primary key equal to pk
    
    '''
    Every view function you create needs to have a context dictionary.
    The context dictionary is used to send information to our template.
    '''
    context = {
        'projects': project
    }
    return render(request, 'project_detail.html', context)

