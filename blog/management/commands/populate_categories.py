from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This command inserts category data"

    def handle(self, *args: Any, **options: Any):

        # delete Existing the data from table
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Completed Delete Data!"))

        categories = [
            "Sports",
            "Technology",
            "Science",
            "Art",
            "Food",
        ]

        for category in categories:
            Category.objects.create(name=category)

        self.stdout.write(self.style.SUCCESS("Completed inserting catgory Data!"))