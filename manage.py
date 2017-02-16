<<<<<<< HEAD
#!/usr/bin/env python3.5
=======
#!/usr/bin/env python
>>>>>>> 3b3f517aec6e98ef1f398d1daede2741a6958cf0
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Account.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
>>>>>>> 3b3f517aec6e98ef1f398d1daede2741a6958cf0
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
