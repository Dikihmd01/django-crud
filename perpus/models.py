from django.db import models

class Kelompok(models.Model):
    nama = models.CharField(max_length=10)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama
    

class Buku(models.Model):
    judul = models.CharField(max_length=50)
    penulis = models.CharField(max_length=20)
    penerbit = models.CharField(max_length=20)
    jumlah = models.IntegerField(null=True)
    kelompok_id = models.ForeignKey(Kelompok, on_delete=models.CASCADE, null=True)
    cover = models.ImageField(upload_to='cover/', null=True)
    tanggal = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.judul
    
