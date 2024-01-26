#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import sys
import os
import django


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    django.setup()


if __name__ == '__main__':
    main()
