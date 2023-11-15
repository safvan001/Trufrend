# Generated by Django 4.2.7 on 2023-11-13 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trufrend', '0014_remove_profile_challenges_profile_challenges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='challenges',
            field=models.CharField(choices=[('Anxiety', 'Anxiety'), ('Motivation', 'Motivation'), ('Confidence', 'Confidence'), ('Sleep', 'Sleep'), ('Depression', 'Depression'), ('Work Stress', 'Work Stress'), ('Relationships', 'Relationships'), ('Exam stress', 'Exam stress'), ('Pregnancy', 'Pregnancy'), ('Loss', 'Loss'), ('LGBTQ+', 'LGBTQ+'), ('Low Energy', 'Low Energy'), ('Self Esteem', 'Self Esteem'), ('Loneliness', 'Loneliness'), ('Trauma', 'Trauma'), ('Health issues', 'Health issues')], max_length=100),
        ),
    ]