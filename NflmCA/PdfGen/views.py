from django.shortcuts import render
from easy_pdf.views import PDFTemplateView
from Consumer_Analytics.models import *
from .models import *


def formpage(request):
    return render(request, "PdfGen/pdf_form.html")


class DetailsPDF(PDFTemplateView):
    template_name = "PdfGen/details_pdf.html"

    def get_context_data(self, **kwargs):
        context = super(DetailsPDF, self).get_context_data(pagesize="A4", title="Consumer Details PDF", **kwargs)
        consumer_num = self.request.GET.get("phonenum")
        context["consumer"] = User.objects.get(phone1=consumer_num)
        context['images'] = UserImage.objects.all()
        context['simages'] = Images.objects.all()
        context['links'] = SocialLink.objects.all()
        context['addresses'] = AlternateAddress.objects.all()
        print("abcdef")
        return context

    def get_pdf_filename(self):
        num = self.request.GET.get("phonenum")
        return str(num) + ".pdf"


def cus_details(request):
    if request.POST:
        pnum = request.POST['phonenum']
        context = {
            'consumer': User.objects.get(phone1=pnum),
            'images': UserImage.objects.all(),
            'links': SocialLink.objects.all(),
            'addresses': AlternateAddress.objects.all(),
            'logs': Log.objects.all(),
            'orders': Order.objects.all()
        }
        return render(request, "PdfGen/cus_details.html", context=context)
    else:
        return render(request, "PdfGen/pdf_form.html")

