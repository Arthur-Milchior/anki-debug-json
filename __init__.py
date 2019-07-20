# -*- coding: utf-8 -*-
# Copyright: Arthur Milchior <arthur@milchior.fr>
# Based on anki code by Damien Elmes <anki@ichi2.net>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Source in https://github.com/Arthur-Milchior/anki-debug-json
# Addon number 2061352905

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
            t = f.read()
            try:
                return json.loads(t)
            except Exception as e:
                print(
                    f"Here is a JSON error in default config of addon {dir}:", file=sys.stderr)
                print(str(e), file=sys.stderr)
                print(
                    f"\n\n===================\n\nCopy and save past config to be sure that it is not overwritten by accident. Past config was {t}", file=sys.stderr)
                return dict()
    except:
        return None


def addonMeta(self, dir):
    path = self._addonMetaPath(dir)
    try:
        with open(path, encoding="utf8") as f:
            t = f.read()
            try:
                return json.loads(t)
            except Exception as e:
                print(
                    f"Here is a JSON error in current config of addon {dir}:", file=sys.stderr)
                print(str(e), file=sys.stderr)
                print(
                    f"\n\n===================\n\nCopy and save past config to be sure that it is not overwritten by accident. Past config was {t}", file=sys.stderr)
                return dict()
    except:
        return dict()


AddonManager.addonMeta = addonMeta
AddonManager.addonConfigDefaults = addonConfigDefaults
