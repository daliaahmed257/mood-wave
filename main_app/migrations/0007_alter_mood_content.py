

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_mood_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mood',
            name='content',
            field=models.TextField(default='', verbose_name='Could to explain further?'),
        ),
    ]
