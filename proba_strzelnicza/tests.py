from django.test import TestCase

from proba_strzelnicza.models import (
    Bullet,
    Factor,
    Material,
    Weapon
)
from proba_strzelnicza.tests_utils.factories import (
    FactorFactory,
    MaterialFactory,
    faker
)


class TestWeapon(TestCase):
    model = Weapon

    _TEST_NAMES = (faker.name(), faker.name(), faker.name(), faker.name())

    def setUp(self) -> None:
        for name in self._TEST_NAMES:
            self.model.objects.create(name=name)

    def tearDown(self) -> None:
        self.model.objects.all().delete()

    @property
    def objects_count(self):
        return self.model.objects.count()

    @property
    def all_objects(self):
        return self.model.objects.all()

    def test_create(self):
        new_object_name = faker.name()
        initial_objects_count = self.objects_count
        assert initial_objects_count == 4
        assert new_object_name not in self.all_objects.values_list("name", flat=True)
        self.model.objects.create(name=new_object_name)
        assert self.objects_count == initial_objects_count + 1

    def test_retrieve(self):
        for object in self.all_objects:
            assert self.model.objects.get(name=object.name)

    def test_update(self):
        new_names = {name: faker.name() for name in self._TEST_NAMES}
        for old, new in new_names.items():
            obj = self.model.objects.get(name=old)
            obj.name = new
            obj.save()
        assert self.model.objects.filter(name__in=self._TEST_NAMES).count() == 0
        assert self.model.objects.filter(name__in=new_names.values()).count() == 4

    def test_delete(self):
        self.model.objects.first().delete()
        assert self.objects_count == 3


class TestBullet(TestWeapon):
    model = Bullet


class TestFactor(TestCase):
    model = Factor
    factory = FactorFactory
    initial_objects_count = 10

    def setUp(self):
        for object in self.build_new_objects(count=self.initial_objects_count):
            object.save()

    def tearDown(self):
        self.model.objects.all().delete()

    def build_new_objects(self, count: int = 1):
        objects = self.factory.build_batch(size=count)
        return objects

    @property
    def objects_count(self) -> int:
        return self.model.objects.count()

    @property
    def all_objects(self):
        return self.model.objects.all()

    def test_create(self):
        new_objects_count = 3
        for new_object in self.build_new_objects(count=new_objects_count):
            new_object.save()
        assert self.objects_count == self.initial_objects_count + new_objects_count

    def test_retrieve(self):
        for obj in self.all_objects:
            assert self.model.objects.get(id=obj.id)

    def test_update(self):
        new_names = {
            name: faker.name()
            for name in self.all_objects.values_list("name", flat=True)
        }
        for old, new in new_names.items():
            obj = self.model.objects.get(name=old)
            obj.name = new
            obj.save()
        assert self.model.objects.filter(name__in=new_names.keys()).count() == 0
        assert (
                self.model.objects.filter(name__in=new_names.values()).count()
                == self.initial_objects_count
        )

    def test_delete(self):
        self.model.objects.first().delete()
        assert self.objects_count == self.initial_objects_count - 1


class TestMaterial(TestCase):
    model = Material
    factory = MaterialFactory
    initial_objects_count = 10

    def save_object(self, new_object):
        new_object.factor.save()
        new_object.save()

    def setUp(self):
        for object in self.build_new_objects(count=self.initial_objects_count):
            self.save_object(object)

    def tearDown(self):
        Factor.objects.all().delete()
        self.model.objects.all().delete()

    def build_new_objects(self, count: int = 1):
        objects = self.factory.build_batch(size=count)
        return objects

    @property
    def objects_count(self) -> int:
        return self.model.objects.count()

    @property
    def all_objects(self):
        return self.model.objects.all()

    def test_create(self):
        new_objects_count = 3
        for new_object in self.build_new_objects(count=new_objects_count):
            self.save_object(new_object)
        assert self.objects_count == self.initial_objects_count + new_objects_count

    def test_retrieve(self):
        for obj in self.all_objects:
            assert self.model.objects.get(id=obj.id)

    def test_update(self):
        new_types = {
            material_type: faker.name()
            for material_type in self.all_objects.values_list(
                "material_type", flat=True
            )
        }
        for old, new in new_types.items():
            obj = self.model.objects.get(material_type=old)
            obj.material_type = new
            obj.save()
        assert (
                self.model.objects.filter(material_type__in=new_types.keys()).count() == 0
        )
        assert (
                self.model.objects.filter(material_type__in=new_types.values()).count()
                == self.initial_objects_count
        )

    def test_delete(self):
        self.model.objects.first().delete()
        assert self.objects_count == self.initial_objects_count - 1
