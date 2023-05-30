from django.core.management import BaseCommand
from main.models import Blogs


class Command(BaseCommand):
    def handle(self, *args, **options) -> None:
        blogs_list = [
            {
                "name": "online_trade",
                "description": "Вы можете получить онлайн-заказ в любом магазине Лента. Просто выберите ближайший на карте и оформите самовывоз.",
                "slug": "online_trade",
                "image": "images/online_trade.jpg"
            },
            {
                "name": "product_back",
                "description": "В «Ленте» мы ценим ваше время и хотим, чтобы каждая покупка здесь была комфортной и в удовольствие. Если случилось так, что без возврата не обойтись – теперь оформить его можно ещё быстрее, проще и удобнее!",
                "slug": "product_back",
                "image": "images/product_back.png",
            },
            ]

        old_blog = []
        blog_for_create = []

        get_blogs = Blogs.objects.all().values('name')    #старые статьи
        for data in get_blogs:
            old_blog.append(data["name"])

        for item in blogs_list:    #добавляем новые
            if item["name"] not in old_blog:
                blog_for_create.append(
                    Blogs(**item)
                    )
        Blogs.objects.bulk_create(blog_for_create)