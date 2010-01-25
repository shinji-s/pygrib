from distutils.core import setup, Extension
import numpy
import os

grib_api_dir = os.environ.get('GRIBAPI_DIR')
jasper_dir = os.environ.get('JASPER_DIR')
png_dir = os.environ.get('PNG_DIR')
zlib_dir = os.environ.get('ZLIB_DIR')
openjpeg_dir = os.environ.get('OPENJPEG_DIR')
libdirs=[]
incdirs=[numpy.get_include()]
libraries=['grib_api']
if grib_api_dir: 
    incdirs.append(os.path.join(grib_api_dir,'include'))
    libdirs.append(os.path.join(grib_api_dir,'lib'))
if openjpeg_dir: 
    incdirs.append(os.path.join(openjpeg_dir,'include'))
    libdirs.append(os.path.join(openjpeg_dir,'lib'))
    libraries.append("openjpeg")
if jasper_dir: 
    incdirs.append(os.path.join(jasper_dir,'include'))
    libdirs.append(os.path.join(jasper_dir,'lib'))
    libraries.append("jasper")
if png_dir: 
    incdirs.append(os.path.join(png_dir,'include'))
    libdirs.append(os.path.join(png_dir,'lib'))
    libraries.append("png")
if zlib_dir: 
    incdirs.append(os.path.join(zlib_dir,'include'))
    libdirs.append(os.path.join(zlib_dir,'lib'))
    libraries.append("z")

setup(name = "pygrib",
      version = "1.0",
      ext_modules = [Extension(
        "pygrib",
        ["pygrib.c"],
	include_dirs=incdirs,
        library_dirs=libdirs,
        libraries=libraries
      )])
