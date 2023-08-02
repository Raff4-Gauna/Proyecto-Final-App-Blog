from django.views.generic import CreateView, TemplateView
from .models import Contact
from .forms import ContactForm
from django.urls import reverse_lazy


class ContactView(CreateView):
    model = Contact
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contacts:contact_notice')
    
class NoticeView(TemplateView):
    template_name = 'contact/contact_notice.html'
