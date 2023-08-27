from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Profil(models.Model):
 nama = models.CharField(max_length=250, null=True, blank=True)
 tentang_diri = RichTextField(config_name='awesome_ckeditor', null=True, blank=True)
 foto = models.ImageField(max_length=250, null=True, blank=True)
 hp = models.CharField(max_length=250, null=True, blank=True)
 fb = models.CharField(max_length=250, null=True, blank=True)
 ig = models.CharField(max_length=250, null=True, blank=True)
 github = models.CharField(max_length=250, null=True, blank=True)

 def __str__(self):
     return self.nama
 
 class Meta:
  verbose_name_plural = "Profil Diri"
  

class Portfolio(models.Model):
 KATEGORI =(
      ('web_dev', 'WEB Development'),
      ('creative_design', 'Creative Design'),
      ('graphic_design', 'Graphic Design'),
 )


 judul = models.CharField(max_length=250, null=True, blank=True)
 isi_aplikasi = RichTextField(config_name='awesome_ckeditor', null=True, blank=True)
 foto_aplikasi = models.ImageField(max_length=250, null=True, blank=True)
 kategori = models.CharField(max_length=250, null=True, blank=True, choices=KATEGORI)
 kategori_dua = models.CharField(max_length=250, null=True, blank=True, choices=KATEGORI)
 penulis = models.CharField(max_length=250, null=True, blank=True)
 link_projek = models.CharField(max_length=250, null=True, blank=True)
 tanggal = models.DateField(auto_now_add=False, null=True)

 def __str__(self):
     return self.judul
 
 class Meta:
  verbose_name_plural = "Galeri Aplikasi"