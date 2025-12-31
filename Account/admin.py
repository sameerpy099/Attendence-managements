from django.contrib import admin
from Student.models import student_basic_detail

@admin.register(student_basic_detail)
class student_basic_detailAdmin(admin.ModelAdmin):
  list_display=['first_name','last_name','state','email','high_passout','inter_passout','high_percentage','inter_percentage','Course','Branch','Dob']
  def get_high_passout(self, obj):
        return obj.high_passout or 0
  get_high_passout.short_description = 'High Passout'

  def get_inter_passout(self, obj):
        return obj.inter_passout or 0
  get_inter_passout.short_description = 'Inter Passout'

  def get_high_percentage(self, obj):
        return obj.high_percentage or 0
  get_high_percentage.short_description = 'High %'

  def get_inter_percentage(self, obj):
        return obj.inter_percentage or 0
  get_inter_percentage.short_description = 'Inter %'
  
  search_fields=('Course','email','Branch')
  list_filter=['Branch','Course']
# Register your models here.