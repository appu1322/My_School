from django.contrib import admin

# Register your models here.
from tut11.models import Physic,PhysicComment,Chemistry,ChemistryComment,Math,MathComment

admin.site.register((Physic, PhysicComment, Chemistry, ChemistryComment, Math, MathComment))