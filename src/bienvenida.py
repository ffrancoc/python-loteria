# bienvenida.py
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

from gi.repository import Adw
from gi.repository import Gtk
from gi.repository import Gdk

@Gtk.Template(resource_path='/com/github/ffrancoc/Loteria/gtk/bienvenida.ui')
class JuegoloteriaVistaBienvenida(Gtk.Box):
    __gtype_name__ = 'JuegoloteriaVistaBienvenida'

    status_page = Gtk.Template.Child()

    @Gtk.Template.Callback()
    def on_cerrar_aplicacion(self, button):
        self.window.destroy()

    @Gtk.Template.Callback()
    def on_iniciar_juego(self, button):
        self.window.cambiar_vista('vista-seleccion')

    def __init__(self, window):
        super().__init__()
        self.window = window

        self.status_page.set_paintable(Gdk.Texture.new_from_resource('/com/github/ffrancoc/Loteria/assets/logo.svg'))
