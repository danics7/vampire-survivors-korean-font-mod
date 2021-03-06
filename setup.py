from distutils.core import setup
import py2exe
setup(
    options={"py2exe": {
        "bundle_files": 1,
        'compressed': 1,
        'dll_excludes': ['tcl86t.dll', 'tk86t.dll', "mswsock.dll", "powrprof.dll"],
        'excludes': ['tkinter']
    }},
    zipfile=None,
    console=[{
            "script": "main.py",
            "icon_resources": [(1, "0.ico")],
            "dest_base": "Vampire Survivors 한글 폰트 모드",
            "name": "Vampire Survivors 한글 폰트 모드",
            "version": "1.0.0"
        }],
    version='1.0.0',
    name='Vampire Survivors 한글 폰트 모드',
    description='Vampire Survivors 한글 폰트 모드',
    author='danics'
)
