from django.views.generic import View
from .forms import LoginForm
class LoginView(View):
    template_name = 'login.html'
    form_class=LoginForm
    def get(self , request,*args,**kwargs):
        form=self.form_class()
        return render(request,template_name,{'form':form})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResonseRedirect(reverse('list-view'))
        else:
            return render(request, self.template_name, {'form': form})