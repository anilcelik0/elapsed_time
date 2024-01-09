from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_modified_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class Units(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name


class MainDepartment(models.Model):
    name = models.CharField(max_length=250)
    unit = models.ForeignKey(Units, on_delete=models.CASCADE, related_name="unit")

    def __str__(self) -> str:
        return self.name


class SubDepartment(models.Model):
    name = models.CharField(max_length=250)
    main_department = models.ForeignKey(MainDepartment, on_delete=models.CASCADE, related_name="main_department")

    def __str__(self) -> str:
        return self.name


class MainTopic(models.Model):
    name = models.CharField(max_length=250)
    sub_department = models.ForeignKey(SubDepartment, on_delete=models.CASCADE, related_name="sub_department")

    def __str__(self) -> str:
        return self.name


class SubTopic(models.Model):
    name = models.CharField(max_length=250)
    main_topic = models.ForeignKey(MainTopic, on_delete=models.CASCADE, related_name="main_topic")

    def __str__(self) -> str:
        return self.name
