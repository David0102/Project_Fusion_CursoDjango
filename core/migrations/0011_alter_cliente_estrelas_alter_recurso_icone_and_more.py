# Generated by Django 4.2.1 on 2023-05-30 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_cliente_estrelas_alter_recurso_icone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='estrelas',
            field=models.CharField(choices=[('1', '1 estrela'), ('4', '4 estrelas'), ('3', '3 estrelas'), ('2', '2 estrelas'), ('5', '5 estrelas')], max_length=12, verbose_name='Estrelas'),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='icone',
            field=models.CharField(choices=[('lni-layers', 'Camadas'), ('lni-leaf', 'Folha'), ('lni-rocket', 'Foguete'), ('lni-pencil-alt', 'Formulario'), ('lni-laptop-phone', 'Computador'), ('lni-cog', 'Engrenagem')], max_length=20, verbose_name='Icone'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-layers', 'Design'), ('lni-stats-up', 'Gráfico'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete'), ('lni-users', 'Usuários'), ('lni-cog', 'Engrenagem')], max_length=13, verbose_name='Icone'),
        ),
    ]
