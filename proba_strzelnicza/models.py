from django.db import models


class Weapon(models.Model):
    name = models.CharField(verbose_name="nazwa", max_length=1024, unique=True, db_column="nazwa")

    class Meta:
        db_table = "Bron"
        verbose_name = "Bron"
        verbose_name_plural = "Bronie"

    def __str__(self):
        return self.name


class Bullet(models.Model):
    name = models.CharField(verbose_name="nazwa", max_length=1024, unique=True, db_column="nazwa")

    class Meta:
        db_table = "Pocisk"
        verbose_name = "Pocisk"
        verbose_name_plural = "Pociski"

    def __str__(self):
        return self.name


class Factor(models.Model):
    name = models.CharField(verbose_name="czynnik", max_length=64, db_column="czynnik")
    parameter = models.CharField(verbose_name="parametr", max_length=64, db_column="parametr")
    temperature = models.SmallIntegerField(verbose_name="temperatura", db_column="temperatura")
    filling = models.FloatField(verbose_name="wypełnienie", db_column="wypelnienie")

    class Meta:
        db_table = "Czynniki"
        verbose_name = "Czynnik"
        verbose_name_plural = "Czynniki"

    def __str__(self):
        return self.name


class Material(models.Model):
    material_type = models.CharField(verbose_name="materiał", max_length=1024, blank=True, db_column="material")
    factor = models.ForeignKey(Factor, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Materiał"
        verbose_name_plural = "Materiały"

    def __str__(self):
        return self.material_type


class Base(models.Model):
    base = models.CharField(verbose_name="podłoże", max_length=512, unique=True, db_column="podloze")

    class Meta:
        db_table = "podloze"
        verbose_name = "Podłoże"
        verbose_name_plural = "Podłoża"

    def __str__(self):
        return self.base


class Ricochet(models.Model):
    material = models.ForeignKey(Material, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "rykoszet"
        verbose_name = "Rykoszet"
        verbose_name_plural = "Rykoszety"

    def __str__(self):
        return self.material.material_type


class Shot(models.Model):
    sample_id = models.CharField(verbose_name="id próby", max_length=64, primary_key=True, db_column="id_proby")
    weapon = models.ForeignKey(Weapon, on_delete=models.DO_NOTHING, db_column="id_broni")
    bullet = models.ForeignKey(Bullet, on_delete=models.DO_NOTHING, db_column="id_pocisku")
    temperature = models.FloatField(blank=True, null=True, db_column="temperatura")
    atmosferic_conditions = models.TextField(verbose_name="warunki_atmosferyczne", db_column="warunki_atmosferyczne")
    wind_speed = models.IntegerField(verbose_name="predkosc_wiatru", db_column="predkosc_wiatru")
    material = models.ForeignKey(Material, models.DO_NOTHING)
    base = models.ForeignKey(Base, models.DO_NOTHING, db_column="podloze")
    ricochet = models.ForeignKey(Ricochet, models.DO_NOTHING, db_column="rykoszet", null=True, blank=True)
    factor = models.ForeignKey(Factor, models.DO_NOTHING, db_column="czynnik")
    link = models.CharField(max_length=80)
    link_caliber = models.CharField(verbose_name="link kaliber", max_length=80, default="1", db_column="link_kaliber")
    camera = models.CharField(verbose_name="kamera zwykła", max_length=64, default="1", db_column="kamera_zwykla")
    slowmotion_camera = models.CharField(verbose_name="kamera szybka", max_length=64, default="1", db_column="kamera_szybka")
    ir_camera = models.CharField(verbose_name="kamera ir", max_length=64, default="1", db_column="kamera_ir")
    photo = models.ImageField(verbose_name="zdjęcie", upload_to="images/", null=True, db_column="zdjecie")

    class Meta:
        db_table = "Proba_Strzelnicza"
        verbose_name = "Próba Strzelnicza"
        verbose_name_plural = "Próby Strzelnicze"

    def __str__(self):
        return f"{self.sample_id} ({self.weapon}, {self.bullet})"

