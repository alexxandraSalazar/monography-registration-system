set -o errexit  # salir en caso de error

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate