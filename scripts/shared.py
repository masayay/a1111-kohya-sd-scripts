import argparse
import importlib
import os
import sys


def is_webui_extension():
    try:
        importlib.import_module("webui")
        return True
    except:
        return False


ROOT_DIR = (
    importlib.import_module("modules.scripts").basedir()
    if is_webui_extension()
    else os.path.dirname(os.path.dirname(__file__))
)

current_tab = None
loaded_tabs = []
help_title_map = {}

parser = argparse.ArgumentParser()
parser.add_argument("--enable-console-log", action="store_true")
cmd_opts, _ = parser.parse_known_args(sys.argv)
