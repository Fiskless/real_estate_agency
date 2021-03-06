# Generated by Django 2.2.4 on 2020-12-01 12:12

from django.db import migrations


def load_owner_flats(apps, schema_editor):

    Owner = apps.get_model('property', 'Owner')
    Flat = apps.get_model('property', 'Flat')
    owners = Owner.objects.all()

    for owner in owners:
        flats = Flat.objects.filter(owner_pure_phone=owner.owner_pure_phone)
        owner.owner_flats.set(flats)


def move_backward(apps, schema_editor):

    Owner = apps.get_model('property', 'Owner')
    owners = Owner.objects.all()
    for owner in owners:
        owner.owner_flats.clear()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20201201_1348'),
    ]

    operations = [
        migrations.RunPython(load_owner_flats, move_backward)
    ]
