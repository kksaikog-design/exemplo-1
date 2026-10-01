from django.db import models
        
class Emprestimo(models.Model):
    livro= models.CharField(max_length=200)
    usuario= models.CharField(max_length=150)
    dia_emprestimo= models.IntegerField()
    dia_devolucao= models.DateField(auto_now_add= True)
        
    def __str__(self):
        return self.livro
        
    
