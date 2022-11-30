pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'juegoloteria')
gnome = import('gnome')

blueprints = custom_target('blueprints',
  input: files(
    'gtk/help-overlay.blp',
    'gtk/window.blp',
    'gtk/bienvenida.blp',
    'gtk/seleccion.blp',
    'gtk/opcion-a.blp',
    'gtk/opcion-b.blp',
    'gtk/principal.blp',
  ),
  output: '.',
  command: [find_program('blueprint-compiler'), 'batch-compile', '@OUTPUT@', '@CURRENT_SOURCE_DIR@', '@INPUT@'],
)

gnome.compile_resources('juegoloteria',
  'juegoloteria.gresource.xml',
  dependencies: blueprints,
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'juegoloteria.in',
  output: 'juegoloteria',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

juegoloteria_sources = [
  '__init__.py',
  'main.py',
  'window.py',
  'bienvenida.py',
  'seleccion.py',
  'opcion_a.py',
  'opcion_b.py',
  'jugador.py',
  'principal.py',
  'item_carta.py',
  'item_carton.py',
]

install_data(juegoloteria_sources, install_dir: moduledir)
