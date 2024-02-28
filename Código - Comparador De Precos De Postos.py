#/*******************************************************************************
#Autor: João Ruan Araujo de Jesus Silva
#Componente Curricular: Mi algoritmos
#Concluido em: 03/09/2023
#Linguagem de progamação: Python 3.11.5
#Sistema operacional usado na criação do código: Windows 11
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************/

consultas = 0
posto1menor = 0
posto2menor = 0
posto3menor = 0
litrosposto1 = 0
litrosposto2 = 0
litrosposto3 = 0
#Abaixo estão as variáveis que serão usadas para verificar se uma condicional foi cumprida dentro do while. O uso delas será para tratamento de erro. 
certogasolina1 = 0
certoetanol1 = 0
certodiesel1 = 0
certogasolina2 = 0
certoetanol2 = 0
certodiesel2 = 0
certogasolina3 = 0
certoetanol3 = 0
certodiesel3 = 0
certomenu = 0
certotipocombustivel = 0
certolitro = 0

#Aqui eu criei uma estrutura para verificar se o usuário irá colocar virgula ao invés de ponto, para separar casas decimais. Caso isso aconteça, minha estrutura transforma a virgula dele em ponto, para não quebrar o sistema.
#Além disso, coloquei um verificador de letras, caso o usuário digite letras ao invés de um número valido, a pergunta se repete até o usuário digitar corretamente.
posto1 = input('Qual é o nome do primeiro posto? ')
while certogasolina1 != 1:
    gasolina1verifica = input(f'Quanto custa o litro da gasolina no {posto1}? ')
    gasolina1verifica = gasolina1verifica.replace(',' , '.')
    gasnumeroverifica = gasolina1verifica.replace('.','')
    gasnumeroverifica.isdigit()
    if gasnumeroverifica.isdigit():
        gasolina1 = float(gasolina1verifica)
        certogasolina1 += 1
    else:
        print('Caracter inválido! Use apenas números')
while certoetanol1 != 1:
    etanol1verifica = input(f'Quanto custa o litro do etanol no {posto1}? ')
    etanol1verifica = etanol1verifica.replace(',' , '.')
    etanumeroverifica = etanol1verifica.replace('.','')
    etanumeroverifica.isdigit()
    if etanumeroverifica.isdigit():
        etanol1 = float(etanol1verifica)
        certoetanol1 += 1
    else:
        print('Caracter inválido! Use apenas números')
while certodiesel1 != 1:
    diesel1verifica = input(f'Quanto custa o litro do diesel no {posto1}? ')
    diesel1verifica = diesel1verifica.replace(',' , '.')
    dienumeroverifica = diesel1verifica.replace('.','')
    dienumeroverifica.isdigit()
    if dienumeroverifica.isdigit():
        diesel1 = float(diesel1verifica)
        certodiesel1 += 1
    else:
        print('Caracter inválido! Use apenas números')


posto2 = input('Qual o nome do segundo posto? ')
while certogasolina2 != 1:
    gasolina2verifica = input(f'Quanto custa o litro da gasolina no {posto2}? ')
    gasolina2verifica = gasolina2verifica.replace(',' , '.')
    gasnumeroverifica = gasolina2verifica.replace('.','')
    gasnumeroverifica.isdigit()
    if gasnumeroverifica.isdigit():
        gasolina2 = float(gasolina2verifica)
        certogasolina2 += 1
    else:
        print('Caracter inválido! Use apenas números')
while certoetanol2 != 1:
    etanol2verifica = input(f'Quanto custa o litro do etanol no {posto2}? ')
    etanol2verifica = etanol2verifica.replace(',' , '.')
    etanumeroverifica = etanol2verifica.replace('.','')
    etanumeroverifica.isdigit()
    if etanumeroverifica.isdigit():
        etanol2 = float(etanol2verifica)
        certoetanol2 += 1
    else:
        print('Caracter inválido! Use apenas números')
while certodiesel2 != 1:
    diesel2verifica = input(f'Quanto custa o litro do diesel no {posto2} ')
    diesel2verifica = diesel2verifica.replace(',' , '.')
    dienumeroverifica = diesel2verifica.replace('.','')
    dienumeroverifica.isdigit()
    if dienumeroverifica.isdigit():
        diesel2 = float(diesel2verifica)
        certodiesel2 += 1
    else:
        print('Caracter inválido! Use apenas números')


posto3 = input('Qual o nome do terceiro posto? ')
while certogasolina3 != 1:
    gasolina3verifica = input(f'Quanto custa o litro da gasolina no {posto3}? ')
    gasolina3verifica = gasolina3verifica.replace(',' , '.')
    gasnumeroverifica = gasolina3verifica.replace('.','')
    gasnumeroverifica.isdigit()
    if gasnumeroverifica.isdigit():
        gasolina3 = float(gasolina3verifica)
        certogasolina3 += 1
    else:
        print('Caracter inválido! Use apenas números')
while certoetanol3 != 1:
    etanol3verifica = input(f'Quanto custa o litro do etanol no {posto3}? ')
    etanol3verifica = etanol3verifica.replace(',' , '.')
    etanumeroverifica = etanol3verifica.replace('.','')
    etanumeroverifica.isdigit()
    if etanumeroverifica.isdigit():
        etanol3 = float(etanol3verifica)
        certoetanol3 += 1
    else:
        print('Caracter inválido! Use apenas números')
while certodiesel3 != 1:
    diesel3verifica = input(f'Quanto custa o litro do diesel no {posto3}? ')
    diesel3verifica = diesel3verifica.replace(',' , '.')
    dienumeroverifica = diesel3verifica.replace('.','')
    dienumeroverifica.isdigit()
    if dienumeroverifica.isdigit():
        diesel3 = float(diesel3verifica)
        certodiesel3 += 1
    else:
        print('Caracter inválido! Use apenas números')


#Aqui é verificado se foi digitado um número valido, um número não valido, ou letras. Ele continua repetindo a pergunta até ser digitado um número valido.
while certomenu != 1:
    menu = input('MENU: \nDigite 1 para selecionar o combustível que deseja, e ver em qual posto o seu preço está mais barato. \nDigite 2 para saber os preços de todos os postos. \nDigite 3 para sair do menu. ')
    if menu.isdigit():
        menu = int(menu)
        if menu >= 4 or menu == 0:
            print('Caracter inválido! Apenas números de 1 até 3')
        else:
            certomenu += 1
    else:
        print('Caracter inválido! Use apenas números inteiros de 1 até 3 ')
#Aqui entra o loop principal.
while menu != 3:  
    if menu == 1:
        consultas += 1
        certotipocombustivel = 0
        while certotipocombustivel != 1:
            tipo = input('Digite 1 para gasolina \nDigite 2 para etanol \nDigite 3 para diesel ')
            if tipo.isdigit():
                tipo = int(tipo)
                if tipo >= 4 or tipo == 0:
                    print('Caracter inválido! Apenas números de 1 até 3')
                else:
                    certotipocombustivel += 1
            else:
                print('Caracter inválido! Use apenas números inteiros de 1 até 3 ')
                #Aqui, criei o mesmo verificador do início do código. Para substituir a possível virgula por ponto, e para evitar o uso de letras quando for informar a quantidade de litros.
        certolitro = 0
        while certolitro != 1:
            litrosverifica = input('Quantos litros quer abastecer? ')
            litrosverifica = litrosverifica.replace(',' , '.')
            litrosnumeroverificar = litrosverifica.replace('.' , '')
            if litrosnumeroverificar.isdigit():
                litros = float(litrosverifica)
                certolitro += 1
            else:
                print('Caracter inválido! Use apenas números')

        if tipo == 1:
            
            if  gasolina3 > gasolina1 < gasolina2:
                posto1menor += 1
                litrosposto1 += litros
                print(f'O posto com a gasolina mais barata é o {posto1}, com o custo de R$ {gasolina1} por litro. \nColocando {litros} litros de gasolina, você irá gastar R$ {litros * gasolina1} no total. \nNo posto {posto1} você irá economizar: \nR$ {round((gasolina2 * litros) - (gasolina1 * litros), 2)} em relação ao posto {posto2}. \nR$ {round((gasolina3 * litros) - (gasolina1 * litros), 2)} em relação ao posto {posto3}.')
            if  gasolina3 > gasolina2 < gasolina1:
                posto2menor += 1 
                litrosposto2 += litros
                print(f'O posto com a gasolina mais barata é o {posto2}, com o custo de R$ {gasolina2} por litro. \nColocando {litros} litros de gasolina, você irá gastar R$ {litros * gasolina2} no total. \nNo posto {posto2} você irá economizar: \nR$ {round((gasolina1 * litros) - (gasolina2 * litros), 2)} em relação ao posto {posto1}. \nR$ {round((gasolina3 * litros) - (gasolina2 * litros), 2)} em relação ao posto {posto3}.')
            if  gasolina2 > gasolina3 < gasolina1:
                posto3menor += 1
                litrosposto3 += litros
                print(f'O posto com a gasolina mais barata é o {posto3}, com o custo de R$ {gasolina3} por litro. \nColocando {litros} litros de gasolina, você irá gastar R$ {litros * gasolina3} no total. \nNo posto {posto3} você irá economizar: \nR$ {round((gasolina1 * litros) - (gasolina3 * litros), 2)} em relação ao posto {posto1}. \nR$ {round((gasolina2 * litros) - (gasolina3 * litros), 2)} em relação ao posto {posto2}.')
                       
            if gasolina1 == gasolina2 and gasolina1 < gasolina3:
                posto1menor += 1
                litrosposto1 += litros
                posto2menor += 1 
                litrosposto2 += litros
                print(f'O posto com a gasolina mais barata é o posto {posto1} e o posto {posto2}, com o custo de R$ {gasolina1} por litro. \nColocando {litros} litros de gasolina, você irá gastar R$ {litros * gasolina1} no total. \nNo posto {posto1} ou {posto2} você irá economizar: \nR$ {round((gasolina3 * litros) - (gasolina1 * litros), 2)} em relação ao posto {posto3}.')
            if gasolina1 == gasolina3 and gasolina1 < gasolina2:
                posto1menor += 1
                litrosposto1 += litros
                posto3menor += 1
                litrosposto3 += litros
                print(f'O posto com a gasolina mais barata é o posto {posto1} e o posto {posto3}, com o custo de R$ {gasolina1} por litro. \nColocando {litros} litros de gasolina, você irá gastar R$ {litros * gasolina1} no total. \nNo posto {posto1} ou {posto3} você irá economizar: \nR$ {round((gasolina2 * litros) - (gasolina1 * litros), 2)} em relação ao posto {posto2}.')
            if gasolina2 == gasolina3 and gasolina2 < gasolina1:
                posto2menor += 1 
                litrosposto2 += litros
                posto3menor += 1
                litrosposto3 += litros
                print(f'O posto com a gasolina mais barata é o posto {posto2} e o posto {posto3}, com o custo de R$ {gasolina2} por litro. \nColocando {litros} litros de gasolina, você irá gastar R$ {litros * gasolina2} no total. \nNo posto {posto2} ou {posto3} você irá economizar: \nR$ {round((gasolina1 * litros) - (gasolina2 * litros), 2)} em relação ao posto {posto1}.')
            if gasolina1 == gasolina2 == gasolina3:
                #Como não há posto mais barato entre os 3, não atribuir nenhuma das variáveis contadora. Nem a que soma e acumula os litros quando posto é o mais barato, e nem a que conta quantas vezes o determinado posto foi o barato. O Mesmo padrão foi codificado quando os 3 postos têm o mesmo valor de etanol ou diesel. 
                print(f'Não há posto posto com a gasolina mais barata, pois em todos os postos o preço da gasolina é igual, com o custo de R$ {gasolina1} por litro. \nColocando {litros} litros de gasolina, você irá gastar R$ {litros * gasolina1} no total.')


        if tipo == 2:
            
            if etanol3 > etanol1 < etanol2:
                posto1menor += 1
                litrosposto1 += litros
                print(f'O posto com o etanol mais barato é o {posto1}, com o custo de R$ {etanol1} por litro. \nColocando {litros} litros de etanol, você irá gastar R$ {litros * etanol1} no total. \nNo posto {posto1} você irá economizar: \nR$ {round((etanol2 * litros) - (etanol1 * litros), 2)} em relação ao posto {posto2}. \nR$ {round((etanol3 * litros) - (etanol1 * litros), 2)} em relação ao posto {posto3}.')
            if etanol3 > etanol2 < etanol1:
                posto2menor += 1
                litrosposto2 += litros
                print(f'O posto com o etanol mais barato é o {posto2}, com o custo de R$ {etanol2} por litro. \nColocando {litros} litros de etanol, você irá gastar R$ {litros * etanol2} no total. \nNo posto {posto2} você irá economizar: \nR$ {round((etanol1 * litros) - (etanol2 * litros), 2)} em relação ao posto {posto1}. \nR$ {round((etanol3 * litros) - (etanol2 * litros), 2)} em relação ao posto {posto3}.')
            if etanol1 > etanol3 < etanol2:
                posto3menor += 1
                litrosposto3 += litros
                print(f'O posto com o etanol mais barato é o {posto3}, com o custo de R$ {etanol3} por litro. \nColocando {litros} litros de etanol, você irá gastar R$ {litros * etanol3} no total. \nNo posto {posto3} você irá economizar: \nR$ {round((etanol1 * litros) - (etanol3 * litros), 2)} em relação ao posto {posto1}. \nR$ {round((etanol2 * litros) - (etanol3 * litros), 2)} em relação ao posto {posto2}.')
           
            if etanol1 == etanol2 and etanol1 < etanol3:
                posto1menor += 1
                litrosposto1 += litros
                posto2menor += 1
                litrosposto2 += litros
                print(f'O posto com o etanol mais barato é o posto {posto1} e o posto {posto2}, com o custo de R$ {etanol1} por litro. \nColocando {litros} litros de etanol, você irá gastar R$ {litros * etanol1} no total. \nNo posto {posto1} ou {posto2} você irá economizar: \nR$ {round((etanol3 * litros) - (etanol1 * litros), 2)} em relação ao posto {posto3}.')
            if etanol1 == etanol3 and etanol1 < etanol2:
                posto1menor += 1
                litrosposto1 += litros
                posto3menor += 1
                litrosposto3 += litros
                print(f'O posto com o etanol mais barato é o posto {posto1} e o posto {posto3}, com o custo de R$ {etanol1} por litro. \nColocando {litros} litros de etanol, você irá gastar R$ {litros * etanol1} no total. \nNo posto {posto1} ou {posto3} você irá economizar: \nR$ {round((etanol2 * litros) - (etanol1 * litros), 2)} em relação ao posto {posto2}.')
            if etanol2 == etanol3 and etanol2 < etanol1:
                posto2menor += 1
                litrosposto2 += litros
                posto3menor += 1
                litrosposto3 += litros
                print(f'O posto com o etanol mais barato é o posto {posto2} e o posto {posto3}, com o custo de R$ {etanol2} por litro. \nColocando {litros} litros de etanol, você irá gastar R$ {litros * etanol2} no total. \nNo posto {posto2} ou {posto3} você irá economizar: \nR$ {round((etanol1 * litros) - (etanol2 * litros), 2)} em relação ao posto {posto1}.')
            if etanol1 == etanol2 == etanol3:
                print(f'Não há posto posto com o etanol mais barato, pois em todos os postos o preço do etanol é igual, com o custo de R$ {etanol1} por litro. \nColocando {litros} litros de etanol, você irá gastar R$ {litros * etanol1} no total.')


        if tipo == 3:
            
            if diesel3 > diesel1 < diesel2:
                posto1menor += 1
                litrosposto1 += litros
                print(f'O posto com o diesel mais barato é o {posto1}, com o custo de R$ {diesel1} por litro. \nColocando {litros} litros de diesel, você irá gastar R$ {litros * diesel1} no total. \nNo posto {posto1} você irá economizar: \nR$ {round((diesel2 * litros) - (diesel1 * litros), 2) } em relação ao posto {posto2}. \nR$ {round((diesel3 * litros) - (diesel1 * litros), 2) } em relação ao posto {posto3}.')
            if diesel3 > diesel2 < diesel1:
                posto2menor += 1
                litrosposto2 += litros
                print(f'O posto com o diesel mais barato é o {posto2}, com o custo de R$ {diesel2} por litro. \nColocando {litros} litros de diesel, você irá gastar R${litros * diesel2} no total. \nNo posto {posto2} você irá economizar: \nR$ {round((diesel1 * litros) - (diesel2 * litros), 2) } em relação ao posto {posto1}. \nR$ {round((diesel3 * litros) - (diesel2 * litros), 2) } em relação ao posto {posto3}.')
            if diesel1 > diesel3 < diesel2:
                posto3menor += 1
                litrosposto3 += litros
                print(f'O posto com o diesel mais barato é o {posto3}, com o custo de R$ {diesel3} por litro. \nColocando {litros} litros de diesel, você irá gastar R$ {litros * diesel3} no total. \nNo posto {posto3} você irá economizar: \nR$ {round((diesel1 * litros) - (diesel3 * litros), 2) } em relação ao posto {posto1}. \nR$ {round((diesel2 * litros) - (diesel3 * litros), 2) } em relação ao posto {posto2}.')
                       
            if diesel1 == diesel2 and diesel1 < diesel3:
                posto1menor += 1
                litrosposto1 += litros
                posto2menor += 1
                litrosposto2 += litros
                print(f'O posto com o diesel mais barato é o posto {posto1} e o posto {posto2}, com o custo de R$ {diesel1} por litro. \nColocando {litros} litros de diesel, você irá gastar R$ {litros * diesel1} no total. \nNo posto {posto1} ou {posto2} você irá economizar: \nR$ {round((diesel3 * litros) - (diesel1 * litros), 2)} em relação ao posto {posto3}.')
            if diesel1 == diesel3 and diesel1 < diesel2:
                posto1menor += 1
                litrosposto1 += litros
                posto3menor += 1
                litrosposto3 += litros
                print(f'O posto com o diesel mais barato é o posto {posto1} e o posto {posto3}, com o custo de R$ {diesel1} por litro. \nColocando {litros} litros de diesel, você irá gastar R$ {litros * diesel1} no total. \nNo posto {posto1} ou {posto3} você irá economizar: \nR$ {round((diesel2 * litros) - (diesel1 * litros), 2)} em relação ao posto {posto2}.')
            if diesel2 == diesel3 and diesel2 < diesel1:
                posto2menor += 1
                litrosposto2 += litros
                posto3menor += 1
                litrosposto3 += litros
                print(f'O posto com o diesel mais barato é o posto {posto2} e o posto {posto3}, com o custo de R$ {diesel2} por litro. \nColocando {litros} litros de diesel, você irá gastar R$ {litros * diesel2} no total. \nNo posto {posto2} ou {posto3} você irá economizar: \nR$ {round((diesel1 * litros) - (diesel2 * litros), 2)} em relação ao posto {posto1}.')
            if diesel1 == diesel2 == diesel3:
                print(f'Não há posto posto com o diesel mais barato, pois em todos os postos o preço do diesel é igual, com o custo de R$ {diesel1} por litro. \nColocando {litros} litros de diesel, você irá gastar R$ {litros * diesel1} no total.')

    if menu == 2:
        consultas += 1
        print(f'Dados do posto {posto1}: \n-Litro da gasolina R$ {gasolina1} \n-Litro do etanol R$ {etanol1}\n-Litro do diesel R$ {diesel1}')
        print(f'Dados do posto {posto2}: \n-Litro da gasolina R$ {gasolina2} \n-Litro do etanol R$ {etanol2}\n-Litro do diesel R$ {diesel2}')
        print(f'Dados do posto {posto3}: \n-Litro da gasolina R$ {gasolina3} \n-Litro do etanol R$ {etanol3}\n-Litro do diesel R$ {diesel3}')
   
    menu = input('MENU: \nDigite 1 para selecionar o combustível que deseja, e ver em qual posto o seu preço está mais barato. \nDigite 2 para saber os preços de todos os postos. \nDigite 3 para sair do menu. ')
    if menu.isdigit():
        menu = int(menu)
        if menu >= 4 or menu == 0:
            print('Caracter inválido! Apenas números de 1 até 3')
    else:
        print('Caracter inválido! Use apenas números inteiros de 1 até 3 ')

#Caso usuário digitasse no menu, 1 ( para ver o posto mais barato) ou 2 (Para ver a relação de dados de todos os postos), cada ação dessas conta como 1 consulta, aumentando +1 no contador de consultas.
print(f'Relatório final: \nForam realizadas {consultas} consultas \nO posto {posto1} teve o preço do combustível mais barato {posto1menor} vezes \nO posto {posto2} teve o preço do combustível mais barato {posto2menor} vezes \nO posto {posto3} teve o preço do combustível mais barato {posto3menor} vezes ')
#Para fazer a média na hora da divisão, o divisor não pode ser 0 no python, caso seja, acaba dando erro. Porém terá casos que quando o usuário rodar o programa, determinado posto poderá nunca ser o mais barato/consultado (ou seja, divisor = 0), sendo a variável divisor = 0, não poderá ser feita a divisão 0/0. Todavia a solução que encontrei, foi transformar o divisor em 1, caso ele seja 0 no fim do programa, logo será a divisão 0/1 = 0, e com isso será possível fazer o cálculo da média, sem afetar o resultado correto. Pois 0/0 resulta em 0.0, e 0/1 também resulta em 0.0. 
if posto1menor == 0:
    posto1menor = 1
if posto2menor == 0:
    posto2menor = 1
if posto3menor == 0:
    posto3menor = 1
print(f'A média de litros por consultas no {posto1} é {round(litrosposto1/posto1menor, 2)} \nA média de litros por consultas no {posto2} é {round(litrosposto2/posto2menor,2)} \nA média de litros por consultas no {posto3} é {round(litrosposto3/posto3menor,2)}')

if gasolina3 < gasolina1 > gasolina2:
    print (f'O posto {posto1} possui o litro de gasolina mais cara, com o custo de R$ {gasolina1}' )
if gasolina3 < gasolina2 > gasolina1:
    print (f'O posto {posto2} possui o litro de gasolina mais cara, com o custo de R$ {gasolina2}' )
if gasolina1 < gasolina3 > gasolina2:
    print (f'O posto {posto3} possui o litro de gasolina mais cara, com o custo de R$ {gasolina3}' )
if gasolina1 == gasolina2 and gasolina1 > gasolina3: 
    print (f'Os postos {posto1} e {posto2} possui o litro de gasolina mais cara, com o custo de R$ {gasolina1}' )
if gasolina1 == gasolina3 and gasolina1 > gasolina2: 
    print (f'Os postos {posto1} e {posto3} possui o litro de gasolina mais cara, com o custo de R$ {gasolina1}' )
if gasolina3 == gasolina2 and gasolina2 > gasolina1: 
    print (f'Os postos {posto2} e {posto3} possui o litro de gasolina mais cara, com o custo de R$ {gasolina2}' )
if gasolina1 == gasolina2 == gasolina3: 
    print (f'Não há posto com a gasolina mais cara, pois todos tem o mesmo preço de R$ {gasolina1}' )

if gasolina3 > gasolina1 < gasolina2:
    print (f'O posto {posto1} possui o litro de gasolina mais barata, com o custo de R$ {gasolina1}' )
if gasolina3 > gasolina2 < gasolina1:
    print (f'O posto {posto2} possui o litro de gasolina mais barata, com o custo de R$ {gasolina2}' )
if gasolina1 > gasolina3 < gasolina2:
    print (f'O posto {posto3} possui o litro de gasolina mais barata, com o custo de R$ {gasolina3}' )
if gasolina1 == gasolina2 and gasolina1 < gasolina3: 
    print (f'Os postos {posto1} e {posto2} possui o litro de gasolina mais barata, com o custo de R$ {gasolina1}' )
if gasolina1 == gasolina3 and gasolina1 < gasolina2: 
    print (f'Os postos {posto1} e {posto3} possui o litro de gasolina mais barata, com o custo de R$ {gasolina1}' )
if gasolina3 == gasolina2 and gasolina2 < gasolina1: 
    print (f'Os postos {posto2} e {posto3} possui o litro de gasolina mais barata, com o custo de R$ {gasolina2}' )
if gasolina1 == gasolina2 == gasolina3: 
    print (f'Não há posto com a gasolina mais barata, pois todos tem o mesmo preço de R$ {gasolina1}' )


if etanol3 < etanol1 > etanol2:
    print(f'O posto {posto1} possui o litro de etanol mais caro, com o custo de R$ {etanol1}' )
if etanol3 < etanol2 > etanol1:
    print(f'O posto {posto2} possui o litro de etanol mais caro, com o custo de R$ {etanol2}' )
if etanol1 < etanol3 > etanol2:
    print(f'O posto {posto3} possui o litro de etanol mais caro, com o custo de R$ {etanol3}' )
if etanol1 == etanol2 and etanol1 > etanol3: 
    print (f'Os postos {posto1} e {posto2} possui o litro de etanol mais caro, com o custo de R$ {etanol1}' )
if etanol1 == etanol3 and etanol1 > etanol2: 
    print (f'Os postos {posto1} e {posto3} possui o litro de etanol mais caro, com o custo de R$ {etanol1}' )
if etanol3 == etanol2 and etanol2 > etanol1: 
    print (f'Os postos {posto2} e {posto3} possui o litro de etanol mais caro, com o custo de R$ {etanol2}' )
if etanol1 == etanol2 == etanol3: 
    print (f'Não há posto com o etanol mais caro, pois todos tem o mesmo preço de R$ {etanol1}' )

if etanol3 > etanol1 < etanol2:
    print(f'O posto {posto1} possui o litro de etanol mais barato, com o custo de R$ {etanol1}' )
if etanol3 > etanol2 < etanol1:
    print(f'O posto {posto2} possui o litro de etanol mais barato, com o custo de R$ {etanol2}' )
if etanol1 > etanol3 < etanol2:
    print(f'O posto {posto3} possui o litro de etanol mais barato, com o custo de R$ {etanol3}' )
if etanol1 == etanol2 and etanol1 < etanol3: 
    print (f'Os postos {posto1} e {posto2} possui o litro de etanol mais barato, com o custo de R$ {etanol1}' )
if etanol1 == etanol3 and etanol1 < etanol2: 
    print (f'Os postos {posto1} e {posto3} possui o litro de etanol mais barato, com o custo de R$ {etanol1}' )
if etanol3 == etanol2 and etanol2 < etanol1: 
    print (f'Os postos {posto2} e {posto3} possui o litro de etanol mais barato, com o custo de R$ {etanol2}' )
if etanol1 == etanol2 == etanol3: 
    print (f'Não há posto com o etanol mais barato, pois todos tem o mesmo preço de R$ {etanol1}' )


if diesel3 < diesel1 > diesel2:
    print(f'O posto {posto1} possui o litro de diesel mais caro, com o custo de R$ {diesel1}' )
if diesel3 < diesel2 > diesel1:
    print(f'O posto {posto2} possui o litro de diesel mais caro, com o custo de R$ {diesel2}' )
if diesel1 < diesel3 > diesel2:
    print(f'O posto {posto3} possui o litro de diesel mais caro, com o custo de R$ {diesel3}' )
if diesel1 == diesel2 and diesel1 > diesel3: 
    print (f'Os postos {posto1} e {posto2} possui o litro de diesel mais caro, com o custo de R$ {diesel1}' )
if diesel1 == diesel3 and diesel1 > diesel2: 
    print (f'Os postos {posto1} e {posto3} possui o litro de diesel mais caro, com o custo de R$ {diesel1}' )
if diesel3 == diesel2 and diesel2 > diesel1: 
    print (f'Os postos {posto2} e {posto3} possui o litro de diesel mais caro, com o custo de R$ {diesel2}' )
if diesel1 == diesel2 == diesel3: 
    print (f'Não há posto com o diesel mais caro, pois todos tem o mesmo preço de R$ {diesel1}' )

if diesel3 > diesel1 < diesel2:
    print(f'O posto {posto1} possui o litro de diesel mais barato, com o custo de R$ {diesel1}' )
if diesel3 > diesel2 < diesel1:
    print(f'O posto {posto2} possui o litro de diesel mais barato, com o custo de R$ {diesel2}' )
if diesel1 > diesel3 < diesel2:
    print(f'O posto {posto3} possui o litro de diesel mais barato, com o custo de R$ {diesel3}' )  
if diesel1 == diesel2 and diesel1 < diesel3: 
    print (f'Os postos {posto1} e {posto2} possui o litro de diesel mais barato, com o custo de R$ {diesel1}' )
if diesel1 == diesel3 and diesel1 < diesel2: 
    print (f'Os postos {posto1} e {posto3} possui o litro de diesel mais barato, com o custo de R$ {diesel1}' )
if diesel3 == diesel2 and diesel2 < diesel1: 
    print (f'Os postos {posto2} e {posto3} possui o litro de diesel mais barato, com o custo de R$ {diesel2}' )
if diesel1 == diesel2 == diesel3: 
    print (f'Não há posto com o diesel mais barato, pois todos tem o mesmo preço de R$ {diesel1}' )        
