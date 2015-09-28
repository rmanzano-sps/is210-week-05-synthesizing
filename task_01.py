#!/usr/env python
# -*- coding: utf-8 -*-
"""function that returns today's date and also conditionally executes that date
if it's run on the command line"""

import datetime

CURDATE = None

def get_current_date():
    return datetime.date.today()

if __name__ == "__main__":
        CURDATE = get_current_date()
