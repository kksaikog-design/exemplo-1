from django.db import models
        
class Livro(models.Model):
    titulo= models.CharField(max_length=200)
    autor= models.CharField(max_length=150)
    isbn= models.CharField(max_length=13, unique=True)
    ano_publicacao= models.IntegerField(default=0)
    data_cadastro= models.DateField(auto_now_add= True)
        
    def __str__(self):
        return self.titulo
        
    
