import unittest
from py_dto import DTO
from typing import Any


class test_py_dto(unittest.TestCase):
    def test_object_property_types(self):
        class TestDTO(DTO):
            test_string: str
            test_integer: int

        o = TestDTO({'test_string': 'I am a string', 'test_integer': 1714})

        self.assertEqual(o.test_string, 'I am a string')
        self.assertEqual(o.test_integer, 1714)

    def test_fails_if_property_is_not_defined(self):
        with self.assertRaises(ValueError):
            class TestDTO(DTO):
                test_list: list

            TestDTO({'test_list': [1, 2, 3], 'this_will_fail': 'the failure'})

    def test_fails_if_property_type_is_incorrect(self):
        with self.assertRaises(TypeError):
            class TestDTO(DTO):
                test_dict: dict

            TestDTO({'test_dict': 'not a dict'})

    def test_object_properties_are_not_set_when_no_values(self):
        class TestDTO(DTO):
            test_string: str

        o = TestDTO({})

        self.assertEqual(o.__dict__, {})
        self.assertFalse(hasattr(o, 'test_string'))

    def test_exception_property_types(self):
        class TestDTO(DTO):
            test_exception: ValueError

        o = TestDTO({'test_exception': ValueError()})

        self.assertEqual(type(o.test_exception), ValueError)

    def test_custom_property_types(self):
        class MyObject():
            pass

        class TestDTO(DTO):
            test_custom: MyObject

        o = TestDTO({'test_custom': MyObject()})

        self.assertEqual(type(o.test_custom), MyObject)

    def test_any_type(self):
        class TestDTO(DTO):
            test_any: Any

        properties = ['string', 0, 1.2, [], {}, Exception]

        for property in properties:
            o = TestDTO({'test_any': property})

            self.assertEqual(type(o.test_any), type(property))

    def test_allows_nones(self):
        class TestDTO(DTO):
            test_str_or_none: str

        o = TestDTO({'test_str_or_none': None}, allows_nones=True)

        self.assertEqual(o.test_str_or_none, None)

    def test_does_not_allow_nones(self):
        class TestDTO(DTO):
            test_str_or_none: str

        with self.assertRaises(TypeError):
            TestDTO({'test_str_or_none': None}, allows_nones=False)

        with self.assertRaises(TypeError):
            TestDTO({'test_str_or_none': None})

    def test_exception_return_dictionary_key(self):
        class TestDTO(DTO):
            test_error_type: str
            test_correct_type: int

        try:
            TestDTO({
                'test_error_type': int(1),
                'test_correct_type': int(1)
            })
        except TypeError as e:
            self.assertEqual(e.args[0], 'test_error_type')

    def test_list_of_types(self):
        class TestA(DTO):
            test_list_of_types: list[int]

        o = TestA({'test_list_of_types': [1]})

        self.assertEqual(o.test_list_of_types, [1])

        class TestB(DTO):
            test_list_of_types: dict[str, int]

        o = TestB({'test_list_of_types': {'a': 42}})

        self.assertEqual(o.test_list_of_types, {'a': 42})

    def test_list_of_types_error(self):
        class TestA(DTO):
            test_list_of_types: list[int]

        with self.assertRaises(TypeError):
            TestA({'test_list_of_types': ['fail']})

        class TestB(DTO):
            test_list_of_types: dict[str, int]

        with self.assertRaises(TypeError):
            TestB({'test_list_of_types': {'a': 'fail'}})

    def test_readme_example(self):
        class UserProfile(DTO):
            avatar: str

        # The DTO with the properties defined
        class User(DTO):
            profile: UserProfile
            name: str
            email: str
            age: int
            tags: list[str]

        # Create the DTO instance
        user = User({
            'profile': UserProfile({'avatar': 'https://i.pravatar.cc/300'}),
            'name': 'John',
            'email': 'john@example.com',
            'age': 42,
            'tags': ['developer', 'python']
        })

        self.assertEqual(user.name, 'John')
        self.assertEqual(user.profile.avatar, 'https://i.pravatar.cc/300')


if __name__ == '__main__':
    unittest.main()
