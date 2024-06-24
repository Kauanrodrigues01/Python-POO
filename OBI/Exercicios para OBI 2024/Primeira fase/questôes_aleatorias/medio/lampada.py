def verificar_estado(interrupitor_apertado):
    lampada_A = False
    lampada_B = False

    for interrupitor in interrupitor_apertado:
        if interrupitor == '1':
            if lampada_A:
                lampada_A = False
            else:
                lampada_A = True
        elif interrupitor == '2':
            lampada_A = not lampada_A
            lampada_B = not lampada_B
    
    if lampada_A:
        print(1)
    else:
        print(0)
    if lampada_B:
        print(1)
    else:
        print(0)

num_vezes_apertou = int(input())
interrupitor_apertado = list(input().strip())
verificar_estado(interrupitor_apertado)