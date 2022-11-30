# opcion_a.py
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

from .jugador import Jugador

@Gtk.Template(resource_path='/com/github/ffrancoc/Loteria/gtk/opcion-a.ui')
class JuegoloteriaOpcionA(Gtk.Box):
    __gtype_name__ = 'JuegoloteriaOpcionA'

    box_jugador_a = Gtk.Template.Child()
    nombre_jugador_a = Gtk.Template.Child()
    combo_jugador_a = Gtk.Template.Child()
    vista_carton_a = Gtk.Template.Child()

    box_jugador_b = Gtk.Template.Child()
    nombre_jugador_b = Gtk.Template.Child()
    combo_jugador_b = Gtk.Template.Child()
    vista_carton_b = Gtk.Template.Child()


    @Gtk.Template.Callback()
    def on_cambio_nombre_jugador_a(self, entry):
        jugador_a = self.obtener_valores_jugador_a()
        jugador_b = self.obtener_valores_jugador_b()

        # condicion_a = len(jugador_a.nombre) == 0 or len(jugador_b.nombre) == 0
        condicion_a = len(jugador_a.nombre) > 0 and len(jugador_b.nombre) > 0
        condicion_b = jugador_a.nombre == jugador_b.nombre
        condicion_c = jugador_a.carton == jugador_b.carton

        if not condicion_a:
            self.vista_seleccion.habilitar_siguiente(False)
            self.box_jugador_a.get_style_context().add_class('invalido')
            self.window.modificar_opcion_seleccionada(None, [])

        if condicion_a and condicion_b:
            self.vista_seleccion.habilitar_siguiente(False)
            self.box_jugador_a.get_style_context().add_class('invalido')
            self.window.modificar_opcion_seleccionada(None, [])

        if condicion_a and not condicion_b and not condicion_c:
            self.vista_seleccion.habilitar_siguiente(True)
            self.box_jugador_a.get_style_context().remove_class('invalido')

            if self.box_jugador_b.get_style_context().has_class('invalido'):
                self.box_jugador_b.get_style_context().remove_class('invalido')

            self.window.modificar_opcion_seleccionada('a', [jugador_a, jugador_b])

        if condicion_a and not condicion_b and condicion_c:
            self.vista_seleccion.habilitar_siguiente(False)
            self.box_jugador_a.get_style_context().add_class('invalido')
            self.window.modificar_opcion_seleccionada(None, [])


    @Gtk.Template.Callback()
    def on_seleccionar_carton_a(self, combo):
        jugador_a = self.obtener_valores_jugador_a()
        jugador_b = self.obtener_valores_jugador_b()

        if jugador_a.carton != jugador_b.carton and len(jugador_a.nombre) > 0 and len(jugador_b.nombre) > 0 and jugador_a.nombre != jugador_b.nombre:
            self.vista_seleccion.habilitar_siguiente(True)
            self.box_jugador_a.get_style_context().remove_class('invalido')

            if self.box_jugador_b.get_style_context().has_class('invalido'):
                self.box_jugador_b.get_style_context().remove_class('invalido')

            self.window.modificar_opcion_seleccionada('a', [jugador_a, jugador_b])

        else:
            self.vista_seleccion.habilitar_siguiente(False)
            self.box_jugador_a.get_style_context().add_class('invalido')
            self.window.modificar_opcion_seleccionada(None, [])

        self.vista_carton_a.set_resource(self.window.imagenes_cartones.get(self.combo_jugador_a.get_active_id()))


    @Gtk.Template.Callback()
    def on_cambio_nombre_jugador_b(self, entry):
        jugador_a = self.obtener_valores_jugador_a()
        jugador_b = self.obtener_valores_jugador_b()

        if len(jugador_a.nombre) == 0 or len(jugador_b.nombre) == 0:
            self.vista_seleccion.habilitar_siguiente(False)
            self.box_jugador_b.get_style_context().add_class('invalido')
            self.window.modificar_opcion_seleccionada(None, [])

        if len(jugador_a.nombre) > 0 and len(jugador_b.nombre) > 0 and jugador_a.nombre == jugador_b.nombre:
            self.vista_seleccion.habilitar_siguiente(False)
            self.box_jugador_b.get_style_context().add_class('invalido')
            self.window.modificar_opcion_seleccionada(None, [])

        if len(jugador_a.nombre) > 0 and len(jugador_b.nombre) > 0 and jugador_a.nombre != jugador_b.nombre and jugador_a.carton != jugador_b.carton:
            self.vista_seleccion.habilitar_siguiente(True)
            self.box_jugador_b.get_style_context().remove_class('invalido')

            if self.box_jugador_a.get_style_context().has_class('invalido'):
                self.box_jugador_a.get_style_context().remove_class('invalido')

            self.window.modificar_opcion_seleccionada('a', [jugador_a, jugador_b])

        if len(jugador_a.nombre) > 0 and len(jugador_b.nombre) > 0 and jugador_a.nombre != jugador_b.nombre and jugador_a.carton == jugador_b.carton:
            self.vista_seleccion.habilitar_siguiente(False)
            self.box_jugador_b.get_style_context().add_class('invalido')
            self.window.modificar_opcion_seleccionada(None, [])


    @Gtk.Template.Callback()
    def on_seleccionar_carton_b(self, combo):
        jugador_a = self.obtener_valores_jugador_a()
        jugador_b = self.obtener_valores_jugador_b()

        if jugador_a.carton != jugador_b.carton and len(jugador_a.nombre) > 0 and len(jugador_b.nombre) > 0 and jugador_a.nombre != jugador_b.nombre:
            self.vista_seleccion.habilitar_siguiente(True)
            self.box_jugador_b.get_style_context().remove_class('invalido')

            if self.box_jugador_a.get_style_context().has_class('invalido'):
                self.box_jugador_a.get_style_context().remove_class('invalido')

            self.window.modificar_opcion_seleccionada('a', [jugador_a, jugador_b])

        else:
            self.vista_seleccion.habilitar_siguiente(False)
            self.box_jugador_b.get_style_context().add_class('invalido')
            self.window.modificar_opcion_seleccionada(None, [])


        self.vista_carton_b.set_resource(self.window.imagenes_cartones.get(self.combo_jugador_b.get_active_id()))


    def obtener_valores_jugador_a(self):
        nombre = self.nombre_jugador_a.get_text().lower()
        carton = self.combo_jugador_a.get_active_id()

        _carton = carton if carton else 'carton1'
        return Jugador(nombre=nombre, carton=_carton, cartas=self.window.carton_cartas[_carton])


    def obtener_valores_jugador_b(self):
        nombre = self.nombre_jugador_b.get_text().lower()
        carton = self.combo_jugador_b.get_active_id()

        _carton = carton if carton else 'carton2'
        return Jugador(nombre=nombre, carton=_carton, cartas=self.window.carton_cartas[_carton])


    def resetear_campos(self):
        self.nombre_jugador_a.set_text('Jugador A')
        self.nombre_jugador_b.set_text('Jugador B')
        self.combo_jugador_a.set_active(0)
        self.combo_jugador_b.set_active(1)
        self.vista_carton_a.set_resource('/com/github/ffrancoc/Loteria/assets/carton/carton1.png')
        self.vista_carton_b.set_resource('/com/github/ffrancoc/Loteria/assets/carton/carton2.png')
        self.vista_seleccion.habilitar_siguiente(True)


    def __init__(self, vista_seleccion, window):
        super().__init__()
        self.vista_seleccion = vista_seleccion
        self.window = window

        self.resetear_campos()
        
