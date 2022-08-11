# Generated by Django 3.1.4 on 2021-03-16 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms_class', '0007_auto_20210316_0906'),
        ('lms_lesson', '0007_auto_20210315_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('type_of_lecture', models.CharField(choices=[('LC', 'Lecture'), ('AN', 'Announcement')], default='AN', max_length=2)),
                ('lesson_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lecture', to='lms_class.lmsclass')),
            ],
        ),
    ]
