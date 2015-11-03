from distutils.core import setup, Extension
import numpy
include_dirs_numpy = [numpy.get_include()]

ext = Extension('libpyspg',
                 include_dirs = ['c/'] + include_dirs_numpy,
                 sources = ['libpyspg.c',
                            'c/cell.c',
                            'c/debug.c',
                            'c/hall_symbol.c',
                            'c/kpoint.c',
                            'c/lattice.c',
                            'c/mathfunc.c',
                            'c/pointgroup.c',
                            'c/primitive.c',
                            'c/refinement.c',
                            'c/site_symmetry.c',
                            'c/sitesym_database.c',
                            'c/spacegroup.c',
                            'c/spg_database.c',
                            'c/spglib.c',
                            'c/spin.c',
                            'c/symmetry.c',
                            'c/niggli.c',
                            'c/hall_symbol.c',
                            'c/tetrahedron_method.c'])

setup(name='libpyspg', version='1.8.2', description='This is libpyspg.', ext_modules=[ext])
