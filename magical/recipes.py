# coding: utf-8

# In[72]:

from magical.magic import magical
from toolz.curried import compose, partial
from jinja2 import Environment, Template
import IPython
from mistune import markdown
import yaml

__all__ = [
    'register_jinja2_magic', 'register_mistune_magic', 'register_yaml_magic',
]


# In[51]:

def _render_jinja2_with_globals(template):
    return template.render(
        **IPython.get_ipython().user_ns
    )


# In[63]:

def register_jinja2_magic(env=Environment(), display='Markdown'):
    """Display reusable jinja2 templates.  Returns a jinja2 template.
    """
    magical(
        'jinja2', lang='jinja2',
        display=compose(
            IPython.display.display,
            IPython.display.Markdown,
            lambda x: x.render(**IPython.get_ipython().user_ns),
        )
    )(env.from_string)
    return env


# In[61]:

def register_mistune_magic(**kwargs):
    magical('mistune', display='HTML', lang='markdown')(
        compose(partial(markdown, **kwargs),
                _render_jinja2_with_globals, Template)
    )


# In[54]:

def register_yaml_magic(loader=yaml.SafeLoader):
    magical('yaml', display=print, lang='yaml')(
        compose(partial(yaml.load, Loader=loader),
                _render_jinja2_with_globals, Template)
    )
register_yaml_magic()
