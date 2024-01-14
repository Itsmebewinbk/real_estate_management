# Generated by Django 4.2 on 2024-01-14 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.URLField(blank=True, null=True)),
                ('features', models.TextField()),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('zipcode', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=250)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('phone_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.country')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.state')),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.URLField(blank=True, null=True)),
                ('document_proofs', models.URLField()),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=250)),
                ('phone_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.country')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.state')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.CharField(choices=[('1BHK', '1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK'), ('4BHK', '4BHK')], max_length=4)),
                ('image', models.URLField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_occupied', models.BooleanField(default=False)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to='core.property')),
                ('tenant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('deposit_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rentals', to='core.property')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rentals', to='core.tenant')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rentals', to='core.unit')),
            ],
        ),
    ]