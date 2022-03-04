from random import (
    randint,
    random
)

import factory
from faker import Faker

faker = Faker()

from proba_strzelnicza.models import (
    Factor,
    Material
)


class FactorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Factor

    name = factory.LazyAttribute(lambda _: faker.name())
    parameter = factory.LazyAttribute(lambda _: faker.name())
    temperature = factory.LazyAttribute(lambda _: randint(0, 30))
    filling = factory.LazyAttribute(lambda _: random())


class MaterialFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Material

    material_type = factory.LazyAttribute(lambda _: faker.name())
    factor = factory.SubFactory(FactorFactory)
