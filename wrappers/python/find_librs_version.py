import io
import re
import sys
import os

def get_version(librealsense_dir, output_dir=None, printOutput=False):
    librs_version = ''
    rs_h_path = os.path.join(librealsense_dir, 'include/librealsense2/rs.h')
    if printOutput:
        print("Extracting version from: ", rs_h_path)
    with io.open(rs_h_path, 'r') as f:
        file_content = f.read()
        major = re.search(r"#define\s*RS2_API_MAJOR_VERSION\s*(\d+)",file_content)
        if not major:
            raise Exception('No major number')
        librs_version += major.group(1)
        librs_version += '.'
        minor = re.search(r"#define\s*RS2_API_MINOR_VERSION\s*(\d+)",file_content)
        if not minor:
            raise Exception('No minor number')
        librs_version += minor.group(1)
        librs_version += '.'
        patch = re.search(r"#define\s*RS2_API_PATCH_VERSION\s*(\d+)",file_content)
        if not patch:
            raise Exception('No patch number')
        librs_version += patch.group(1)

        if printOutput:
            print("Librealsense Version: ", librs_version)
        if output_dir is not None:
            outfile = os.path.join(output_dir, '_version.py')
            print("Writing version to: ", outfile)
            with open(outfile, 'w') as f:
                f.write('__version__ = "{}"'.format(librs_version))
        return librs_version

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Error! Usage: find_librs_version.py <absolute_path_to_librealsense> <output_dir>")
        exit(1)
    get_version(sys.argv[1], sys.argv[2], write_file=True, printOutput=True)
