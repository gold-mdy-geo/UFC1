# -*- coding: utf-8 -*-

# Usage: main.py inputfilename.ext outputfilename.ext
# Example: main.py zawgyi.txt unicode.txt

import codecs
import sys


input_file_name = sys.argv[1]
output_file_name = sys.argv[2]
input_file = codes.open(input_file_name, encoding='utf-8')
output_file = codecs.open(output_file_name, encoding='utf-8', mode='w')

input_file.close()
output_file.close()
