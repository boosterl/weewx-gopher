# Copyright 2022 Bram Oosterlynck

from setup import ExtensionInstaller

def loader():
    return GopherInstaller()

class GopherInstaller(ExtensionInstaller):
    def __init__(self):
        super(GopherInstaller, self).__init__(
            version="0.1",
            name='gopher',
            description='A skin which outputs Gopher menus.',
            author="Bram Oosterlynck",
            author_email="bram.oosterlynck@gmail.com",
            config={
                'StdReport': {
                    'gopher': {
                        'skin':'gopher',
                        'HTML_ROOT':'/srv/gopher'}}},
            files=[('skins/gopher',
                    ['skins/gopher/gophermap.tmpl',
                     'skins/gopher/week.tmpl',
                     'skins/gopher/skin.conf'])
                   ]
            )
