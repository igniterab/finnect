from django.shortcuts import render , redirect
from .forms import UserRegisterForm , UserUpdateForm ,ProfileUpdateForm ,ProfileUpdateForma,ProfileUpdateFormb ,ProfileUpdateFormc ,ProfileUpdateFormd
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'{username} your account has been created !, Kindly login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'accounts/register.html',{'form':form})



#User must be logged in to view this profile page that whats decorater do 
@login_required
def profile(request):
    return render(request,'accounts/profile.html')

@login_required
def profileupdate(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST , instance=request.user)
        p_form = ProfileUpdateForm(request.POST ,request.FILES , instance=request.user.profile)
        p_forma = ProfileUpdateForma(request.POST ,request.FILES , instance=request.user.profile)
        p_formb = ProfileUpdateFormb(request.POST ,request.FILES , instance=request.user.profile)
        p_formc = ProfileUpdateFormc(request.POST ,request.FILES , instance=request.user.profile)
        p_formd = ProfileUpdateFormd(request.POST ,request.FILES , instance=request.user.profile)
        
        
        if u_form.is_valid() and p_form.is_valid() and p_forma.is_valid() and p_formb.is_valid() and p_formc.is_valid() and p_formd.is_valid():
            u_form.save()
            p_form.save()
            p_forma.save()
            p_formb.save()
            p_formc.save()
            p_formd.save()
            
            messages.success(request,'your profile has been updated !')
            return redirect('profile')


    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        p_forma = ProfileUpdateForma(instance=request.user.profile)
        p_formb = ProfileUpdateFormb(instance=request.user.profile)
        p_formc = ProfileUpdateFormc(instance=request.user.profile)
        p_formd = ProfileUpdateFormd(instance=request.user.profile)
        
    context = { 'u_form':u_form , 'p_form':p_form, 'p_forma':p_forma, 'p_formb':p_formb, 'p_formc':p_formc, 'p_formd':p_formd }
    return render(request,'accounts/profile_update.html',context)