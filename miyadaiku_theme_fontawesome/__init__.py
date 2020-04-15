import pkg_resources
from miyadaiku import config

FONTAWESOME_MIN = 'font-awesome.min.css'
FONTAWESOME = 'font-awesome.css'
DEST_PATH = '/static/fontawesome/css/'

def load_package(site):
    f = site.config.get('/', 'fontawesome_compressed')
    f = config.to_bool(f)
    fontawesome = FONTAWESOME_MIN if f else FONTAWESOME
    src_path = 'externals/css/'+fontawesome
    
    content = pkg_resources.resource_string(__name__, src_path)
    site.files.add_bytes("binary", DEST_PATH + fontawesome , content )
    site.config.add('/', {'fontawesome_path': DEST_PATH+fontawesome})

    site.add_template_module('fontawesome', 'miyadaiku_theme_fontawesome!macros.html')

