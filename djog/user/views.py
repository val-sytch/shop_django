import logging

from django.views import generic
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django import http
from django.core.urlresolvers import reverse
from django.template.loader import get_template
from django.template import Context

from djog.user import forms
from oscar.apps.customer.forms import generate_username

logger = logging.getLogger('user')


class UserView(generic.FormView):
    template_name = 'user/form.html'
    form_class = forms.UserForm

    def form_valid(self, form):
        real_email = form.cleaned_data['email']
        username = generate_username()
        password = generate_username()
        email = 'dashboard-user-%s@oscarcommerce.com' % username

        user = self.create_dashboard_user(username, email, password)
        self.send_confirmation_email(real_email, user, password)
        logger.info("Created dashboard user #%d for %s",
                    user.id, real_email)

        messages.success(
            self.request,
            "The credentials for a dashboard user have been sent to %s" % real_email)
        return http.HttpResponseRedirect(reverse('user'))

    def create_dashboard_user(self, username, email, password):
        user = User.objects.create_user(username, email, password)
        user.is_staff = True
        user.save()
        return user

    def send_confirmation_email(self, real_email, user, password):
        msg = get_template('user/email.txt').render(Context({
            'email': user.email,
            'password': password
        }))
        send_mail('Dashboard access ',
                  msg, 'blackhole@latest.oscarcommerce.com',
                  [real_email])

