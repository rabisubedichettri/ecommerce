from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField(help_text="Duration of the service (e.g., 1 hour)")

    def __str__(self):
        return self.name


class ServiceLog(models.Model):
    service = models.ForeignKey(Service, related_name='log', on_delete=models.CASCADE)
    logger = models.ForeignKey(User, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    mac = models.CharField(max_length=17)
    browser_agent = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log for {self.name} by {self.logger.username}"

class ServiceTaken(models.Model):
    customer_name=models.CharField(max_length=255)
    customer_number=models.CharField(max_length=15,blank=True,null=True)
    customer_email=models.EmailField(max_length=50,blank=True,null=True)
    service_name=models.CharField(max_length=255)
    note=models.TextField(max_length=1000)
    image = models.ImageField(upload_to='service_images/',blank=True,null=True)
    taken_by=models.ForeignKey(User, on_delete=models.CASCADE)
    taken_at=models.DateTimeField()
    deadline=models.DateTimeField()
    finished=models.BooleanField(default=False)
