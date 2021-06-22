from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args, **kwargs):
            
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
        
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('No estas autorizado para ver esta página')
        return wrapper_func
    return decorator

def check_group(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
        if group == 'secretaria':
            return redirect('home')
        
        if group == 'medico':
            return redirect('home')
        
        if group == 'paciente':
            return redirect('home')
        
        if group == 'admin':
            return redirect('admin')
        
    return wrapper_function