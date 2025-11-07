Fyntralink — Django 5 bilingual website

Stack: Django 5, django-environ, Pillow, django-htmx, markdown2

Setup
- Python 3.11+
- Optional: create venv and activate
- Install deps: pip install "Django>=5,<6" django-environ Pillow markdown2 django-htmx

Dev Commands
- python manage.py makemigrations && python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver 0.0.0.0:8000

Internationalization
- django-admin makemessages -l ar
- django-admin makemessages -l en
- django-admin compilemessages

Environment (.env)
- DEBUG=1
- SECRET_KEY=change-me
- ALLOWED_HOSTS=127.0.0.1,localhost

URLs and Features
- Bilingual via i18n_patterns: /ar/ and /en/
- Non-i18n endpoints:
  - /sitemap.xml
  - /rss.xml
  - /robots.txt
  - /health/
- Blog: posts, tags, RSS feed
- Leads: contact form + newsletter subscribe

