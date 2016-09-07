
``magical-magic``
=================

Dead simple reusable ``IPython`` magics.

Installation
------------

``pip install magical-magic``

Basic Usage
-----------

.. code:: python

    import magical
    env = magical.register_jinja2_magic() # returns a jinja environment
    magical.register_mistune_magic(escape=False)
    magical.register_yaml_magic()



.. parsed-literal::

    <IPython.core.display.Javascript object>



.. parsed-literal::

    <IPython.core.display.Javascript object>



.. parsed-literal::

    <IPython.core.display.Javascript object>


.. code:: python

    data = {'🐮': 'moo', '🐑': 'bah', '🔥': 'burn'}

.. code:: python

    %%jinja2 
    # Jinja Cell Magics
    
    `%%jinja2` inserts data from the notebook into the template.  
    
    ## An example of a list
    
    {% for key in data %}* {{key}} - __{{data[key]}}__
    {% endfor %}



Jinja Cell Magics
=================

``%%jinja2`` inserts data from the notebook into the template.

An example of a list
--------------------

-  🐮 - **moo**
-  🔥 - **burn**
-  🐑 - **bah**


--------------

.. code:: python

    %%mistune
    ## Mistune Cell Magics
    
    `%%mistune` uses a pure Python markdown parser.  For convenience, jinja templates can be used to 
    tell us about the length of `data` is {{data.__len__()}}.



.. raw:: html

    <h2>Mistune Cell Magics</h2>
    <p><code>%%mistune</code> uses a pure Python markdown parser.  For convenience, jinja templates can be used to 
    tell us about the length of <code>data</code> is 3.</p>



--------------

Development
-----------

Running the Build and Tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    pip install -r requirements-dev.txt
    python setup.py develop
    watchmedo tricks tricks.yaml

The ``watchmedo`` script will convert your notebooks to scripts and html
files. ``py.test-ipynb`` will test all notebooks matching
``test-*.ipynb``.

Running the docs
^^^^^^^^^^^^^^^^

::

    jekyll serve docs -wit

Docs are hosted at ``http://localhost:4000/magical-magic/``.

License
-------

``magical-magic`` is released as free software under the `BSD 3-Clause
license <https://github.com/tonyfast/magical-magic/blob/master/LICENSE>`__.
