Django CMS 3 WYMeditor Text Plugin
==================================

A plugin that allows text content to be edited in WYMeditor and saved in Django
CMS 3. Meant as a replacement for the WYMeditor text plugin in Django CMS 2.

Compatibility
-------------

At the moment, the only browser the plugin has fully worked in is Google Chrome.
The editor has not been working correctly in Firefox, and the plugin has not
been tested in any other browsers.

Install
-------

1. Clone the git repo.
    
    ```
    $ git clone https://github.com/FriedRice/djangocms_wymeditor_plugin.git
    ```

2. Install the requirements (i.e. Django CMS 3).
    
    ```
    $ pip install -r requirements.txt
    ```

3. Install the plugin.
    
    ```
    $ python setup.py install
    ```

4. Add the string `'djangocms_wymeditor_plugin'` to `INSTALLED_APPS` in the
   Django settings file of a Django CMS 3 project.

5. Sync the database for the Django CMS 3 project.
    
    ```
    $ python manage.py syncdb
    ```

6. (Optional) Configure custom settings for WYMeditor by adding any of the
   following options to the Django settings file.

* `WYM_TOOLS`
* `WYM_CONTAINERS`
* `WYM_CLASSES`
* `WYM_STYLES`
* `WYM_STYLESHEET`
