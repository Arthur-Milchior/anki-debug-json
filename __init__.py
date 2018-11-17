import json
import os
import sys

from aqt.addons import AddonManager


def addonConfigDefaults(self, dir):
    """The (default) configuration of the addon whose
name/directory is dir.

    This file should be called config.json"""
    path = os.path.join(self.addonsFolder(dir), "config.json")
    try:
        with open(path, encoding="utf8") as f:
            try:
                return json.load(f)
            except Exception as e:
                print(f"Here is a JSON error in addon {dir}:", file=sys.stderr)
                print(str(e), file=sys.stderr)
                return dict()
    except:
        return None


def addonMeta(self, dir):
    path = self._addonMetaPath(dir)
    try:
        with open(path, encoding="utf8") as f:
            try:
                return json.load(f)
            except Exception as e:
                print(str(e), file=sys.stderr)
                return dict()
    except:
        return dict()


AddonManager.addonMeta = addonMeta
AddonManager.addonConfigDefaults = addonConfigDefaults
