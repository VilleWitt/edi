# -*- coding: utf-8 -*-
# Copyright (C) 2016 Matthias Luescher
#
# Authors:
#  Matthias Luescher
#
# This file is part of edi.
#
# edi is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# edi is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with edi.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os
from pwd import getpwnam
import socket


def print_error_and_exit(*args, **kwargs):
    print('Error: ', end="", file=sys.stderr)
    print(*args, file=sys.stderr, **kwargs)
    sys.exit(1)


def get_user():
    if 'SUDO_USER' in os.environ:
        return os.environ['SUDO_USER']
    else:
        return os.environ['USER']


def get_user_uid():
    return getpwnam(get_user()).pw_uid


def get_user_gid():
    return getpwnam(get_user()).pw_gid


def get_hostname():
    return socket.gethostname()


def which(executable):
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, _ = os.path.split(executable)
    if fpath:
        if is_exe(executable):
            return executable
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file_path = os.path.join(path, executable)
            if is_exe(exe_file_path):
                return exe_file_path

    return None


def require_executable(executable, hint):
    if which(executable) is None:
        print_error_and_exit(("Missing executable '{0}'.\n"
                              "Use '{1}' to install it.").format(executable,
                                                                 hint))