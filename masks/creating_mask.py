import os
import fmask 
from fmask.cmdline import sentinel2Stacked

def main():

    # Checking wether or not there is a cloud masked images directory. 
    # If there is not, then it creates one.

    cloud_direc_name = "/hdd/1-PRINCIPAL-2022-1/1-PROYECTOS/PROYECTO_FREGATA_SPACE/Code/masks/Cloud_masking/"
    cloud_direc_ex = os.path.exists(cloud_direc_name)

    if cloud_direc_ex == True:
        None
    else:
        os.mkdir(cloud_direc_name)

    #Creates the paths to the .SAFE directories where the band images are located.
    SAFE_paths = "COPERNICUS/"
    SAFE_paths = [SAFE_paths+path for path in list(os.walk(SAFE_paths))[0][1]]
    SAFE_paths = [path+"/"+list(os.walk(path))[0][1][0] for path in SAFE_paths]

    #Creates the masks for every bands-image in each .SAFE directory, and 
    #saves them in the cloud-masked-images directory.
    for safe_path in SAFE_paths:
        out_img_file = 
        #fmask.config.FmaskConfig( fmask.config.FMASK_SENTINEL2).setEqn17CloudProbThresh(0.05)
        sentinel2Stacked.mainRoutine(['--safedir', safe_path, '-o', out_img_file])
    
    print('Completed running Fmask on SAFE file')
    


if __name__ == "__main__":
    main()