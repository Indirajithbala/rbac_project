from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Role, Permission

def index(request):
    users = User.objects.all()
    roles = Role.objects.all()
    permissions = Permission.objects.all()
    return render(request, 'index.html', {
        'users': users,
        'roles': roles,
        'permissions': permissions,
    })

def assign_role(request):
    user_id = request.POST.get('user_id')
    role_id = request.POST.get('role_id')
    user = User.objects.get(id=user_id)
    role = Role.objects.get(id=role_id)
    user.roles.add(role)
    return JsonResponse({'success': True})

def assign_permission(request):
    role_id = request.POST.get('role_id')
    permission_id = request.POST.get('permission_id')
    role = Role.objects.get(id=role_id)
    permission = Permission.objects.get(id=permission_id)
    role.permission_set.add(permission)
    return JsonResponse({'success': True})
