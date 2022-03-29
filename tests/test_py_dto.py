import unittest
from typing import Any, Optional
from py_dto import DTO


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

        for prop in properties:
            o = TestDTO({'test_any': prop})

            self.assertEqual(type(o.test_any), type(prop))

    def test_allows_nones(self):
        class TestDTO(DTO):
            test_str_or_none: Optional[str]

        o = TestDTO({'test_str_or_none': None})
        self.assertEqual(o.test_str_or_none, None)

        o = TestDTO({'test_str_or_none': 'test'})
        self.assertEqual(o.test_str_or_none, 'test')

        with self.assertRaises(TypeError):
            TestDTO({'test_str_or_none': 42})

    def test_does_not_allow_nones(self):
        class TestDTO(DTO):
            test_str_not_none: str

        o = TestDTO({'test_str_not_none': 'test'})
        self.assertEqual(o.test_str_not_none, 'test')

        with self.assertRaises(TypeError):
            TestDTO({'test_str_not_none': None})

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

    def test_without_missing_keys(self):
        class TestDTO(DTO):
            a: str
            b: str

        with self.assertRaises(KeyError):
            TestDTO({'a': 'test'})

        with self.assertRaises(KeyError):
            TestDTO({'a': 'test'}, allows_missing_keys=False)

    def test_with_missing_keys(self):
        class TestDTO(DTO):
            a: str
            b: str

        o = TestDTO({'a': 'test'}, allows_missing_keys=True)
        self.assertEqual(o.__dict__, {'a': 'test'})
        self.assertFalse(hasattr(o, 'b'))

        o = TestDTO({}, allows_missing_keys=True)
        self.assertEqual(o.__dict__, {})

    def test_list_of_types_error(self):
        class TestA(DTO):
            test_list_of_types: list[int]

        with self.assertRaises(TypeError):
            TestA({'test_list_of_types': ['fail']})

        class TestB(DTO):
            test_list_of_types: dict[str, int]

        with self.assertRaises(TypeError):
            TestB({'test_list_of_types': {'a': 'fail'}})

    def test_readme_usage_example(self):
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

    def test_readme_any_example(self):
        # The DTO accepts "any" type of data for the "name" property
        class User(DTO):
            name: Any

        # Create the DTO instance
        user = User({
            'name': 'John',
        })

        self.assertEqual(user.name, 'John')

        user = User({
            'name': 123,
        })

        self.assertEqual(user.name, 123)

    def test_readme_none_example(self):
        # The DTO "name" property can be a str or a None value
        class User(DTO):
            name: Optional[str]

        # Create the DTO instance with a "str"
        user = User({
            'name': 'John',
        })

        self.assertEqual(user.name, 'John')

        # Create the DTO instance with a "None"
        user = User({
            'name': None,
        })

        self.assertEqual(user.name, None)

        # Any other type will raise an exception
        with self.assertRaises(TypeError):
            user = User({
                'name': 123,
            })


if __name__ == '__main__':
    unittest.main()
