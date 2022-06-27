from app import create_app

if __name__ == '__main__':
    create_app().run()
else:
    gunicorn = create_app()

"""
gunicorn run:

pip install gunicorn

gunicorn -b 0.0.0.0:5000 -w 3 run:gunicorn
"""