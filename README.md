# Show JSON error message when importing
## Rationale
For some reason, anki use json for config. If json is not parseable,
(which is often, since it may be hand-written), it generates an
error-message. And Anki choose to hide it, considering instead that
the config is empty !
## Usage
This add-on correct this problem by showing json's error message,
allowing the user to correct their JSON. It also print the past
config, so if you add-on destroy it, it is not lost.
## Internal
This add-on change AddonManager.addonMeta and
AddonManager.addonConfigDefaults in module aqt.addons. It does not
call the last version, and thus is incompatible with any other add-ons
modifying this.

## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Copyright   | Arthur Milchior <arthur@milchior.fr>
Based on    | Anki code by Damien Elmes <anki@ichi2.net>
License     | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
Source in   | https://github.com/Arthur-Milchior/anki-debug-json
Addon number| [2061352905](https://ankiweb.net/shared/info/2061352905)
Support me on| [![Ko-fi](https://ko-fi.com/img/Kofi_Logo_Blue.svg)](https://Ko-fi.com/arthurmilchior) or [![Patreon](http://www.milchior.fr/patreon.png)](https://www.patreon.com/bePatron?u=146206)
