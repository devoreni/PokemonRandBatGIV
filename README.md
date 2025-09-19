The project is now done. To run on windows: navigate to the dist folder and download the .exe
or refer below...

to run on another operating system:
1. pull the project
2. run pip install -r requirements.txt (after you have created a venv)
3. run whatever your operating system command is for the following pyinstaller windows command

pyinstaller --onefile --windowed --name "DNi Generation 4 Random Battles" --hidden-import=_cffi_backend --hidden-import=sklearn --hidden-import=sklearn.ensemble._forest --hidden-import=scipy.special._cdflib --hidden-import=sklearn.neighbors._typedefs --hidden-import=sklearn.neighbors._quad_tree --hidden-import=sklearn.tree._utils --hidden-import=numpy --hidden-import=scipy --hidden-import=pandas --add-data "assets;assets" --add-data "data;data" --add-data "pickle_model;." --add-data "dml_version.txt;." app.py