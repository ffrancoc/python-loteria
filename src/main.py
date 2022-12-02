# main.py
#
# Copyright 2022 Francisco Curin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Gdk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Gdk, Gio, Adw
from .window import JuegoloteriaWindow


class JuegoloteriaApplication(Adw.Application):
    """The main application singleton class."""

    def __init__(self):
        super().__init__(application_id='com.github.ffrancoc.Loteria',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = JuegoloteriaWindow(application=self)
            css_provider = Gtk.CssProvider()
            css_provider.load_from_resource('/com/github/ffrancoc/Loteria/css/style.css')
            style_context = win.get_style_context()
            style_context.add_provider_for_display(win.get_display(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
        win.present()


def main(version):
    """The application's entry point."""
    app = JuegoloteriaApplication()
    return app.run(sys.argv)
