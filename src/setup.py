from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
from Cython.Distutils import build_ext

class CustomBuildExtCommand(build_ext):
    """build_ext command for use when numpy headers are needed."""
    def run(self):

        # Import numpy here, only when headers are needed
        import numpy

        # Add numpy headers to include_dirs
        self.include_dirs.append(numpy.get_include())

        # Call original build_ext command
        build_ext.run(self)
        
sourcefiles  = ['sent2vec.pyx', 
                'fasttext.cc', 
                "args.cc", 
                "dictionary.cc", 
                "matrix.cc", 
                "qmatrix.cc", 
                "model.cc", 
                'real.cc', 
                'utils.cc', 
                'vector.cc', 
                'real.cc', 
                'productquantizer.cc']
compile_opts = ['-std=c++0x', '-Wno-cpp', '-pthread', '-Wno-sign-compare']
ext=[Extension('*',
            sourcefiles,
            extra_compile_args=compile_opts,
            language='c++',
            include_dirs=[])]

setup(
  name='sent2vec',
  cmdclass = {'build_ext': CustomBuildExtCommand},
  install_requires=['numpy'],
  ext_modules=cythonize(ext)
)


