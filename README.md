# Python DTO

<p align="center"><img height="200" alt="rogervila/py_dto" src="https://image.flaticon.com/icons/png/512/2911/2911162.png" /></p>

[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=rogervila_py_dto&metric=coverage)](https://sonarcloud.io/dashboard?id=rogervila_py_dto)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=rogervila_py_dto&metric=alert_status)](https://sonarcloud.io/dashboard?id=rogervila_py_dto)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=rogervila_py_dto&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=rogervila_py_dto)

Data Transfer Objects (DTO) with Python.


## Install

```sh
pip install py_dto
```

## Usage

Define your object properties with types defined.

You can use custom objects and the `Any` type.

### Example

We will create a User DTO with some properties.

```py
from py_dto import DTO

# This DTO will be used as a type definition
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

print(user.name) # 'John'
print(user.profile.avatar) # https://i.pravatar.cc/300
```

## License

This project is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).

Original idea comes from [spatie/data-transfer-object](https://github.com/spatie/data-transfer-object) package for PHP.

<div>Icons made by <a href="https://www.flaticon.com/authors/pixel-perfect" title="Pixel perfect">Pixel perfect</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
