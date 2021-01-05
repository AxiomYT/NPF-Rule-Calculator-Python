# Imports
from configparser import *
from pathlib import Path

# Variables, Arrays and Classes
pixelpitch = {
    "physical_width" : None,     # Millimetres
    "pixel_width" : None         # Pixels
}

class calculation:
    def __init__(self, aperture, pixel_pitch, focal_length, shutter_speed):
        self.aperture = ""       # F/Stop No.
        self.pixel_pitch = ""    # Microns
        self.focal_length = ""   # Millimetres
        self.shutter_speed = ""  # Seconds

# Functions
def main():
   configRead()
   setup()

def configRead():
    try:
        config = ConfigParser()
        config.read(r"config.cfg")
        pixelpitch["pixel_width"] = config.get('Pixel Pitch', 'PIXEL_WIDTH')
        pixelpitch["physical_width"] = config.get('Pixel Pitch', 'PHYSICAL_WIDTH')

    except:
        raise Exception('Could not open config.cfg, this could be down to a permissions error - \nOr even simply that the file does not exist, please check.\n\nhttps://github.com/AxiomYT/NPF-Rule-Calculator-Python\n\nFor further clarification.\n')

def setup():
    calculation.aperture = ""
    calculation.pixel_pitch = ((float((pixelpitch["physical_width"])) / float((pixelpitch["pixel_width"]))) * 1000 )
    calculation.focal_length = ""
    calculation.shutter_speed = ''
    print("Pixel Pitch - ", calculation.pixel_pitch)

if __name__ == "__main__":
    main()