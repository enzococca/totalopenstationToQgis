#! /usr/bin/env python
# -*- coding: utf-8 -*-
# filename: upref.py
# Copyright 2019 Stefano Costa <steko@iosa.it>
# Copyright 2010 Luca Bianconi <luxetluc@yahoo.it>
#
# This file is part of Total Open Station.
#
# Total Open Station is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Total Open Station is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Total Open Station.  If not, see
# <http://www.gnu.org/licenses/>.

import atexit
import logging
import os
import os.path

from configparser import ConfigParser, NoSectionError, NoOptionError

logger = logging.getLogger(__name__)

class UserPrefs(ConfigParser):
    '''Manage user preferences for GUI options and last used values.

    Proof-of-concept. Notes:

    * user preferences path is hardcoded here
    * returns a dictionary of user preferences
    * preferences will be set through a dictionary as well'''

    OPTIONS = {
        'model': '',
        'port': '',
        'sleeptime': '1.0',       # added in 0.3.1
    }

    def __init__(self):

        ConfigParser.__init__(self)

        USER_PREFS_PATH = '~/.totalopenstation/totalopenstation.cfg'

        self.upref = os.path.expanduser(USER_PREFS_PATH)

        try:
            with open(self.upref) as f:
                self.read(f)
        except FileNotFoundError:
                self.initfile()
        else:
            try:
                self.getvalue('model')
            except NoSectionError:
                self.initfile()


    def initfile(self):
        try:
            self.write()
        except FileNotFoundError:
            os.mkdir(os.path.dirname(self.upref))
        finally:
            self.write()
        logger.info('User preferences do not exist!')
        self.add_section('topsconfig')
        for k,v in list(self.OPTIONS.items()):
            self.set('DEFAULT', k, v)
        logger.info('Created new user preferences file with default values')

    def write(self):
        ''' override ConfigParser.write() method '''

        ConfigParser.write(self, open(self.upref, 'w'))

    def getdict(self):
        ''' get config file values '''

        current_options = {}
        for k in list(self.OPTIONS.keys()):
            current_options[k] = self.getvalue(k)

        return current_options

    def getvalue(self, option):
        ''' get specific config file value '''

        value = self.get('topsconfig', option)
        return value

    def setvalues(self, values):
        ''' set specific config file value '''

        for k, v in list(values.items()):
            self.set('topsconfig', str(k), str(v))

        self.write()
