Add some changes on vps:
-----------------------------
python3 manage.py makemigrations --settings=freee_dj.settings.prod

python3 manage.py migrate --settings=freee_dj.settings.prod

sudo systemctl restart gunicorn

sudo systemctl restart nginx
