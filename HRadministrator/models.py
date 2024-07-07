from django.db import models
from django.forms import ValidationError

# Create your models here.

class organization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class department(models.Model):
    name = models.CharField(max_length=100)
    orgname = models.ForeignKey("organization", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class position(models.Model):
    name = models.CharField(max_length=100)
    deptname = models.ForeignKey("department", on_delete=models.PROTECT)
    orgname = models.ForeignKey("organization", on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
class requisition(models.Model):
    requisition_id = models.CharField(max_length=100, unique=True)
    positionname = models.ForeignKey("position", on_delete=models.PROTECT)
    no_of_openings = models.IntegerField(default=0)
    min_salary = models.IntegerField(null=True)
    max_salary = models.IntegerField(null=True)
    min_experiance = models.IntegerField(null=True)
    max_experiance = models.IntegerField(null=True)
    qualification = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.requisition_id

class candidate(models.Model):
    cand_id = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=False)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.cand_id
    
class requisition_candidates(models.Model):
    requisition = models.ForeignKey("requisition", on_delete=models.PROTECT)
    candidate = models.ForeignKey("candidate", on_delete=models.PROTECT)

    def clean(self, *args, **kwargs):
        if (requisition_candidates.objects.filter(requisition=self.requisition_id).exists()and
            requisition_candidates.objects.filter(candidate=self.cand_id).exists()):
            raise ValidationError('Class Details already exists')
        