# Projeto Compiladores 2016-2
[![Build Status](https://travis-ci.com/djornada/interpretador-calculadora.svg?token=5JLBuaWZHaduxmfL3XDo&branch=master)](https://travis-ci.com/djornada/interpretador-calculadora)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000?style=flat-square)]()

Implemenetação da calculadora [bc](https://www.gnu.org/software/bc/manual/bc.html), disponível em sistemas Linux, com várias simplificações para tornar o projeto viável no prazo proposto.

Para o projeto de compiladores, as seguintes regras devem ser aplicadas:

- Identificadores, usados para nomes de funções, argumentos e variáveis seguem a regra de formação da linguagem Java;

- A calculadora trabalha apenas com os tipos numérico (double) e lógico (boolean), o tipo é inferido durante o processamento. Os valores numéricos são sempre apresentados com três casas decimais;

- Embora possam ser declaradas variáveis globais (a partir de um comando de atribuição), os argumentos e variáveis utilizadas em uma função são sempre locais a esta. Funções recursivas são permitidas o que exigirá um certo cuidado para utilização destes elementos;

- A calculadora contém três modos básicos de operação, a sintaxe específica de cada um pode ser encontrada na documentação, alterações são permitidas a critério do grupo, desde que explicadas no relatório entregue:

  - Imediato: A expressão é compilada (gera uma ASA) e executada imediatamente. **Exemplo: 2^3+5**. A expressão é avaliada e seu resultado mostrado na tela.
 
  - Atribuição: a expressão é compilada, executada, e armazenada associada ao identificador. **Exemplo: f = 2^b+5**
 
  - Declaração de função. A expressão é compilada e armazenada em uma tabela de funções para uso posterior. **Exemplo: define d (n) { return (2*n); }**
  
- Controle:
  - __help__ – mostra um pequeno auxílio ao uso da calculadora (conteúdo a critério do grupo)
  
  - __load__ "nome_arquivo", permite carregar em memória um conjunto de declarações (declarações de funções)
  
  - __save__ "nome_arquivo", grava o conteúdo atual da tabela de funções
  
  - __show__ "ident" – apresenta os dados armazenados na tabela de valores/funções associadas ao identificador "ident"
  
  - __show_all__ – apresenta todos os dados armazenados nas tabelas de valores/funções
  
- Operadores válidos, valendo as regras de precedência e associatividade da linguagem Java:
  
  - __Aritméticos:__ _+_, _-_, _*_, _/_, _^_ (potência, maior precedência e associativo à direita). Operandos devem ser numéricos e o resultado é numérico
  
  - __Relacionais:__ _>_, _>=_, _\<_, _<=_, _!=_. Operandos numéricos e o resultado lógico.
  
  - __Lógicos:__ _&&_, _||_, _!_. Operandos lógicos, resultado lógico
  
  - __Atribuição:__ _=_, _+=_, _*=_. Identificador do mesmo tipo do resultado da expressão.
  
  - __Condicional:__ _?:_. Expressão de teste lógica, outras duas do mesmo tipo.
  
  - __Sequencia:__ _,_ . Expressões são avaliadas sequencialmente e o resultado da lista é o resultado da última expressão avaliada.
  
- Comandos
 - Seleção (if)
 - Repetição (while e for)
 - Impressão (print)
- Definição de funções. 
 - __Atenção!__ A declaração e uso de funções é o grande diferencial da calculadora e então valerá 25% da nota final do trabalho!
