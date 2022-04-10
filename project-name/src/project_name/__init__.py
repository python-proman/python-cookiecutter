# -*- coding: utf-8 -*-
# copyright: Copyright (C) [2022] [Jesse P. Johnson]
# license: unlicensed, see LICENSE.md for more details.

import logging
from typing import List

__author__ = 'Jesse P. Johnson'
__title__ = 'project_name'
__version__ = '0.1.0'
__all__: List[str] = []

logging.getLogger(__name__).addHandler(logging.NullHandler())
