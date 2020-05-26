html = """<!DOCTYPE html>
<html>
    <head> <title>Calculadora Assembler</title> </head>
    <body> <h1>Calculadora Assembler</h1>
        %s
    </body>
</html>
"""

@micropython.asm_thumb
def calc(r0, r1, r2):
    cmp(r2, 1)          #compara pra ver se e soma
    it(eq)              #se for igual executa prox instrucao
    add(r0, r0, r1)     #soma
    cmp(r2, 2)          #compara pra ver se eh subtracao
    it(eq)              #se for igual executa prox instrucao
    sub(r0, r0, r1)     #subtrai
    cmp(r2, 3)          #compara pra ver se eh multiplicacao
    it(eq)              #se for igual executa prox instrucao
    mul(r0, r1)         #multiplica
    cmp(r2, 4)          #compara pra ver se eh multiplicacao
    it(eq)              #se for igual executa prox instrucao
    sdiv(r0, r0, r1)    #subtrai


import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
    response = html % calc(2, 1, 4)
    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send(response)
    cl.close()
