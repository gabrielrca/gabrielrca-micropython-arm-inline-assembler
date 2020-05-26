FROM debian
LABEL version="1.0" description="Micropython Docker for ARM" maintainer="Gabriel R. Caldas de Aquino<gcaldas08@gmail.com>"

WORKDIR /

RUN apt-get update && apt-get -y install build-essential libreadline-dev libffi-dev pkg-config python-setuptools python-dev git dh-autoreconf python3

WORKDIR /

RUN git clone https://github.com/micropython/micropython.git

WORKDIR /micropython/mpy-cross

RUN make

WORKDIR /micropython/ports/unix

RUN git submodule update --init

RUN make deplibs

RUN make CFLAGS_EXTRA='-DMICROPY_EMIT_INLINE_THUMB=1'

WORKDIR / 

RUN git clone https://github.com/micropython/micropython-lib.git

WORKDIR /micropython-lib

RUN make install

WORKDIR /micropython/ports/unix

RUN ln -s /micropython/ports/unix/micropython /mpython
