from django.core.management.base import BaseCommand
from paginas.models import *

class Command(BaseCommand):

    def handle(self, *args, **options):
        produtos = Products.objects.all().filter(category__name='TOP')
        print(produtos)