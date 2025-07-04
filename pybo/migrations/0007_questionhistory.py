# Generated by Django 4.2.23 on 2025-06-15 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0006_auto_20200507_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='histories', to='pybo.question')),
            ],
        ),
    ]
