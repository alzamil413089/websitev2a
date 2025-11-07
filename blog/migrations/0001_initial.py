from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=220, unique=True)),
                ('language', models.CharField(choices=[('ar', 'العربية'), ('en', 'English')], default='ar', max_length=2)),
                ('excerpt', models.TextField(blank=True)),
                ('body', models.TextField()),
                ('cover', models.ImageField(blank=True, null=True, upload_to='blog/covers/')),
                ('tags', models.CharField(blank=True, help_text='Comma-separated tags', max_length=300)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('publish_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('meta_title', models.CharField(blank=True, max_length=255)),
                ('meta_description', models.CharField(blank=True, max_length=300)),
                ('og_image', models.ImageField(blank=True, null=True, upload_to='blog/og/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={'ordering': ['-publish_at']},
        ),
    ]

