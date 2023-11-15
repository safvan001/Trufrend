# Generated by Django 4.2.7 on 2023-11-07 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trufrend', '0006_video_parent_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoPack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='video',
            name='parent_video',
        ),
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trufrend.videopack'),
        ),
    ]