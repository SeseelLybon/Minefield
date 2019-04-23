
import json
import os
import logging


class ConfigManager:

    #Default values for the config_dict in case file system fails
    config_dict = {"window_size":(600,480)}

    @classmethod
    def createdefaultconfig(cls, corrupt:bool=False):
        logging.warning("Generating new config file")
        if corrupt:
            if os.path.exists("resources\\config.json"):
                os.remove("resources\\config.json")

        with open("resources\\config.json", "w") as f:
            f.write(json.dumps(cls.config_dict,
                               sort_keys=True, indent=4, separators=(',', ': ')))

    @classmethod
    def loadexistingconfig(cls, manualdefault=True):
        if os.path.exists("resources\\config.json"):
            with open("resources\\config.json", "r") as f:
                cls.config_dict = json.load(f)

        elif manualdefault:
            cls.createdefaultconfig()
