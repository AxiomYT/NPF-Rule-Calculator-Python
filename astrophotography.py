# Imports
import sys
from configparser import *
from pathlib import Path
sys.path

# Variables, Arrays and Classes
pixelpitch = {
    "physical_width" : None,     # Millimetres
    "pixel_width" : None,        # Pixels
    "selector" : True
}

class calculation:
    def __init__(self): # , aperture, pixel_pitch, focal_length, shutter_speed):
        self.aperture = ""       # F/Stop No.
        self.pixel_pitch = ""    # Microns
        self.focal_length = ""   # Millimetres
        self.shutter_speed = ""  # Seconds

# Functions
def main():
    config = ConfigParser()
    configRead(config)
    setup(config)
    npfMethod()
    sys.exit()

def configRead(config):
    try:
        config.read(r"config.cfg")

        calculation.pixel_pitch = config.get('Pixel Pitch','PIXEL_PITCH')
        
        if (calculation.pixel_pitch != ""):
            pixelpitch["pixel_width"] = config.get('Pixel Pitch', 'PIXEL_WIDTH')
            pixelpitch["physical_width"] = config.get('Pixel Pitch', 'PHYSICAL_WIDTH')
            
            calculation.pixel_pitch = ( ( float(pixelpitch["physical_width"]) / ( float(pixelpitch["pixel_width"])) ) * 1000 )

        else:
            calculation.pixel_pitch = config.get('Pixel Pitch','PIXEL_PITCH')

    except:
        raise Exception('Could not open config.cfg, this could be down to a permissions error - \nOr even simply that the file does not exist, please check.\n\nhttps://github.com/AxiomYT/NPF-Rule-Calculator-Python\n\nFor further clarification.\n')

def setup(config):
    calculation.focal_length = (float(config.get('Specific Camera Variables', 'FOCAL_LENGTH')))
    #calculation.pixel_pitch = ( ( float(pixelpitch["physical_width"]) / ( float(pixelpitch["pixel_width"])) ) * 1000 )
    calculation.aperture = float(config.get('Specific Camera Variables', 'APERTURE')) 
    
    print('\033[95m' + "\nFocal Length  -", calculation.focal_length, "Millimetres" + '\033[0m')
    print('\033[94m' + "Pixel Pitch   -", round(calculation.pixel_pitch, 2), " Millimetres" + '\033[0m')   # Important that the output is rounded, 
    print('\033[96m' + "Aperture      -", calculation.aperture, "\n" + '\033[0m')

def npfMethod():
    # (((35 x aperture) + (30 x pixel pitch)) ÷ focal length ) = Shutter speed in seconds.
    calculation.shutter_speed = ( (( 35 * calculation.aperture ) + ( 30 * calculation.pixel_pitch )) / (float(calculation.focal_length)))
    print('\033[93m' + "Shutter Speed - ", (round(calculation.shutter_speed * 2.0) / 2.0), "Seconds\n" + '\033[0m')

# Main
if __name__ == "__main__":
    main()
