import sys
import os
import datetime
from jasily.objects import Guid

folder = os.path.dirname(sys.argv[0])
name = datetime.datetime.now().strftime("%Y-%m-%d-") + Guid().to_string().upper() + '.md'

with open(os.path.join(folder, name), 'w', encoding='utf8', newline='\r\n') as writer:
    writer.write('---\n')
    writer.write('categories: \n')
    writer.write('title: \n')
    writer.write('layout: \n')
    writer.write('---\n')
