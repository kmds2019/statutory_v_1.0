from django.db import models

# Create your models here.

class statutory_details(models.Model):
    statutory_id = models.AutoField(primary_key=True)
    country = models.ForeignKey('countries', on_delete=models.CASCADE)
    domain = models.ForeignKey('domain', on_delete=models.CASCADE)
    act_name = models.CharField(max_length=200)
    rule_name = models.CharField(max_length=200)
    is_active = models.IntegerField()
    is_custom = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    updated_by = models.IntegerField()
    updated_on = models.DateTimeField()
    def __str__(self):
        return str(self.statutory_id) + str(self.country) + str(self.domain) + self.act_name + self.rule_name

class countries(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=100)
    is_active = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    updated_by = models.IntegerField()
    updated_on = models.DateTimeField()
    def __str__(self):
        return self.country_name

class domain(models.Model):
    domain_id = models.AutoField(primary_key=True)
    domain_name = models.CharField(max_length=100)
    country = models.ForeignKey('countries', on_delete=models.CASCADE)
    is_active = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    updated_by = models.IntegerField()
    updated_on = models.DateTimeField()
    def __str__(self):
        return self.domain_name
