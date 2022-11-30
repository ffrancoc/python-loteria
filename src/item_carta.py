# item-carta.py
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
from gi.repository import GdkPixbuf

class ItemCarta(Gtk.Stack):


    def mostrar_vista_activa(self):
        self.set_visible_child_name('vista-activa')


    def mostrar_vista_inactiva(self):
        self.set_visible_child_name('vista-inactiva')


    def crear_vista(self, imagen):
        pixbuf = GdkPixbuf.Pixbuf.new_from_resource_at_scale(imagen, 100, 60, True)
        vista = Gtk.Picture.new_for_pixbuf(pixbuf)
        vista.set_content_fit(True)
        vista.set_can_shrink(True)

        return vista


    def carton_id(self):
        return self.id


    def __init__(self, id, imagen):
        super().__init__()
        self.id = id

        self.vista_activa = self.crear_vista(imagen)

        self.vista_inactiva = self.crear_vista(imagen)
        self.vista_inactiva.get_style_context().add_class('cover')

        self.add_named(self.vista_activa, 'vista-activa')
        self.add_named(self.vista_inactiva, 'vista-inactiva')
        self.set_transition_type(Gtk.StackTransitionType.ROTATE_LEFT_RIGHT)
        
