from rest_framework import serializers
from .models import Teknik, Computer, Elit


class TeknikSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teknik
        fields = ["id", "masuk", "ngambil barang", "kasir"]
            class meta:
                model = teknik 
                fields = ["untuk melihat barang"]
class ComputerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = ["id", "masuk", "ngambil barang", "kasir"]
            class meta:
            model = teknik 
            fields = ["barang yang disukai"]
class ElitSerializers(serializers.ModelSerializer):
    class Meta:
        model = Elit
        fields = ["id", "masuk", "ngambil barang", "kasir"]
            class meta:
                model = elit 
                fields = ["bayar"]