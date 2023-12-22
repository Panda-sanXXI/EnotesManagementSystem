
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ContactNo', models.CharField(max_length=10, null=True)),
                ('About', models.CharField(max_length=450, null=True)),
                ('Role', models.CharField(max_length=150, null=True)),
                ('RegDate', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200, null=True)),
                ('Content', models.CharField(max_length=450, null=True)),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
                ('UpdationDate', models.DateField(null=True)),
                ('signup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enotes.signup')),
            ],
        ),
    ]
