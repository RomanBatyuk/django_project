from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product

class Command(BaseCommand):
    help = 'Создаёт группу "Модератор продуктов" и назначает ей права cancellation_of_product и delete_product'

    def handle(self, *args, **options):
        # Получаем ContentType для модели Product
        content_type = ContentType.objects.get_for_model(Product)

        # Получаем права
        try:
            cancel_perm = Permission.objects.get(codename='cancellation_of_product', content_type=content_type)
            delete_perm = Permission.objects.get(codename='delete_product', content_type=content_type)
        except Permission.DoesNotExist as e:
            self.stdout.write(self.style.ERROR(f'Право не найдено: {e}. Убедитесь, что оно добавлено в Meta модели Product.'))
            return

        # Создаём группу (или получаем существующую)
        group, created = Group.objects.get_or_create(name='Модератор продуктов')
        if created:
            self.stdout.write(f'Группа "{group.name}" создана.')
        else:
            self.stdout.write(f'Группа "{group.name}" уже существует.')

        # Назначаем права группе
        group.permissions.set([cancel_perm, delete_perm])
        self.stdout.write(self.style.SUCCESS(f'Права назначены группе "{group.name}": {cancel_perm.name}, {delete_perm.name}'))