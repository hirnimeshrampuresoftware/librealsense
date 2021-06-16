import distutils.sysconfig as sysconfig
import io
import importlib.util
from skbuild import setup

spec = importlib.util.spec_from_file_location("module.name", "./wrappers/python/find_librs_version.py")
find_librs_version = importlib.util.module_from_spec(spec)
spec.loader.exec_module(find_librs_version)

package_name = "pyrealsense2"

__version__ = find_librs_version.get_version(librealsense_dir=".", output_dir=None)
print("version = ", __version__)

def load_readme():
     with io.open('./wrappers/python/README.rst', encoding="utf-8") as f:
        return f.read()

setup(
    name=package_name,
    version=__version__,
    author='Intel(R) RealSense(TM)',
    author_email='realsense@intel.com',
    url='https://github.com/IntelRealSense/librealsense',
    scripts=[
        'wrappers/python/examples/align-depth2color.py',
        'wrappers/python/examples/export_ply_example.py',
        'wrappers/python/examples/opencv_viewer_example.py',
        'wrappers/python/examples/python-rs400-advanced-mode-example.py',
        'wrappers/python/examples/python-tutorial-1-depth.py'
    ],
    license='Apache License, Version 2.0',
    description='Python Wrapper for Intel Realsense SDK 2.0.',
    long_description=load_readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Multimedia :: Video',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks'
        ],
    packages=[package_name],
    package_dir = {'': 'wrappers/python'},
    cmake_args=[
        '-DBUILD_PYTHON_BINDINGS:bool=true',
        '-DBUILD_EXAMPLES:bool=false',
        '-DBUILD_GRAPHICAL_EXAMPLES:bool=false',
        '-DBUILD_TOOLS:bool=false'
        # '-DPYTHON_INCLUDE_DIR=' + sysconfig.get_python_inc(),
        # '-DPYTHON_LIBRARY=' + sysconfig.get_config_var('LIBDIR')
    ],
    zip_safe=False,
)
