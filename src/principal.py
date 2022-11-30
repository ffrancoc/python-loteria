# principal.py
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

import random
from gi.repository import Adw
from gi.repository import Gtk
from gi.repository import Gdk

from .item_carta import ItemCarta
from .item_carton import ItemCarton

@Gtk.Template(resource_path='/com/github/ffrancoc/Loteria/gtk/principal.ui')
class JuegoloteriaVistaPrincipal(Gtk.Box):
    __gtype_name__ = 'JuegoloteriaVistaPrincipal'

    btn_cantar_carta = Gtk.Template.Child()
    grid_cartas_titulo = Gtk.Template.Child()
    grid_cartas = Gtk.Template.Child()
    box_cartones = Gtk.Template.Child()


    @Gtk.Template.Callback()
    def on_volver(self, button):
        self.window.modificar_opcion_seleccionada(None, [])
        self.window.cambiar_vista('vista-seleccion')


    @Gtk.Template.Callback()
    def on_cantar_carta(self, button):
        cartas_disponibles = len(self.cartas)
        if cartas_disponibles > 0:
            numero = random.randint(1, cartas_disponibles) - 1
            item_carta = self.cartas[numero]
            item_carta.mostrar_vista_inactiva()
            self.cartas.remove(item_carta)

            self.cartas_restantes = self.cartas_restantes - 1
            self.grid_cartas_titulo.set_label(f'Cartas restantes {self.cartas_restantes}/54')

            for carton in self.cartones:
                carton.buscar_carta(item_carta.carton_id())


    def resetear_cartas(self):
        self.cartas_restantes = 54
        if len(self.cartas) > 0:
            for carta in self.cartas:
                self.grid_cartas.remove(carta)
            self.cartas.clear()


    def resetear_cartones(self):
        if len(self.cartones) > 0:
            for carton in self.cartones:
                self.box_cartones.remove(carton)
            self.cartones.clear()


    def inicializar_cartones(self):
        self.resetear_cartones()

        opcion = self.window.opcion_seleccionada['opcion']
        jugadores = self.window.opcion_seleccionada['jugadores']

        for jugador in jugadores:
            item_carton = ItemCarton(jugador, self.window.imagenes_cartas, self.btn_cantar_carta)
            self.box_cartones.append(item_carton)
            self.cartones.append(item_carton)


    def inicializar_vista(self):
        self.btn_cantar_carta.set_sensitive(True)
        self.resetear_cartas()

        columna = 0
        fila = 0
        for carta in self.window.imagenes_cartas:
            item_carta = ItemCarta(carta[0], carta[1])
            self.grid_cartas.attach(item_carta, columna, fila, 1, 1)
            self.cartas.append(item_carta)

            columna = columna + 1

            if columna == 18:
                columna = 0
                fila = fila + 1

        self.grid_cartas_titulo.set_label('Cartas restantes 54/54')
        self.inicializar_cartones()


    def __init__(self, window):
        super().__init__()
        self.window = window
        self.cartas_restantes = 0
        self.cartones = []
        self.cartas = []

        
