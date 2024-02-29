#Thomas Frentzel
'''To obtain the points related to this work, you must make a program, using the
Python, C++, C programming language capable of validating and executing programs written in
language proposed below by issuing a lexical analysis report, the classification as valid or
invalidates for each declaration of the language and the result of the program.
Language description
Identifiers: composed only of lowercase letters and numbers;
Special symbols: ?, ), (;
Operations: addition (+), subtraction (-), multiplication (*), division (/), sine (sin), cosine (cos),
exponentiation (exp), root (rot) according to the following examples:
(3 4 +) represents the sum of 3 and 4 and returns 7,000;
   (3.4 2.5 -) represents the subtraction between 3.6 and 2.5 and returns 1,100;
(2.5 3 *) is the product of 2.5 times 3 and returns 7,500;
(2.6 2 /) represents the division of 2.6 by 2 and returns 1,300;
    (sin 30) represents the sine of 30 degrees and returns 0.500;
    (cos 30) represents the cosine of 30 degrees and returns 0.866;
    (exp 3 2) represents 3 to the power of 2 and returns 9,000;
    (rot 81 2) represents the square root of 81 and returns 9000;
Note that all numbers are double precision reals and all results will be
truncated to the third place after the decimal point.
The special symbol will be used to pass the result of one line to the next line. Like this,
a file containing the following declarations:
(3 4 +)
(two ? *)
You should return 14 as an answer in addition to validating all lexemes and validating the
statements. For the example above, the output should be:
Line 1: lexemes: (, 3, 4, +,) all valid
Line 1: syntax: correct
Line 2: lexemes: (, 2, ?, ) all valid
Line 2: syntax: correct
In addition, we will be able to use identifiers and alignment. So to create a variable and
store a value we will use the sentence:
  
(test(2 3*))
In this example, the test variable was created and this variable will store the value 6,000.
A complete program could be written as:
  
(op1 15)
(op2 2)
(sin (op1 op2 *) )
(3 ? *)
In this example the result will be 1,500.
Important considerations: To test your program, you must upload three files
containing programs with 6 or more statements that use all the operations described with at least
least two nesting operations in each test file and with at least one variable in
each test file.
The tests must be able to indicate the behavior of your program if the code created
contains lexical or syntactic errors.
To carry out the lexical validation, you must simulate, in code, a state machine
finite and cannot use any regular expression.
To perform the syntactic validation you can use an LL1 parser or create your own.
claim validation code. '''

#importa as bibliotecas

import string
import math

alfa_valid = string.ascii_lowercase#

def get_file(file):
  return open(file).read()# abre o arquivo e retorna o conteudo

counterwhile = 0 
      
while counterwhile < 3:
  listapronta = []
  counterwhile = counterwhile + 1
  opcaocontagem = []
  file = get_file(f"teste{counterwhile}.txt").split("\n")
  validadorparenteses = False
  verificar = []#lista para verificar se o arquivo esta correto
  
  for i in file:
    verificar.append("1")
    a = i.split(" ")
    novo = []
    listcountleft = 0#contador de parenteses esquerdo
    for m in a:
      for n in m:
        x = "("
        xe = ")"
        if n == x:
          listcountleft = listcountleft + 1#conta os parenteses esquerdo
    listcountrigjt = 0
    validadornumerolistas = False
    for l in a:
      for t in l:
        for o in t:
          if o == '1' or o == '2' or o == '3' or o == '4' or o == '5' or o == '6' or o == '7' or o == '8' or o == '9':
            validadornumerolistas = True#verifica se tem numero na lista

        
    for m in a:#verifica se tem parenteses direito
      for n in m:
        x = "("
        xe = ")"
        if n == xe:
          listcountrigjt = listcountrigjt + 1#conta os parenteses direito
    if listcountrigjt == listcountleft:#verifica se o numero de parenteses esquerdo e igual ao numero de parenteses direito
      print(" ")
    else:
      print(" ")
      validadorparenteses = True
    for x in a:
      item = x
      for y in ['\n', '\t', '(', ')']:#remove os caracteres especiais
        item = item.replace(y, "")
      novo.append(item)
    a = novo
    removerInterrog = False
    for interrog in a:
      if interrog == '?':
        removerInterrog = True
    listaprontaB = []#lista para verificar se o arquivo esta correto


        
    a = [ x for x in a if x != '?' ]#remove o simbolo de interrogação
    
      
    bufferopcaocontagem = False#variavel para verificar se o arquivo esta correto
    verificaroperacao = False#verifica se tem operacao
    
    for q in a:
      if q == 'op1' or q == 'op2':
        verificaroperacao = True
        opcaocontagem.append(a[1])
        opcaocontagem = [ x for x in opcaocontagem if x != 'op1' ]
        opcaocontagem = [ x for x in opcaocontagem if x != 'op2' ]
        bufferopcaocontagem = True#verifica se tem a variavel op1 ou op2
     
    
    buffer = 0
    if verificaroperacao == True:#verifica se tem operacao
      for j in a:
        if j == '*' or j == '+' or j == '-' or j == '+':
          buffer = j
      if buffer == '*':#verifica se tem a operacao de multiplicação

        primtermo = float(opcaocontagem[0])
        segtermo = float(opcaocontagem[1])
        contaPronta = primtermo * segtermo# faz a conta
        print(
          '{} * {} ='.format(float(opcaocontagem[0]), float(opcaocontagem[1])),#imprime o resultado
          ' %.3f' % contaPronta)
        listapronta.append(contaPronta)#adiciona o resultado na lista

      if buffer == '+':
        primtermo = float(opcaocontagem[0])
        segtermo = float(opcaocontagem[1])
        contaPronta = primtermo + segtermo
        print(
          '{} + {} ='.format(float(opcaocontagem[0]), float(opcaocontagem[1])),
          ' %.3f' % contaPronta)
      if buffer == '-':
        primtermo = float(opcaocontagem[0])
        segtermo = float(opcaocontagem[1])
        contaPronta = primtermo - segtermo#
        print(
          '{} - {} ='.format(float(opcaocontagem[0]), float(opcaocontagem[1])),#
          ' %.3f' % contaPronta)
      if buffer == '/':

        primtermo = float(opcaocontagem[0])
        segtermo = float(opcaocontagem[1])
        contaPronta = primtermo / segtermo
        print(
          '{} / {} ='.format(float(opcaocontagem[0]), float(opcaocontagem[1])),
          ' %.3f' % contaPronta)
    
    print("linha {}".format(len(verificar)), "lexemas: ", f" {i} ")#imprime a linha e o lexema
        
    if removerInterrog == True:
      for interrog in a:
        if interrog == '*':
          a = [ x for x in a if x != '?' ]
          a = [ x for x in a if x != '*' ]#remove o simbolo de interrogação
          firsttermo = int(a[0])
          second = int(listapronta[0])
          print('{} / {} ='.format(float(opcaocontagem[0]), float(opcaocontagem[1])), ' %.3f' % (firsttermo * second))#
          
    if bufferopcaocontagem == True:
      a = [ x for x in a if x != 'op1' ]
      a = [ x for x in a if x != 'op2' ]
      a = [ x for x in a if x != '' ]#remove o simbolo de interrogação
      buffer = a[0]
      if buffer == '*':
        primtermo = float(opcaocontagem[0])
        segtermo = float(opcaocontagem[1])
        contaPronta = primtermo * segtermo
        print(
          '{} * {} ='.format(float(opcaocontagem[0]), float(opcaocontagem[1])),
          ' %.3f' % contaPronta)
      if buffer == '+':
        primtermo = float(opcaocontagem[0])
        segtermo = float(opcaocontagem[1])
        contaPronta = primtermo + segtermo
        print(
          '{} + {} ='.format(float(opcaocontagem[0]), float(opcaocontagem[1])),
          ' %.3f' % contaPronta)
      if buffer == '-':
        primtermo = float(opcaocontagem[0])
        segtermo = float(opcaocontagem[1])
        contaPronta = primtermo - segtermo
        print(
          '{} - {} ='.format(float(opcaocontagem[0]), float(opcaocontagem[1])),
          ' %.3f' % contaPronta)
      if buffer == '/':
        primtermo = float(opcaocontagem[0])
        segtermo = float(opcaocontagem[1])
        contaPronta = (primtermo / segtermo)
        print(
          '{} / {} ='.format(float(opcaocontagem[0]), float(opcaocontagem[1])),
          ' %.3f' % contaPronta)

      if buffer == '+':
        primtermo = float(opcaocontagem[0])
        segtermo = float(opcaocontagem[1])
        contaPronta = primtermo + segtermo
        print(
          '{} + {} ='.format(float(opcaocontagem[0]), float(opcaocontagem[1])),
          ' %.3f' % contaPronta)
      if buffer == '-':
        primtermo = float(opcaocontagem[0])
        segtermo = float(opcaocontagem[1])
        contaPronta = primtermo - segtermo
        print(
          '{} - {} ='.format(float(opcaocontagem[0]), float(opcaocontagem[1])),
          ' %.3f' % contaPronta)
      if buffer == '/':

        primtermo = float(opcaocontagem[0])
        segtermo = float(opcaocontagem[1])
        contaPronta = (primtermo / segtermo)
        print(
          '{} / {} ='.format(float(opcaocontagem[0]), float(opcaocontagem[1])),
          ' %.3f' % contaPronta)#imprime o resultado
        
    if len(a) == 2 and a[0] == 'sin':#verifica se o lexema é sin
      angulo = int(a[1])
      seno = math.sin(math.radians(angulo))
      print("seno de {} é {}".format(angulo, seno))
      print("linha {}".format(len(verificar)), "sintaxe: valido ")


      
    elif len(a) == 2 and a[0] == 'cos':#verifica se o lexema é cos
      angulo = int(a[1])
      seno = math.cos(math.radians(angulo))
      print("cosseno de {} é {}".format(angulo, seno))
    elif len(a) == 3 and a[0] == 'exp':
      denominador = int(a[1])
      elevador = int(a[2])
      print(a[1], "elevado a", a[2], "é", denominador**elevador)
    elif len(a) == 3 and a[0] == 'rot':
      raiz = math.sqrt(int(a[1]))
      print("a raiz quadrada é", raiz)#imprime o resultado

    
    elif len(a) > 3 and verificaroperacao == False:#verifica se o lexema é uma operação
      listNovo = []
      for g in a:
        elemento = g
        a = list(string.ascii_lowercase)#cria uma lista com todas as letras do alfabeto
        for p in a:
          elemento = elemento.replace(p, "")
        listNovo.append(elemento)
    
      for x in listNovo.copy():
          if x == '':
              listNovo.remove(x)
      validadorparenteses = False
      contagemdelistas = []#conta quantas listas tem
      for i in listNovo:
        contagemdelistas.append(i)
      if contagemdelistas[2] == '+':
        primtermo = float(contagemdelistas[0])
        segtermo = float(contagemdelistas[1])
        print(
          '{} + {} ='.format(float(contagemdelistas[0]), float(contagemdelistas[1])),
          ' %.3f' % (primtermo + segtermo))
    
      if contagemdelistas[2] == '-':
        primtermo = float(contagemdelistas[0])
        segtermo = float(contagemdelistas[1])
        print(
          '{} - {} ='.format(float(contagemdelistas[0]), float(contagemdelistas[1])),
          ' %.3f' % (primtermo - segtermo))
      if contagemdelistas[2] == '*':
        
        primtermo = float(contagemdelistas[0])
        segtermo = float(contagemdelistas[1])
        print(
          '{} * {} ='.format(float(contagemdelistas[0]), float(contagemdelistas[1])),
          ' %.3f' % (primtermo * segtermo))
      if contagemdelistas[2] == '/':
        
        primtermo = float(contagemdelistas[0])
        segtermo = float(contagemdelistas[1])
        print(
          '{} / {} ='.format(float(contagemdelistas[0]), float(contagemdelistas[1])),
          ' %.3f' % (primtermo / segtermo))
        
  
    if len(a) > 2 and verificaroperacao == False:#verifica se o lexema é uma operação
      
      contagemdelistas = []
      for i in a:
        contagemdelistas.append(i)
      if contagemdelistas[2] == '+':
        primtermo = float(contagemdelistas[0])
        segtermo = float(contagemdelistas[1])
        print(
          '{} + {} ='.format(float(contagemdelistas[0]), float(contagemdelistas[1])),
          ' %.3f' % (primtermo + segtermo))
    
      if contagemdelistas[2] == '-':
        primtermo = float(contagemdelistas[0])
        segtermo = float(contagemdelistas[1])
        print(
          '{} - {} ='.format(float(contagemdelistas[0]), float(contagemdelistas[1])),
          ' %.3f' % (primtermo - segtermo))
      if contagemdelistas[2] == '*':
        primtermo = float(contagemdelistas[0])
        segtermo = float(contagemdelistas[1])
        print(
          '{} * {} ='.format(float(contagemdelistas[0]), float(contagemdelistas[1])),
          ' %.3f' % (primtermo * segtermo))
      if contagemdelistas[2] == '/':
    
        primtermo = float(contagemdelistas[0])
        segtermo = float(contagemdelistas[1])
        print(
          '{} / {} ='.format(float(contagemdelistas[0]), float(contagemdelistas[1])),#
          ' %.3f' % (primtermo / segtermo))
    if validadorparenteses == True:
      print("linha {}".format(len(verificar)), "sintaxe: invalido")
      validadorparenteses = False
    else:
      if validadornumerolistas == True:
        print("linha {}".format(len(verificar)), "sintaxe: valido")#imprime se a linha é valida ou não
    if validadornumerolistas == False:
      print("linha {}".format(len(verificar)), "sintaxe: invalido")
