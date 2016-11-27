from django.shortcuts import render,get_object_or_404,redirect
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import profile,Data,images,Massage

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'webpage/login.html')
    else:
        db = profile.objects.filter(user1 = request.user)
        return render(request, 'webpage/index.html' , {'db':db})

def Profile(request, names):
    if not request.user.is_authenticated():
        return render(request, 'webpage/login.html')
    else:
        db = get_object_or_404(profile,nick_name__iexact = str(names),user1 = request.user)
        return render(request, 'webpage/profile.html' , {'db':db})

def Details(request):
    if not request.user.is_authenticated():
        return render(request, 'webpage/login.html')
    else:
        db = profile.objects.filter(user1 = request.user)
        return render(request, 'webpage/user_profile.html' ,{ 'db':db} )

class AddUser(CreateView):
        model= profile
        fields = ['user1','name','nick_name']

class UpdateUser(UpdateView):
        model= profile
        fields = ['user1','name','nick_name']

class DeleteUser(DeleteView):
        model= profile
        success_url = reverse_lazy('webpage:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'webpage/reg.html'

    def get(self,request):
        form = self.form_class(None)
        return render (request,self.template_name , {'form' :form })

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # normalised data_set
            username = form.cleaned_data ['username']
            password = form.cleaned_data ['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username,password=password)
            if user is not None:

                if user.is_active:
                    login(request,user)
                    return redirect ('webpage:index')
        return render(request, self.template_name , {'form': form})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                db = profile.objects.filter(user1=request.user)
                return render(request, 'webpage/index.html', {'db' : db})
            else:
                return render(request, 'webpage/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'webpage/login.html', {'error_message': 'Invalid login'})
    return render(request, 'webpage/login.html')

def logout_user(request):
    if not request.user.is_authenticated():
        return render(request, 'webpage/login.html')
    else:
        logout(request)
        form = UserForm(request.POST or None)
        context = {
            "form": form,
        }
        return render(request, 'webpage/login.html', context)

class AddImage(CreateView):
        model= images
        fields = ['user3','images_details','images']
        success_url = reverse_lazy('webpage:index')

def Images(request, names):
    if not request.user.is_authenticated():
        return render(request, 'webpage/login.html')
    else:
        db = get_object_or_404(profile,nick_name__iexact = str(names))
        return render(request, 'webpage/Images.html' , {'db':db})

class AddData(CreateView):
        model= Data
        fields = ['user2','about','email', 'mobile']
        success_url = reverse_lazy('webpage:index')

def Data(request, names):
    if not request.user.is_authenticated():
        return render(request, 'webpage/login.html')
    else:
        db = get_object_or_404(profile,nick_name__iexact = str(names))
        return render(request, 'webpage/About.html' , {'db':db})

class AddMassage(CreateView):
        model= Massage
        fields = ['user4','sub','massage']
        success_url = reverse_lazy('webpage:index')

def Massages(request):
    if not request.user.is_authenticated():
        return render(request, 'webpage/login.html')
    else:
        return render(request, 'webpage/Massages.html' )
