# Python 3.14 compatibility patch for Django BaseContext copying (Django Ticket #35844)
from copy import copy
from django.template import context


def _patched_copy(self):
    duplicate = context.BaseContext()
    duplicate.__class__ = self.__class__
    duplicate.__dict__ = copy(self.__dict__)
    duplicate.dicts = self.dicts[:]
    return duplicate


context.BaseContext.__copy__ = _patched_copy

