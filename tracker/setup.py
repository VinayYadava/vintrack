from setuptools import setup, find_packages
import sys
import os
import shutil
setup(
    name = "tracker",
    version = "0.1.0",
    packages = find_packages(),
    include_package_data=True,
)
#lib_path = os.path.join(sys.prefix, "Lib" , "site_packages")
#print(lib_path)
#shutil.copy("../tracker" , lib_path , follow_symlinks=True)
