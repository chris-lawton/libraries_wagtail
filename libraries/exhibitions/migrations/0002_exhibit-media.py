# Generated by Django 2.0.2 on 2018-08-13 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0007_merge'),
        ('exhibitions', '0001_exhibits-initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibitartwork',
            name='media',
            field=models.ForeignKey(blank=True, help_text='Video or audio to embed. Only needed for video/audio types.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document'),
        ),
        migrations.AlterField(
            model_name='exhibitartwork',
            name='embed_code',
            field=models.TextField(blank=True, help_text='Can be used for YouTube/Vimeo videos. ONLY PASTE THE EMBED URL e.g. https://youtube.com/embed/KbjGqRdPF7s and not the full <iframe> wrapped HTML.'),
        ),
    ]
