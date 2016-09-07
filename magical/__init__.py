# coding: utf-8

# In[3]:

from magical.magic import magical
from magical.recipes import (
    register_jinja2_magic,
    register_mistune_magic,
    register_yaml_magic
)

__version__ = "0.0.9"

magical

__all__ = [
    'magical', 'register_jinja2_magic',
    'register_mistune_magic', 'register_yaml_magic',
]
