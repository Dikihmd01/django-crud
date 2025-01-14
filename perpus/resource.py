from import_export import resources
from perpus.models import Buku
from import_export.fields import Field

class BukuResource(resources.ModelResource):
    kelompok_id__nama = Field(attribute='kelompok_id', column_name='kelompok')

    class Meta:
        model = Buku
        fields = ['judul', 'tanggal', 'kelompok_id__nama', 'penulis', 'penerbit', 'jumlah']
        export_order = ['judul', 'tanggal', 'penulis', 'penerbit', 'jumlah', 'kelompok_id__nama']