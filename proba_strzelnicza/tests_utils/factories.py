from random import (
    randint,
    random
)

import factory
from factory.django import DjangoModelFactory
from faker import Faker

faker = Faker()

from proba_strzelnicza.models import Factor


class FactorFactory(DjangoModelFactory):
    class Meta:
        model = Factor

    name = factory.LazyAttribute(lambda _: faker.name())
    parameter = factory.LazyAttribute(lambda _: faker.name())
    temperature = factory.LazyAttribute(lambda _: randint(0, 30))
    filling = factory.LazyAttribute(lambda _: random())
