from __future__ import annotations

import unittest
from typing import Optional

from py_dto import DTO


class FutureProfile(DTO):
    avatar: str


class FutureUser(DTO):
    profile: FutureProfile
    name: str
    tags: list[str]
    nickname: Optional[str]


class test_future_annotations(unittest.TestCase):
    def test_module_level_postponed_annotations(self):
        user = FutureUser({
            'profile': FutureProfile({'avatar': 'https://example.com/avatar.png'}),
            'name': 'John',
            'tags': ['developer', 'python'],
            'nickname': None,
        })

        self.assertEqual(user.profile.avatar, 'https://example.com/avatar.png')
        self.assertEqual(user.tags, ['developer', 'python'])
        self.assertEqual(user.nickname, None)

        with self.assertRaises(TypeError):
            FutureUser({
                'profile': FutureProfile({'avatar': 'https://example.com/avatar.png'}),
                'name': 'John',
                'tags': ['developer', 42],
                'nickname': None,
            })

    def test_local_builtin_postponed_annotations(self):
        class LocalDTO(DTO):
            names: list[str]
            nickname: Optional[str]

        local_dto = LocalDTO({
            'names': ['John', 'Jane'],
            'nickname': 'JJ',
        })

        self.assertEqual(local_dto.names, ['John', 'Jane'])
        self.assertEqual(local_dto.nickname, 'JJ')

        with self.assertRaises(TypeError):
            LocalDTO({
                'names': ['John', 123],
                'nickname': None,
            })


if __name__ == '__main__':
    unittest.main()
