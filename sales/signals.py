from .models import Sale
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

# many to many changed signals
# en el momento en que se modifica algun campo de un many to many, se puede ejecutar una senal

#? https://docs.djangoproject.com/en/3.2/ref/signals/#m2m-changed
# el sender es la clase intermedia usada en el many to many 
# para acceder a esta se debe usar el atributo through en el campo Many To Many
@receiver(m2m_changed, sender=Sale.positions.through)
def calculate_price(sender, instance, action, **kwargs):
    print(action)
    total_price = 0
    if action == 'post_add' or action == 'post_remove':
        for item in instance.get_positions():
            total_price += item.price

    instance.total_price = total_price
    instance.save()

# se desea sumar el precio de todas las posiciones

