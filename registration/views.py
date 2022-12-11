from .forms import SignUpFormWithEmail
from django.views.generic import CreateView
from django.urls import reverse_lazy


class SignUpView(CreateView):
    form_class = SignUpFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'