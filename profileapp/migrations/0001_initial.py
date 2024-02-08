# Generated by Django 4.2.1 on 2024-02-08 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profileapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='productNotifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senderName', models.TextField()),
                ('senderId', models.IntegerField()),
                ('receiver', models.TextField()),
                ('seen', models.CharField(choices=[('seen', 'seen'), ('unseen', 'unseen')], max_length=100)),
                ('text', models.CharField(max_length=100)),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pics', models.ImageField(blank=True, default='/profile/default.png', null=True, upload_to=profileapp.models.upload_to)),
                ('location', models.CharField(blank=True, max_length=70, null=True)),
                ('ratings_value', models.IntegerField(blank=True, null=True)),
                ('voucher', models.CharField(blank=True, max_length=100, null=True)),
                ('tags', models.TextField(choices=[('no-seller', 'no-seller'), ('seller', 'seller')], default='no-seller')),
                ('blocked', models.TextField(choices=[('true', 'true'), ('false', 'false')], default='false')),
                ('banckAccount', models.IntegerField(blank=True, null=True)),
                ('accountNumber', models.IntegerField(blank=True, null=True)),
                ('subaccount_percentage', models.IntegerField(blank=True, null=True)),
                ('subaccountId', models.CharField(blank=True, max_length=30, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=30, null=True)),
                ('state', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('businessName', models.CharField(blank=True, max_length=30, null=True)),
                ('item', models.TextField(blank=True, null=True)),
                ('name', models.SlugField(blank=True, unique=True)),
                ('followers', models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('following', models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('notification', models.ManyToManyField(blank=True, related_name='productnotification', to='profileapp.productnotifications')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('text', models.TextField(blank=True, null=True)),
                ('sender_name', models.CharField(blank=True, max_length=50, null=True)),
                ('pics', models.ImageField(blank=True, null=True, upload_to='')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_review', to='profileapp.profile')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_review', to='profileapp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('accept', 'accept'), ('delete', 'delete')], max_length=10)),
                ('followers', models.IntegerField()),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receivers', to='profileapp.profile')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='senders', to='profileapp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senderName', models.TextField()),
                ('text', models.CharField(max_length=100)),
                ('time', models.TimeField()),
                ('seen', models.CharField(choices=[('seen', 'seen'), ('unseen', 'unseen')], max_length=100)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_receivers', to='profileapp.profile')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_senders', to='profileapp.profile')),
            ],
        ),
    ]
