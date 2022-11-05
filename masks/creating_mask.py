import os
import fmask 
from fmask.cmdline import sentinel2Stacked

def main():
    safe_dir_20221101T183841 = "S2A_MSIL1C_20221101T151711_N0400_R125_T18NYN_20221101T183841.SAFE"
    out_img_file_20221101T183841= 'cloud_20221101T183841.img'
    fmask.config.setEqn17CloudProbThresh(0.4)
    sentinel2Stacked.mainRoutine(['--safedir', safe_dir_20221101T183841, '-o', out_img_file_20221101T183841])

    print('Completed running Fmask on SAFE file')


if __name__ == "__main__":
    main()