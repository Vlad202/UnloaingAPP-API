<<<<<<< HEAD
# Generated by Django 3.1.3 on 2021-01-25 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rules', '0003_auto_20210125_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercolor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
=======
# Generated by Django 3.1.3 on 2021-01-25 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rules', '0003_auto_20210125_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercolor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
>>>>>>> 28db349d9fc26775f91308aec53ddc052260599d
