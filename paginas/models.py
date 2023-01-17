from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100,null=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to="catogeries",blank=False)
    slug = models.SlugField('Slug',max_length=100,blank=True,editable=False)
    
    @property
    def view_image(self):
        return mark_safe('<img src="%s" width="100%" />'%self.imagem.url)   
        view_image.short_description = "Imagem Cadastrada" 
        view_image.allow_tags = True 

    class Meta:
        ordering = ('-id'),
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


    def __str__(self):
        return f'{self.name}'



def products_pre_save(signal,instance,sender,**kwars):
    instance.slug = slugify(instance.name)

signals.pre_save.connect(products_pre_save,sender=Categories)




class Products(models.Model):
    STATUS = (
        ('inativo','INATIVO'),
        ('ativo','ATIVO'),
    )
    name = models.CharField(max_length=100,null=False)
    description = models.TextField(max_length=500,null=False)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE,verbose_name='Categorias')
    slug = models.SlugField('Slug',max_length=100,blank=True,editable=False)
    create = models.DateTimeField(default=timezone.now)
    imagemprimeira = models.ImageField(upload_to="paginas",blank=False,default=False)
    imagemsegunda = models.ImageField(upload_to="paginas1",blank=False,default=False)
    imagemterceira = models.ImageField(upload_to="paginas2",blank=False,default=False)
    imagemquarta = models.ImageField(upload_to="paginas3",blank=False,default=False)
    status = models.TextField(choices=STATUS,max_length=10,default='INATIVO')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destaque = models.BooleanField(default=False,verbose_name='Destaque?')

    #def get_absolute_url(self):
    #    return reverse('post_detail',args=[self.slug])

    #def get_absolute_url_update(self):
    #    return reverse('post_edit',args=[self.pk])

    
    def get_absolute_url(self):
        return reverse('produtos-detail',args=[self.category,self.slug])

    @property
    def view_image(self):
        return mark_safe('<img src="%s" width="100%" />'%self.imagemprimeira.url)   
        view_image.short_description = "Imagem Cadastrada" 
        view_image.allow_tags = True 


    def view_image(self):
        return mark_safe('<img src="%s" width="100%" />'%self.imagemsegunda.url)   
        view_image.short_description = "Imagem Cadastrada" 
        view_image.allow_tags = True 


    def view_image(self):
        return mark_safe('<img src="%s" width="100%" />'%self.imagemterceira.url)   
        view_image.short_description = "Imagem Cadastrada" 
        view_image.allow_tags = True 

    def view_image(self):
        return mark_safe('<img src="%s" width="100%" />'%self.imagemquarta.url)
        view_image.short_description = "Imagem Cadastrada" 
        view_image.allow_tags = True 

    class Meta:
        ordering = ('-create'),
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return f'{self.name} - {self.category} - {self.create} - {self.status} - {self.user}'
    
    def delete(self, *args, **kwargs):
        self.imagemprimeira.delete()
        super().delete(*args, **kwargs)

def products_pre_save(signal,instance,sender,**kwars):
    instance.slug = slugify(instance.name)

signals.pre_save.connect(products_pre_save,sender=Products)

class Materials(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)
    imagem = models.FileField(upload_to='catalogos/pdf')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='catalogos/capa', null=True, blank=True)
    
    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('-id',)
        verbose_name = "Material"
        verbose_name_plural = "Materiais"

        
    @property
    def view_image(self):
        return mark_safe('<img src="%s" width="100%" />'%self.arquivo.url)   
        view_image.short_description = "Imagem Cadastrada" 
        view_image.allow_tags = True 

    def delete(self, *args, **kwargs):
        self.cover.delete()
        super().delete(*args, **kwargs)

