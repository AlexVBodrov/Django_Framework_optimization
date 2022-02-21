from django.db.models import F


@receiver(pre_save, sender=OrderItem)
@receiver(pre_save, sender=Basket)
def product_quantity_update_save(instance, sender, **kwargs):
    if instance.pk:
        instance.product.quantity = F("quantity") - (instance.quantity - sender.get_item(instance.pk).quantity)
    else:
        instance.product.quantity = F("quantity") - instance.quantity
    instance.product.save()


@receiver(pre_delete, sender=OrderItem)
@receiver(pre_delete, sender=Basket)
def product_quantity_update_delete(instance, **kwargs):
    instance.product.quantity = F("quantity") + instance.quantity
    instance.product.save()