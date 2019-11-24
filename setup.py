"""
Copyright (C) 2017 kanishka-linux kanishka.linux@gmail.com

This file is part of kawaii-player.

kawaii-player is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

kawaii-player is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with kawaii-player.  If not, see <http://www.gnu.org/licenses/>.
"""


import os
import shutil
import platform
from setuptools import setup
from importlib.machinery import SourceFileLoader

auto_update = SourceFileLoader("auto_update.py", "kawaii_player/auto_update.py").load_module()
current_version = auto_update.get_version()
current_version_split = current_version.split('.')
version_field_1 = current_version_split[0]
version_field_2 = current_version_split[1]
version_field_3 = current_version_split[2].split('-')[0]

version = version_field_1 + '.' + version_field_2 + '.' + version_field_3
"""
 GNU/Linux users should install dependencies manually using their native
 package manager
"""

if os.name == 'posix':
    install_dependencies = []
else:
    install_dependencies = [
        'PyQt5', 'pycurl', 'bs4', 'Pillow', 'mutagen', 'lxml', 'youtube_dl',
        'certifi', 'PyQtWebEngine', 'PyOpenGL'
        ]
setup(
    name='kawaii-player', 
    version=version, 
    license='GPLv3', 
    author='kanishka-linux', 
    author_email='kanishka.linux@gmail.com', 
    url='https://github.com/kanishka-linux/kawaii-player', 
    long_description="README.md", 
    packages=[
        'kawaii_player', 'kawaii_player.Plugins', 'kawaii_player.widgets',
        'kawaii_player.hls_webengine', 'kawaii_player.hls_webkit',
        'kawaii_player.vinanti', 'kawaii_player.tvdb_async',
        ], 
    include_package_data=True, 
    entry_points={
        'gui_scripts':['kawaii-player = kawaii_player.kawaii_player:main'], 
        'console_scripts':['kawaii-player-console = kawaii_player.kawaii_player:main']
        }, 
    install_requires=install_dependencies, 
    description="A Audio/Video manager, multimedia player and portable media server", 
)
