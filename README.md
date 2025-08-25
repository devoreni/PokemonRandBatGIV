To run with pip installed:
1. activate the virtual environment and run
    "pip install -r requirements.txt"
2. Run pokemon_dml.py with
    "python pokemon_dmp.py"

To run with docker: DOCKER CURRENTLY BROKEN
1. run the command
    "docker build -t <image name> ."
    "docker run --rm -v pokedata:/data --name poke-builder poke python pokemon_dml.py"
    "docker run <volume name>:/data <image name> python app.py"

WIP: app.py is the main function and runs the gui. Pokemon sets are still being constructed.
Current sets progress: 133/292 
Dragon, Ice, Fighting, Dark, Fire, Ghost, Steel, Electric, Rock