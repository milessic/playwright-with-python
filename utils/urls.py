from utils.config_manager import config_manager

class Environments:
    test = "bieda.it"
    prod = "byst.re"

class Urls:
    try:
        homepage = "https://mjportfolio.{}".format(getattr(Environments, config_manager.environment))
    except AttributeError as e:
        raise AttributeError(f"Either Environments or ConfigManager doens't contain given attribute: '{e}'")


