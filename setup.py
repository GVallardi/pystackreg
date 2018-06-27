from distutils.core import setup, Extension
import numpy.distutils.misc_util

setup(
	name="pystackreg",
	#package_dir={'' : 'pystackreg'},
    ext_modules=[
		Extension("stackreg", [
			#"src/pymain.cpp",
			"src/PyStackReg.cpp",
			"src/TurboReg.cpp",
			"src/TurboRegMask.cpp",
			"src/TurboRegImage.cpp",
			"src/TurboRegTransform.cpp",
			"src/TurboRegPointHandler.cpp"])],
    include_dirs=['inc/'] + numpy.distutils.misc_util.get_numpy_include_dirs(),
) 
