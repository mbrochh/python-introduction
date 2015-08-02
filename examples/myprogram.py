#!/usr/bin/env python
import datetime
from django.db import models


my_variable = "Foobar"


def get_current_time():
    return datetime.datetime.now()


print my_variable

print get_current_time()

for number in range(10):
    if number == 4:
        print "Number 5 is the best!"
    else:
        print number
