from django.db import migrations
from django.utils import timezone


def create_sample_posts(apps, schema_editor):
    BlogPost = apps.get_model('blog', 'BlogPost')
    now = timezone.now()
    BlogPost.objects.create(
        title='أهلاً بكم في فنترا لينك',
        slug='ahlan-bkm-fntr-lynk',
        language='ar',
        excerpt='مرحبا! هذه مقالة تعريفية باللغة العربية.',
        body='هذه أول تدوينة عربية لاختبار النظام.',
        tags='إعلان, تعريفي',
        status='published',
        publish_at=now,
        meta_title='فنترا لينك — المدونة',
        meta_description='أول تدوينة عربية على مدونة فنترا لينك.',
    )
    BlogPost.objects.create(
        title='Welcome to Fyntralink',
        slug='welcome-to-fyntralink',
        language='en',
        excerpt='Hello! This is an English intro post.',
        body='This is the first English post to validate the blog.',
        tags='announcement, intro',
        status='published',
        publish_at=now,
        meta_title='Fyntralink — Blog',
        meta_description='First English post on the Fyntralink blog.',
    )


def remove_sample_posts(apps, schema_editor):
    BlogPost = apps.get_model('blog', 'BlogPost')
    BlogPost.objects.filter(slug__in=['ahlan-bkm-fntr-lynk', 'welcome-to-fyntralink']).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_sample_posts, remove_sample_posts),
    ]
