from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from .forms import ProfileEditForm


class ProfileEditView(LoginRequiredMixin, UpdateView):
	template_name = 'account/edit_profiles.html'
	model = CustomUser
	form_class = ProfileEditForm
	success_url = '/account/edit_profile/'
	def get_object(self):
		return self.request.user
