# Generated by Django 4.2.7 on 2024-01-01 18:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AdminSide', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenges', models.CharField(choices=[('Anxiety', 'Anxiety'), ('Motivation', 'Motivation'), ('Confidence', 'Confidence'), ('Sleep', 'Sleep'), ('Depression', 'Depression'), ('Work Stress', 'Work Stress'), ('Relationships', 'Relationships'), ('Exam stress', 'Exam stress'), ('Pregnancy', 'Pregnancy'), ('Loss', 'Loss'), ('LGBTQ+', 'LGBTQ+'), ('Low Energy', 'Low Energy'), ('Self Esteem', 'Self Esteem'), ('Loneliness', 'Loneliness'), ('Trauma', 'Trauma'), ('Health issues', 'Health issues')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=15)),
                ('firstname', models.CharField(max_length=100)),
                ('Lastname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=254)),
                ('subject', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(default='', max_length=15)),
                ('dp', models.ImageField(blank=True, default='img/profile_pictures/userimage.png', null=True, upload_to='img/profile_pictures')),
                ('name', models.CharField(max_length=100)),
                ('nick_name', models.CharField(max_length=50)),
                ('Gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('others', 'others')], default='Male', max_length=100, null=True)),
                ('is_online', models.BooleanField(default=False)),
                ('challenges', models.ManyToManyField(to='Trufrend.challenge')),
                ('doctorFavour', models.ManyToManyField(related_name='doctor_fav_profiles', to='AdminSide.doctordata')),
                ('language', models.ManyToManyField(to='Trufrend.languages')),
            ],
        ),
        migrations.CreateModel(
            name='Usercount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VideoPack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_file', models.FileField(default=1, upload_to='videos/')),
                ('subtitle', models.CharField(default=' ', max_length=200)),
                ('description', models.TextField(default='')),
                ('videolen', models.CharField(default='10', max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/videobanner')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('posterimage', models.ImageField(blank=True, null=True, upload_to='img/Posterimage')),
                ('video_files', models.ManyToManyField(to='Trufrend.videopack')),
            ],
        ),
        migrations.CreateModel(
            name='Recent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminSide.doctordata')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trufrend.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_value', models.IntegerField()),
                ('doctor', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='AdminSide.doctordata')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trufrend.profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='videoFavour',
            field=models.ManyToManyField(to='Trufrend.video'),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trufrend.profile')),
            ],
        ),
    ]
