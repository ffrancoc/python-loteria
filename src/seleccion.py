# seleccion.py
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

from .opcion_a import JuegoloteriaOpcionA
from .opcion_b import JuegoloteriaOpcionB

@Gtk.Template(resource_path='/com/github/ffrancoc/Loteria/gtk/seleccion.ui')
class JuegoloteriaVistaSeleccion(Gtk.Box):
    __gtype_name__ = 'JuegoloteriaVistaSeleccion'

    stack_menu = Gtk.Template.Child()
    btn_continuar = Gtk.Template.Child()
    btn_opcion_a = Gtk.Template.Child()


    @Gtk.Template.Callback()
    def on_volver(self, button):
        self.stack_menu.set_visible_child_name('opcion-a')
        self.window.cambiar_vista('vista-bienvenida')
        self.btn_opcion_a.set_active(True)
        self.opcion_a.resetear_campos()
        self.opcion_b.resetear_campos()
        self.habilitar_siguiente(True)


    @Gtk.Template.Callback()
    def on_seleccion_a(self, button):
        self.stack_menu.set_visible_child_name('opcion-a')


    @Gtk.Template.Callback()
    def on_seleccion_b(self, button):
        self.stack_menu.set_visible_child_name('opcion-b')


    @Gtk.Template.Callback()
    def on_continuar(self, button):
        opcion_seleccionada = self.window.opcion_seleccionada['opcion']
        numero_jugadores = len(self.window.opcion_seleccionada['jugadores'])

        if opcion_seleccionada and numero_jugadores == 2 or numero_jugadores == 3:
            self.window.cambiar_vista('vista-principal')
            self.window.vista_principal.inicializar_vista()

            self.stack_menu.set_visible_child_name('opcion-a')
            self.btn_opcion_a.set_active(True)
            self.opcion_a.resetear_campos()
            self.opcion_b.resetear_campos()


    @Gtk.Template.Callback()
    def on_cambiar_menu(self, stack, pspec):
        try:
            opcion = self.stack_menu.get_visible_child_name()
            if opcion == 'opcion-a':
                self.opcion_b.resetear_campos()
                jugador_a = self.opcion_a.obtener_valores_jugador_a()
                jugador_b = self.opcion_a.obtener_valores_jugador_b()
                self.window.modificar_opcion_seleccionada('a', [jugador_a, jugador_b])

            elif opcion == 'opcion-b':
                self.opcion_a.resetear_campos()
                jugador_a = self.opcion_b.obtener_valores_jugador_a()
                jugador_b = self.opcion_b.obtener_valores_jugador_b()
                jugador_c = self.opcion_b.obtener_valores_jugador_c()
                self.window.modificar_opcion_seleccionada('b', [jugador_a, jugador_b, jugador_c])
        except Exception:
            pass


    def set_default(self):
        jugador_a = self.opcion_a.obtener_valores_jugador_a()
        jugador_b = self.opcion_a.obtener_valores_jugador_b()
        self.window.modificar_opcion_seleccionada('a', [jugador_a, jugador_b])

    def habilitar_siguiente(self, estatus):
        self.btn_continuar.set_sensitive(estatus)


    def __init__(self, window):
        super().__init__()
        self.window = window

        self.opcion_a = JuegoloteriaOpcionA(self, window)
        self.stack_menu.add_named(self.opcion_a, 'opcion-a')

        self.opcion_b = JuegoloteriaOpcionB(self, window)
        self.stack_menu.add_named(self.opcion_b, 'opcion-b')


