# -*- coding: utf-8 -*-
# convert Zg to Unicode (replace,decompose,visual2logical)
import re

def replace(input):
    output = input
    #  nyalay

    output = output.replace(u'\u106A', u'\u1009')

    #  nya
    output = output.replace(u'\u106B', u'\u100A')

    #  yakaut
    output = output.replace(u'\u1090', u'\u101B')

    #  1chaungngin
    output = output.replace(u'\u1033', u'\u102F')

    #  2chaungngin
    output = output.replace(u'\u1034', u'\u1030')

    #  hahtoe
    output = output.replace(u'\u103D', u'\u103E')
    output = output.replace(u'\u1087', u'\u103E')

    #  waswae
    output = output.replace(u'\u103C', u'\u103D')

    #  yayit

    output = output.replace(u'\u103B', u'\u103C')
    output = output.replace(u'\u107E', u'\u103C')
    output = output.replace(u'\u107F', u'\u103C')
    output = output.replace(u'\u1080', u'\u103C')
    output = output.replace(u'\u1081', u'\u103C')
    output = output.replace(u'\u1082', u'\u103C')
    output = output.replace(u'\u1083', u'\u103C')
    output = output.replace(u'\u1084', u'\u103C')

    #  yapin
    output = output.replace(u'\u103A', u'\u103B')
    output = output.replace(u'\u107D', u'\u103B')

    #  htawonbae

    #  dayinkaut

    #  tatalin

    #  athat
    output = output.replace(u'\u1039', u'\u103A')

    #  outkamyint
    output = output.replace(u'\u1094', u'\u1037')
    output = output.replace(u'\u1095', u'\u1037')

    #  na
    output = output.replace(u'\u108F', u'\u1014')

    #  thagyi
    output = output.replace(u'\u1086', u'\u103F')

return output
