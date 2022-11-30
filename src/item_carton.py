# item-carton.py
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

from .item_carta import ItemCarta

class ItemCarton(Gtk.Box):


    def buscar_carta(self, id):
        for index, carta in enumerate(self.cartas):
                if id == carta.carton_id():
                    self.cartas[index].mostrar_vista_inactiva()
                    self.cartas_obtenidas = self.cartas_obtenidas + 1
                    self.grid_footer.set_label(f'Cartas  {self.cartas_obtenidas}/16')

                    if self.cartas_obtenidas == 16:
                        self.get_style_context().add_class('carton-ganador')
                        self.btn_cantar_carta.set_sensitive(False)
                    break


    def obtener_imagen_carta(self, id):
        for carta in self.imagenes_cartas:
            if carta[0] == id:
                return carta[1]


    def __init__(self, jugador, imagenes_cartas, btn_cantar_carta):
        super().__init__(orientation= Gtk.Orientation.VERTICAL, spacing= 10)
        self.imagenes_cartas = imagenes_cartas
        self.btn_cantar_carta = btn_cantar_carta
        self.cartas_obtenidas = 0
        self.cartas = []
        self.get_style_context().add_class('card')


        self.nombre_jugador = Gtk.Label(label=jugador.nombre)
        self.nombre_jugador.set_margin_top(10)
        self.nombre_jugador.get_style_context().add_class('caption-heading')

        self.grid = Gtk.Grid()
        self.grid.set_margin_end(10)
        self.grid.set_margin_start(10)

        self.grid_footer = Gtk.Label(label='Cartas  0/16')
        self.grid_footer.set_margin_bottom(10)
        self.grid_footer.get_style_context().add_class('caption')

        self.append(self.nombre_jugador)
        self.append(self.grid)
        self.append(self.grid_footer)


        columna = 0
        fila = 0
        for carta in jugador.cartas:
            item_carta = ItemCarta(carta, self.obtener_imagen_carta(carta))
            self.grid.attach(item_carta, columna, fila, 1, 1)
            self.cartas.append(item_carta)

            columna = columna + 1

            if columna == 4:
                columna = 0
                fila = fila + 1
