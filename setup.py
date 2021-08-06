import sys
from cx_Freeze import setup, Executable

# Dependências do projeto
build_exe_opitions = {'packages': ['os'], 'includes': ['tkinter', 'math', 're', 'typing']}

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name = 'PY_Calc',
    version = '1.0',
    description = 'Minha calculadora com tkinter',
    options = {'build_exe': build_exe_opitions},
    executables = {Executable('calculadora.py', base=base)}
)