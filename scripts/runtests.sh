echo "Running tests"
. venv/bin/activate
python manage.py test
deactivate
echo "Test are OK"