version: '3.8'

service:
    django:
        container_name: django
        build: 
            context: ./djangoCelery
        command: python manage.py runserver 0.0.0.0:8000
        
