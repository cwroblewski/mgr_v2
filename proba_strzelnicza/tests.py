from django.test import TestCase

from proba_strzelnicza.models import (
    Bullet,
    Factor,
    Weapon
)
from proba_strzelnicza.tests_utils.factories import FactorFactory


class TestWeapon(TestCase):
    model = Weapon

    _TEST_NAMES = (
        "Test_1",
        "Test_2",
        "Test_3",
        "Test_4",
    )

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
        new_object_name = "Test_5"
        initial_objects_count = self.objects_count
        assert initial_objects_count == 4
        assert new_object_name not in self.all_objects.values_list("name", flat=True)
        self.model.objects.create(name=new_object_name)
        assert self.objects_count == initial_objects_count + 1

    def test_retrieve(self):
        for object in self.all_objects:
            assert self.model.objects.get(name=object.name)

    def test_update(self):
        new_names = {
            name: "Test_" + str(int(name[-1]) + 4) for name in self._TEST_NAMES
        }
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
        for object in self.factory.build_batch(size=self.initial_objects_count):
            object.save()

    def tearDown(self):
        self.model.objects.all().delete()

    def build_new_object(self, count: int = 1):
        obj = self.factory.build_batch(size=count)
        return obj

    @property
    def objects_count(self) -> int:
        return self.model.objects.count()

    @property
    def all_objects(self):
        return self.model.objects.all()

    def test_create(self):
        for new_object in self.build_new_object(count=3):
            new_object.save()
        assert self.objects_count == self.initial_objects_count + 3

        # assert new_object not in self.all_objects.values_list("name", flat=True)
        # self.model.objects.create(name=new_object_name)
        # assert self.objects_count == initial_objects_count + 1

    #
    # def test_retrieve(self):
    #     for object in self.all_objects:
    #         assert self.model.objects.get(name=object.name)
    #
    # def test_update(self):
    #     new_names = {
    #         name: "Test_" + str(int(name[-1]) + 4) for name in self._TEST_NAMES
    #     }
    #     for old, new in new_names.items():
    #         obj = self.model.objects.get(name=old)
    #         obj.name = new
    #         obj.save()
    #     assert self.model.objects.filter(name__in=self._TEST_NAMES).count() == 0
    #     assert self.model.objects.filter(name__in=new_names.values()).count() == 4
    #
    # def test_delete(self):
    #     self.model.objects.first().delete()
    #     assert self.objects_count == 3
