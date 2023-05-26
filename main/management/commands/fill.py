from django.core.management import BaseCommand

from main.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'id': '100', 'name': 'Бакалея', 'description': '..'},
            {'id': '101', 'name': 'Молочка', 'description': '..'},
            {'id': '102', 'name': 'Заморожка', 'description': '..'},
            {'id': '103', 'name': 'Хлебобулочные', 'description': ',,'},
            {'id': '104', 'name': 'Новинки', 'description': ',,'},
            {'id': '105', 'name': 'Акции', 'description': ',,'},
            {'id': '106', 'name': 'Посуда', 'description': ',,'},

        ]
        #for category_item in category_list:
            #Category.objects.create(**category_item)
        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))
        Category.objects.all().delete()
        Category.objects.bulk_create(category_for_create)
