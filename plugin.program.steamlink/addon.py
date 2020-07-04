"""
Steamlink Launcher for Xbian Kodi
"""

import os
import xbmc
import xbmcgui
import xbmcaddon

from subprocess import check_call

class KodiAddon(object):
    def __init__(self):
        self._addon = xbmcaddon.Addon()
        self.path = self._addon.getAddonInfo('path').decode('utf-8')
    
    def run(self):
        check_call(['bash', self.path + '/usr/local/share/kodi/addons/steamlink/resources/lib/start.sh'])

def main():
    addon = KodiAddon()
    addon.run()

main()
