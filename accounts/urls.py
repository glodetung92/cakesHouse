from django.urls import path
from .views import ProfileEditView

app_name = 'accounts'

urlpatterns = [
	path('edit_profile/', ProfileEditView.as_view(), name='edit_profile'),
]
