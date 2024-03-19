#!/usr/bin/env python3

import os

package_dir = '/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[0:-1])
db_dir = os.path.join(package_dir, 'freebies.db')
SQLITE_URL = ''.join(['sqlite:///', db_dir])