from random import (
    randint,
    random
)

import factory
from factory import (
    django,
    fuzzy
)
from faker import Faker

faker = Faker()

from proba_strzelnicza.models import (
    Base,
    Bullet,
    Factor,
    Material,
    Ricochet,
    Shot,
    Weapon
)


class FactorFactory(django.DjangoModelFactory):
    class Meta:
        model = Factor

    name = factory.LazyAttribute(lambda _: faker.name())
    parameter = factory.LazyAttribute(lambda _: faker.name())
    temperature = factory.LazyAttribute(lambda _: randint(0, 30))
    filling = factory.LazyAttribute(lambda _: random())


class MaterialFactory(django.DjangoModelFactory):
    class Meta:
        model = Material

    material_type = factory.LazyAttribute(lambda _: faker.name())
    factor = factory.SubFactory(FactorFactory)


class WeaponFactory(django.DjangoModelFactory):
    class Meta:
        model = Weapon

    name = factory.LazyAttribute(lambda _: faker.name())


class BulletFactory(django.DjangoModelFactory):
    class Meta:
        model = Bullet

    name = factory.LazyAttribute(lambda _: faker.name())


class BaseFactory(django.DjangoModelFactory):
    class Meta:
        model = Base

    base = factory.LazyAttribute(lambda _: faker.name())


class RicochetFactory(django.DjangoModelFactory):
    class Meta:
        model = Ricochet

    material = factory.SubFactory(MaterialFactory)


class ShotFactory(django.DjangoModelFactory):
    class Meta:
        model = Shot

    sample_id = factory.Sequence(lambda n: n)
    weapon = factory.SubFactory(WeaponFactory)
    bullet = factory.SubFactory(BulletFactory)
    temperature = factory.LazyAttribute(lambda _: randint(0, 30))
    atmosferic_conditions = fuzzy.FuzzyText(length=512)
    wind_speed = factory.LazyAttribute(lambda _: randint(0, 30))
    material = factory.SubFactory(MaterialFactory)
    base = factory.SubFactory(BaseFactory)
    ricochet = factory.SubFactory(RicochetFactory)
    factor = factory.SubFactory(FactorFactory)
    link = factory.LazyFunction(faker.url)
    link_caliber = factory.LazyAttribute(lambda _: str(randint(1, 80)))
    camera = factory.LazyAttribute(lambda _: faker.name())
    slowmotion_camera = factory.LazyAttribute(lambda _: faker.name())
    ir_camera = factory.LazyAttribute(lambda _: faker.name())
    photo = factory.django.ImageField(color="blue")
