# Generated by Django 3.1.4 on 2021-03-16 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms_class', '0009_auto_20210316_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lmsclassinfo',
            name='act_num',
        ),
        migrations.RemoveField(
            model_name='lmsclassinfo',
            name='ass_num',
        ),
        migrations.RemoveField(
            model_name='lmsclassinfo',
            name='exam_num',
        ),
        migrations.RemoveField(
            model_name='lmsclassinfo',
            name='quiz_num',
        ),
        migrations.DeleteModel(
            name='TermCounts',
        ),
    ]