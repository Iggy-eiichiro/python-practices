import json # it is going to be useable as a dict
import logging

logging.basicConfig(
    filename=r"c:\Users\bro\OneDrive\デスクトップ\python Rikai\app log", level = logging.ERROR
)
def load_config(filename):

    try:
        with open(filename, "r") as file:# as file of file is chngeable.
            config = json.load(file)# only in this program, it is called "file" that is decided 

        if "name" not in config:# if there is no "name" inside
            logging.warning("Missing key: name")# Display it if there is no "name" inside
            print("Run:logging.warning")
            return None

        return config

    except FileNotFoundError:
        logging.error("Config file not found")
        print("Run:except FileNotFoundError")
        return None

    except json.JSONDecodeError:# it shows up when JSON is written incorrectly and python cannot be read as JSON
        logging.error("Invalid JSON")
        print("Run:except json.JSONDecodeError")
        return None


config = load_config("config.json")

if config is not None:# return dictionary = displayed config
    print(config)

# logging.error. specify and record the error message yourself
# logging.exception. error messae in except + record details of the exception that occured