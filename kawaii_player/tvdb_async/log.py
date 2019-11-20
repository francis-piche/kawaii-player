"""
Copyright (C) 2018 kanishka-linux kanishka.linux@gmail.com

This file is part of tvdb-async.

tvdb-async is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

tvdb-async is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with tvdb-async.  If not, see <http://www.gnu.org/licenses/>.
"""

import logging


def log_function(name):
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("asyncio").setLevel(logging.WARNING)
    # fmt = '%(asctime)-15s::%(module)s:%(funcName)s: %(levelname)-7s - %(message)s'
    # formatter_ch = logging.Formatter(fmt)
    fmt = "%(lineno)s::%(levelname)s::%(module)s::%(funcName)s: %(message)s"
    formatter_ch = logging.Formatter(fmt)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter_ch)
    logger = logging.getLogger(name)
    logger.addHandler(ch)
    return logger
