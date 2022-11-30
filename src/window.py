# window.py
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

from .bienvenida import JuegoloteriaVistaBienvenida
from .seleccion import JuegoloteriaVistaSeleccion
from .principal import JuegoloteriaVistaPrincipal

@Gtk.Template(resource_path='/com/github/ffrancoc/Loteria/gtk/window.ui')
class JuegoloteriaWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'JuegoloteriaWindow'

    stack = Gtk.Template.Child()


    def cambiar_vista(self, nombre_vista):
        if nombre_vista == 'vista-seleccion':
            self.vista_seleccion.set_default()
        self.stack.set_visible_child_name(nombre_vista)


    def modificar_opcion_seleccionada(self, opcion, jugadores):
        self.opcion_seleccionada['opcion'] = opcion
        self.opcion_seleccionada['jugadores'] = jugadores


    def do_close_request(self):
        return True


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.imagenes_cartones = {
            "carton1": "/com/github/ffrancoc/Loteria/assets/carton/carton1.png",
            "carton2": "/com/github/ffrancoc/Loteria/assets/carton/carton2.png",
            "carton3": "/com/github/ffrancoc/Loteria/assets/carton/carton3.png",
            "carton4": "/com/github/ffrancoc/Loteria/assets/carton/carton4.png",
            "carton5": "/com/github/ffrancoc/Loteria/assets/carton/carton5.png",
            "carton6": "/com/github/ffrancoc/Loteria/assets/carton/carton6.png",
            "carton7": "/com/github/ffrancoc/Loteria/assets/carton/carton7.png",
            "carton8": "/com/github/ffrancoc/Loteria/assets/carton/carton8.png",
            "carton9": "/com/github/ffrancoc/Loteria/assets/carton/carton9.png",
            "carton10": "/com/github/ffrancoc/Loteria/assets/carton/carton10.png",
        }

        self.imagenes_cartas = [
            ["carta1", "/com/github/ffrancoc/Loteria/assets/carta/carta1.png"],
            ["carta2", "/com/github/ffrancoc/Loteria/assets/carta/carta2.png"],
            ["carta3", "/com/github/ffrancoc/Loteria/assets/carta/carta3.png"],
            ["carta4", "/com/github/ffrancoc/Loteria/assets/carta/carta4.png"],
            ["carta5", "/com/github/ffrancoc/Loteria/assets/carta/carta5.png"],
            ["carta6", "/com/github/ffrancoc/Loteria/assets/carta/carta6.png"],
            ["carta7", "/com/github/ffrancoc/Loteria/assets/carta/carta7.png"],
            ["carta8", "/com/github/ffrancoc/Loteria/assets/carta/carta8.png"],
            ["carta9", "/com/github/ffrancoc/Loteria/assets/carta/carta9.png"],
            ["carta10", "/com/github/ffrancoc/Loteria/assets/carta/carta10.png"],
            ["carta11", "/com/github/ffrancoc/Loteria/assets/carta/carta11.png"],
            ["carta12", "/com/github/ffrancoc/Loteria/assets/carta/carta12.png"],
            ["carta13", "/com/github/ffrancoc/Loteria/assets/carta/carta13.png"],
            ["carta14", "/com/github/ffrancoc/Loteria/assets/carta/carta14.png"],
            ["carta15", "/com/github/ffrancoc/Loteria/assets/carta/carta15.png"],
            ["carta16", "/com/github/ffrancoc/Loteria/assets/carta/carta16.png"],
            ["carta17", "/com/github/ffrancoc/Loteria/assets/carta/carta17.png"],
            ["carta18", "/com/github/ffrancoc/Loteria/assets/carta/carta18.png"],
            ["carta19", "/com/github/ffrancoc/Loteria/assets/carta/carta19.png"],
            ["carta20", "/com/github/ffrancoc/Loteria/assets/carta/carta20.png"],
            ["carta21", "/com/github/ffrancoc/Loteria/assets/carta/carta21.png"],
            ["carta22", "/com/github/ffrancoc/Loteria/assets/carta/carta22.png"],
            ["carta23", "/com/github/ffrancoc/Loteria/assets/carta/carta23.png"],
            ["carta24", "/com/github/ffrancoc/Loteria/assets/carta/carta24.png"],
            ["carta25", "/com/github/ffrancoc/Loteria/assets/carta/carta25.png"],
            ["carta26", "/com/github/ffrancoc/Loteria/assets/carta/carta26.png"],
            ["carta27", "/com/github/ffrancoc/Loteria/assets/carta/carta27.png"],
            ["carta28", "/com/github/ffrancoc/Loteria/assets/carta/carta28.png"],
            ["carta29", "/com/github/ffrancoc/Loteria/assets/carta/carta29.png"],
            ["carta30", "/com/github/ffrancoc/Loteria/assets/carta/carta30.png"],
            ["carta31", "/com/github/ffrancoc/Loteria/assets/carta/carta31.png"],
            ["carta32", "/com/github/ffrancoc/Loteria/assets/carta/carta32.png"],
            ["carta33", "/com/github/ffrancoc/Loteria/assets/carta/carta33.png"],
            ["carta34", "/com/github/ffrancoc/Loteria/assets/carta/carta34.png"],
            ["carta35", "/com/github/ffrancoc/Loteria/assets/carta/carta35.png"],
            ["carta36", "/com/github/ffrancoc/Loteria/assets/carta/carta36.png"],
            ["carta37", "/com/github/ffrancoc/Loteria/assets/carta/carta37.png"],
            ["carta38", "/com/github/ffrancoc/Loteria/assets/carta/carta38.png"],
            ["carta39", "/com/github/ffrancoc/Loteria/assets/carta/carta39.png"],
            ["carta40", "/com/github/ffrancoc/Loteria/assets/carta/carta40.png"],
            ["carta41", "/com/github/ffrancoc/Loteria/assets/carta/carta41.png"],
            ["carta42", "/com/github/ffrancoc/Loteria/assets/carta/carta42.png"],
            ["carta43", "/com/github/ffrancoc/Loteria/assets/carta/carta43.png"],
            ["carta44", "/com/github/ffrancoc/Loteria/assets/carta/carta44.png"],
            ["carta45", "/com/github/ffrancoc/Loteria/assets/carta/carta45.png"],
            ["carta46", "/com/github/ffrancoc/Loteria/assets/carta/carta46.png"],
            ["carta47", "/com/github/ffrancoc/Loteria/assets/carta/carta47.png"],
            ["carta48", "/com/github/ffrancoc/Loteria/assets/carta/carta48.png"],
            ["carta49", "/com/github/ffrancoc/Loteria/assets/carta/carta49.png"],
            ["carta50", "/com/github/ffrancoc/Loteria/assets/carta/carta50.png"],
            ["carta51", "/com/github/ffrancoc/Loteria/assets/carta/carta51.png"],
            ["carta52", "/com/github/ffrancoc/Loteria/assets/carta/carta52.png"],
            ["carta53", "/com/github/ffrancoc/Loteria/assets/carta/carta53.png"],
            ["carta54", "/com/github/ffrancoc/Loteria/assets/carta/carta54.png"]
        ]

        self.carton_cartas = {
            "carton1": ["carta1", "carta2", "carta3", "carta4", "carta10", "carta11", "carta12", "carta13", "carta19", "carta20", "carta21", "carta22", "carta28", "carta29", "carta30", "carta31"],
            "carton2": ["carta6", "carta7", "carta8", "carta9", "carta15", "carta16", "carta17", "carta18", "carta24", "carta25", "carta26", "carta27", "carta33", "carta34", "carta35", "carta36"],
            "carton3": ["carta2", "carta3", "carta4", "carta5", "carta7", "carta8", "carta9", "carta10", "carta12", "carta13", "carta14", "carta15", "carta17", "carta18", "carta19", "carta20"],
            "carton4": ["carta43", "carta44", "carta45", "carta21", "carta52", "carta53", "carta54", "carta26", "carta7", "carta8", "carta9", "carta31", "carta16", "carta17", "carta18", "carta36"],
            "carton5": ["carta22", "carta23", "carta24", "carta25", "carta27", "carta28", "carta29", "carta30", "carta32", "carta33", "carta34", "carta35", "carta37", "carta38", "carta39", "carta40"],
            "carton6": ["carta21", "carta22", "carta23", "carta24", "carta30", "carta31", "carta32", "carta33", "carta39", "carta40", "carta41", "carta42", "carta48", "carta49", "carta50", "carta51"],
            "carton7": ["carta25", "carta26", "carta27", "carta41", "carta34", "carta35", "carta36", "carta46", "carta43", "carta44", "carta45", "carta51", "carta51", "carta53", "carta54", "carta32"],
            "carton8": ["carta42", "carta43", "carta44", "carta45", "carta47", "carta48", "carta49", "carta50", "carta52", "carta53", "carta54", "carta1", "carta40", "carta10", "carta19", "carta20"],
            "carton9": ["carta41", "carta42", "carta37", "carta38", "carta50", "carta51", "carta46", "carta47", "carta5", "carta6", "carta1", "carta2", "carta14", "carta15", "carta10", "carta11"],
            "carton10": ["carta39", "carta40", "carta19", "carta20", "carta48", "carta49", "carta28", "carta29", "carta3", "carta4", "carta37", "carta38", "carta12", "carta13", "carta46", "carta47"],
        }

        self.opcion_seleccionada = {
            'opcion': None,
            'jugadores': []
        }

        self.vista_bienvenida = JuegoloteriaVistaBienvenida(self)
        self.vista_seleccion = JuegoloteriaVistaSeleccion(self)
        self.vista_principal = JuegoloteriaVistaPrincipal(self)

        self.stack.add_named(self.vista_bienvenida, 'vista-bienvenida')
        self.stack.add_named(self.vista_seleccion, 'vista-seleccion')
        self.stack.add_named(self.vista_principal, 'vista-principal')
