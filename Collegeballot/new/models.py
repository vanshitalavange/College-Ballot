from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=45,null=True,blank=True)
    year = models.CharField(max_length=45,null=True,blank=True)
    dept = models.CharField(max_length=45,null=True,blank=True)
    div = models.CharField(max_length=45,null=True,blank=True)
    rollno = models.CharField(max_length=45,null=True,blank=True)
    login_id = models.CharField(max_length=45,null=True,blank=True)
    password = models.CharField(max_length=45,null=True,blank=True)
    solution = models.CharField(max_length=50,null=True,blank=True)
    crformfilled = models.CharField(max_length=45,null=True,blank=True)
    ans1 = models.CharField(max_length=100,null=True,blank=True)
    ans2 = models.CharField(max_length=100,null=True,blank=True)
    hod = models.CharField(max_length=45,null=True,blank=True)
    user_vc = models.IntegerField(default=0,null=True,blank=True)
    vc_pcr = models.IntegerField(default=0,null=True,blank=True)
    elected_cr = models.CharField(max_length=45,null=True,blank=True)
    elected_dept_head = models.CharField(max_length=45,null=True,blank=True)
    ans = models.CharField(max_length=100,null=True,blank=True)
    dept_vc=models.IntegerField(default=0,null=True,blank=True)
    s_dept_vc = models.IntegerField(default=0, null=True, blank=True)
    all_cr_vc = models.IntegerField(default=0, null=True, blank=True)
    cr_vc = models.IntegerField(default=0,null=True,blank=True)
    president = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name

class Hod(models.Model):
    hod_login_id = models.CharField(max_length=45, null=True, blank=True)
    hod_password = models.CharField(max_length=45, null=True, blank=True)
    dept = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return self.dept