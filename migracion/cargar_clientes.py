import csv
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'credicentro.settings'
import django
django.setup()
from cliente.models import Cliente

# Cliente.objects.all().delete()

with open('personas.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for i, row in enumerate(reader):
        try:
            Cliente.objects.create(
                nombre=row['nombre'],
                apellido=row['apellido'],
                documento=row['documento']

            )
        except:
            print ('Error:',row)