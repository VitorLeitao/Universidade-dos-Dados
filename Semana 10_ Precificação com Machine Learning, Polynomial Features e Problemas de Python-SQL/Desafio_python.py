def ultima_pagina(String):
    c = '1'
    while True:
        #print(f'String: {String}, C: {c}')
        if len(String) == 0: # Caso parada positiva
            #print('Passou')
            print(int(c)-1)
            break
        elif String[0: len(c)] != c: # Caso parada negativa
            #print('NÃO Passou')
            print(int(c)-1)
            String = String[len(c):]
            break
        else: # Caso continua
            #print('continuando')
            String = String[len(c):]
            c = str(int(c) + 1)

ultima_pagina('1235678')
