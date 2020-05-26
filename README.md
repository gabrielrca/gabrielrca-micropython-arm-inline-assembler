# micropython-arm-inline-assembler

This repository provides the Dockerfile for a docker container to run  the inline assembler of the Micropython for arm-based platforms (e.g. a Raspberry Pi).

`docker build -t gabrielrca/micropython-arm-inline-assembler .`

`docker run -v path/to/your/codes:/home -it --name my-mpython-image -d -p 80:80 gabrielrca/micropython-arm-inline-assembler`

`docker exec -it  my-mpython-image /mpython /home/main.py`
