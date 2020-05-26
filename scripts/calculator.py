
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


soma=1
subtracao=2
multiplicacao=3
divisao=4
print('resultado ', calc(2, 1, divisao))
