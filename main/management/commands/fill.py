from django.core.management import BaseCommand

from main.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'name': 'Бакалея', 'description': '..'},
            {'name': 'Молочка', 'description': '..'},
            {'name': 'Заморожка', 'description': '..'},
            {'name': 'Хлебобулочные', 'description': ',,'},
            {'name': 'Новинки', 'description': ',,'},
            {'name': 'Акции', 'description': ',,'},
            {'name': 'Посуда', 'description': ',,'},

        ]
        #for category_item in category_list:
            #Category.objects.create(**category_item)
        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))
        Category.objects.all().delete()
        Category.objects.bulk_create(category_for_create)
