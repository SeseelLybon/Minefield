
import json
import os
import logging


class ConfigManager:

    #Default values for the config_dict in case file system fails
    config_dict = {"window_size":(600,480), #Size of window in pixels
                   "Minedensity":0.17, #Inverse chance of mine being placed
                   "Minepenalty":-50, #Penalty for detonating mines
                   "Tilepenalty":-10 #Penalty for destroying tiles
                   }


    @classmethod
    def createdefaultconfig(cls, corrupt:bool=False):
        logging.warning("Generating new config file")
        if corrupt:
            if os.path.exists("./resources/config.json"):
                os.remove("./resources/config.json")
        
        with open(".\\resources\\config.json", "w") as f:
            f.write(json.dumps(cls.config_dict,
                               sort_keys=True, indent=2, separators=(',', ': ')))

    @classmethod
    def loadexistingconfig(cls, manualdefault=True):
        if os.path.exists("./resources/config.json"):
            with open("./resources/config.json", "r") as f:
                cls.config_dict = json.load(f)

        elif manualdefault:
            cls.createdefaultconfig()
