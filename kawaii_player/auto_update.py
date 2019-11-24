import PySimpleGUI as sg
import base64
import requests
import re
import webbrowser
import argparse
import sys
import os


def check_update():
    # parser = argparse.ArgumentParser(description='arg parser')
    # parser.add_argument("--v", default=1, help="current user version")
    # args = parser.parse_args()
    # current_version = args.v

    if getattr(sys, 'frozen', False):
        BASEDIR, BASEFILE = os.path.split(os.path.abspath(sys.executable))
    else:
        BASEDIR, BASEFILE = os.path.split(os.path.abspath(__file__))
        print(BASEDIR, BASEFILE, os.getcwd())
        sys.path.insert(0, BASEDIR)
        RESOURCE_DIR = os.path.join(BASEDIR, 'version.txt')

    with open(RESOURCE_DIR, 'r') as fin:
        current_version = fin.read()

    sg.change_look_and_feel('DarkBlue1')

    layout = [[sg.Text('An update is available, do you want to go to the download page?')],
              [sg.Button('Yes'), sg.Button('No')]]

    cmd = 'echo current user version is: ' + str(current_version)
    url = 'https://api.github.com/repos/francis-piche/kawaii-player/contents/kawaii_player/resources/version_number'
    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        req = req.json()  # the response is a JSON
        content = base64.b64decode(req['content']).decode('utf-8')
        matchObj = re.search("(\d+\.)(\d+\.)(\d)", content)
        version = matchObj.group()
        if(version == current_version):
            print('version is up to date')
        else:
            print('update available')
            window = sg.Window('Kawaii-player updater', layout)
            event, values = window.read()
            print(event)
            if(event == 'Yes'):
                webbrowser.open_new_tab('https://github.com/kanishka-linux/kawaii-player/blob/master/README.md#dependencies-and-installation')
                window.close()
                sys.exit()
            else: 
                window.close()
    else:
        print('Kawii-updater Error: Unable to verify current version from github')
