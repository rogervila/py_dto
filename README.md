# Python DTO

<p align="center"><img height="200" alt="rogervila/py_dto" src="https://rogervila.es/static/img/py_dto.png" /></p>

[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=rogervila_py_dto&metric=coverage)](https://sonarcloud.io/dashboard?id=rogervila_py_dto)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=rogervila_py_dto&metric=alert_status)](https://sonarcloud.io/dashboard?id=rogervila_py_dto)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=rogervila_py_dto&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=rogervila_py_dto)

Data Transfer Objects (DTO) with Python.


## Install

```sh
pip install py_dto
```

## Usage

Define the object properties with types defined, then pass a `dict` with data.

### Basic example

For type hinting

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

### The `Any` type

Even DTO are supposed to specify data types, you can use the `Any` type to accept literally any type for a property:

```py
from py_dto import DTO
from typing import Any

# The DTO accepts "any" type of data for the "name" property
class User(DTO):
    name: Any

# Create the DTO instance
user = User({
    'name': 'John',
})

print(user.name) # 'John'

user = User({
    'name': 123,
})

print(user.name) # 123
```

### Dealing with `None`

Imagine you are retrieving data from a database table where a column is empty for some records.

By using python's `Optional` type on a specific property, the DTO will not raise an exception if a `None` value is set.

```py
from py_dto import DTO
from typing import Optional

# The DTO "name" property can be a str or a None value
class User(DTO):
    name: Optional[str]

# Create the DTO instance with a "str"
user = User({
    'name': 'John',
})

print(user.name) # 'John'

# Create the DTO instance with a "None"
user = User({
    'name': None,
})

print(user.name) # None

# Any other type will raise an exception
try:
    user = User({
        'name': 123,
    })
except:
    print('123 does not have a "str" nor a "None" type')
```

## License

This project is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).

Original idea comes from [spatie/data-transfer-object](https://github.com/spatie/data-transfer-object) package for PHP.

<div>Icons made by <a href="https://www.flaticon.com/authors/pixel-perfect" title="Pixel perfect">Pixel perfect</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
