from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


def Promote_context(category):
    promote_project_data = []
    all_promoted_projects = Promote.objects.filter(category=category).order_by('active_index')
    for promote in all_promoted_projects:
        promote_project_data.append({
            'title': promote.title,
            'description': promote.description,
            'cover': promote.cover.url,
            'link': promote.link,
        })
    return promote_project_data


def Service_promote():
    all_services = Service.objects.all().order_by('active_index')
    service_data = []
    for service in all_services:
        service_data.append(
            {
                'title': service.title,
                'description': service.description,
                'icon_class': service.icon_class,
                'link': service.link, }
        )
        return service_data


def Product_promote():
    all_products = ProductPromote.objects.all().order_by('active_index')
    product_data = []
    for product in all_products:
        product_data.append({
            'cover': product.cover.url,
            'title': product.title,
            'description': product.description,
            'link': product.link,
        })


class IndexPage(TemplateView):
    def get(self, request, **kwargs):
        all_start = Promote_context('st')
        all_promote = Promote_context('pr')
        active_start = all_start.pop(0)
        active_promo_project = all_promote.pop(0)
        all_icons = Icon.objects.all()
        icons_link = [icon.link for icon in all_icons]

        context = {
            'promote_project_data': all_promote,
            'active_promo_project': active_promo_project,
            'start_promote': all_start,
            'active_start': active_start,
            'icons_link': icons_link,
            'service_data': Service_promote(),
            'product_data': Product_promote(),
        }

        return render(request, 'Index.html', context)
