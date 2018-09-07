# -*- coding: utf-8 -*-
import re


def replace(input):
    output = input
    output = output.replace(u'\u004F', u'\u1025')  # u
    output = output.replace(u'\u00CD', u'\u1009')  # nya-lay
    output = output.replace(u'\u00DA', u'\u1009')

    #  #####Consonent
    output = output.replace(u'\u0075', u'\u1000')  # ka
    output = output.replace(u'\u0063', u'\u1001')  # kha
    output = output.replace(u'\u002A', u'\u1002')  # ga-nge
    output = output.replace(u'\u0043', u'\u1003')  # ga-gyi
    output = output.replace(u'\u0069', u'\u1004')  # nga
    output = output.replace(u'\u0070', u'\u1005')  # sa-lone
    output = output.replace(u'\u0071', u'\u1006')  # sa-lane
    output = output.replace(u'\u005A', u'\u1007')  # za
    output = output.replace(u'\u006E', u'\u100A')  # nya
    output = output.replace(u'\u00F1', u'\u100A')
    output = output.replace(u'\u0023', u'\u100B')  # ta-ta-lin
    output = output.replace(u'\u0058', u'\u100C')  # hta-won-bae
    output = output.replace(u'\u007C', u'\u100B\u1039\u100C')  # hta-won-bae-ayit
    output = output.replace(u'\u0021', u'\u100D')  # da-yin-kaut
    output = output.replace(u'\u00A1', u'\u100E')  # da-yin-mote
    output = output.replace(u'\u0050', u'\u100F')  # na-gyi
    output = output.replace(u'\u0077', u'\u1010')  # ta-won-pu
    output = output.replace(u'\u0078', u'\u1011')  # hta-sin-htoo
    output = output.replace(u'\u0027', u'\u1012')  # da-dway
    output = output.replace(u'\u0022', u'\u1013')  # da-out-chaint
    output = output.replace(u'\u0065', u'\u1014')  # na
    output = output.replace(u'\u0045', u'\u1014')
    output = output.replace(u'\u0079', u'\u1015')  # pa
    output = output.replace(u'\u007A', u'\u1016')  # pha
    output = output.replace(u'\u0041', u'\u1017')  # ba-htet
    output = output.replace(u'\u0062', u'\u1018')  # ba
    output = output.replace(u'\u0072', u'\u1019')  # ma
    output = output.replace(u'\u002C', u'\u101A')  # ya-pa-lat
    output = output.replace(u'\u0026', u'\u101B')  # ya-kaut
    output = output.replace(u'\u00BD', u'\u101B')
    output = output.replace(u'\u0076', u'\u101C')  # la
    output = output.replace(u'\u0030', u'\u101D')
    output = output.replace(u'\u1040', u'\u101D')
    output = output.replace(u'\u0030', u'\u1040')  # wa

    output = output.replace(u'\u006F', u'\u101E')  # tha
    output = output.replace(u'\u005B', u'\u101F')  # ha
    output = output.replace(u'\u0056', u'\u1020')  # la-gyi
    output = output.replace(u'\u0074', u'\u1021')  # ah

    return output
