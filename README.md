To run with pip installed:
1. activate the virtual environment and run
    "pip install -r requirements.txt"
2. Run pokemon_dml.py with
    "python pokemon_dmp.py"

To run with docker:
1. run the command
    "docker build -t <image name> ."
    "docker run <volume name>:/data <image name> python pokemon_dml.py"
    "docker run <volume name>:/data <image name> python <script>"

WIP: There is no main function yet. Pokemon sets are still being constructed.
Current sets progress: 86/292 Dragon, Ice, Fighting, Dark, Fire, Ghost