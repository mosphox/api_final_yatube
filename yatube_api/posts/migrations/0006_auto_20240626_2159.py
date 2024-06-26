# Generated by Django 3.2.16 on 2024-06-26 18:59

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20240626_2149'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique subscription',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_subscription'),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(('user', django.db.models.expressions.F('following')), _negated=True), name='no_self_following'),
        ),
    ]
