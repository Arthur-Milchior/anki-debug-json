For some reason, anki use json for config. If json is not parseable, (which is often, since it may be hand-written), it generates an error-message. And Anki choose to hide it, considering instead that the config is empty !

This add-on correct this problem by showing json's error message, allowing the user to correct their JSON.