# coding: utf-8

# In[4]:

from IPython import display, get_ipython
from IPython.core import magic_arguments
from typing import Callable
from toolz.curried import partial, pipe, reduce

__all__ = ['magical']


# > Evaluate arbitrary variables that can be added to the global context by
# defining a name.

# {% raw %}

# In[119]:

@magic_arguments.magic_arguments()
@magic_arguments.argument(
    "name",
    default='markdown',
    nargs="?",
    help="""Name of local variable to set to parsed value""",
)
@magic_arguments.argument(
    "-d",
    "--display",
    default='Markdown',
    nargs="?",
    help="""An IPython.display method."""
)
def _wraps_magic(f, line, cell="""""", **kwargs):
    def _preprocess_line(line):
        """I don't understand how I would use this yet."""
        return line.strip().split(' ', 1)

    if not cell:
        line, cell = _preprocess_line(line)

    args = magic_arguments.parse_argstring(_wraps_magic, line.strip())

    retval = f(cell)

    if args.name:
        if '.' in args.name or '[' in args.name:
            path = args.name.split('.')
            var = get_ipython().user_ns[path[0]]
            setattr(reduce(
                lambda x, y: getattr(x, y) if hasattr(x, y) else x[y],
                path[1:-1],
                var
            ), path[-1], retval)
        else:
            get_ipython().user_ns[args.name] = retval

    if args.display:
        disp = kwargs['display'] if 'display' in kwargs else args.display
        if isinstance(disp, str):
            return display.display(getattr(display, disp)(retval))
        elif isinstance(disp, Callable):
            return disp(retval)


def magical(name, lang=None, **kwargs):
    if lang:
        # Syntax highlighting
        pipe("""require([
                    "notebook/js/codecell",
                    "codemirror/mode/{0}/{0}"
                ],
                function(cc){{
                    cc.CodeCell.options_default.highlight_modes.magic_{1} = {{
                        reg: ["^%%{1}"]
                    }};
                }}
            );
            """.format(lang, name),
             display.Javascript, display.display,
             )

    def _register(method):
        get_ipython().register_magic_function(
            partial(_wraps_magic, method, **kwargs),
            magic_kind='line_cell', magic_name=name
        )
    return _register


# {% endraw %}
