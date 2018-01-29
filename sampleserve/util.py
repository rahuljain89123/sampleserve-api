
"""

Util functions for the app. Hashids allows 8 character URL slugs to be used instead
of model ids. Implemented with matching params in JS.

"""
import random
import string

from hashids import Hashids

hashids = Hashids('SampleServe', 8, 'abcdefghijklmnopqrstuvwxyz')


def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
