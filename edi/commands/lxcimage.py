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

from edi.lib.edicommand import EdiCommand


class LxcImage(EdiCommand):

    @classmethod
    def advertise(cls, subparsers):
        help_text = "upgrade a bootstrap image to a lxcimage"
        description_text = "Upgrade a bootstrap image to a lxcimage."
        parser = subparsers.add_parser(cls._get_command_name(),
                                       help=help_text,
                                       description=description_text)
        cls.require_config_file(parser)

    def run_cli(self, cli_args):
        self.run(cli_args.config_file)

    def run(self, config_file):
        self._setup_parser(config_file)

        self.require_sudo()
