# 1) Classe Livro: Crie e teste uma classe que modele um livro:


`Atributos`: título, autor, total_paginas, pagina_atual
`Métodos`: avancar_pagina, voltar_pagina, ir_para_pagina, str

Obs: O método avancar_pagina deve incrementar a página atual em 1, e o
voltar_pagina deve diminuir em 1 (sem permitir valores negativos). O método ir_para_pagina recebe um número e define a página atual, respeitando os limites do livro

# decompondo o problema

```Bash
    Classe modelo livro
    |
    |____Representar o livro
    |        |____ titulo
    |        |____ autor
    |        |____ total_paginas
    |        |____ pagina_atual
    |
    |_____ representar o avanço da pagina
    |        |___ avancar_pagina()
    |
    |
    |_____ representar voltar  uma pagina
    |        |____ voltar_pagina()
    |    
    |______ representar indo na pagina
            |______ ir_para_pagina()
```

# abstraindo

a questão fala:

> atributos: título, autor, total_paginas, pagina_atual
> Métodos: avancar_pagina, voltar_pagina, ir_para_pagina, __str__

ja entregando os atributos e os metodos apenas isso deve ser representado pela classe para nossa representação do estado do Livro temos:

```bash
    class livro:
        titulo
        autor
        total_pagina
        pagina_atual

```
a quetão nao deixa explicito se o numero de paginas e fixo ou nao apenas que devemos assumir um numero de paginas que nao deve ser ultrapassado pelos metetodos bem como a pagina atual que se encontramos

>O `método avancar_pagina` deve incrementar a página atual em 1, e o
>`voltar_pagina deve diminuir` em 1 (**sem permitir valores negativos**). O método
>`ir_para_pagina` recebe **um número e define a página atual, respeitando os limites do livro**

## primeiro metodo: avancar_pagina()

> deve incrementar a página atual em 1

isso significa que ele pegara o valor de paginas atual e aumntara baseado no valor atual da pagina ou seja

```bash

    nova_pag = pagina_atual + avanco_pg

    #considerando a pagina atual sendo a 15 e o avanco de paginas em 5
    nova_pag = 15 + 5 -> nova_pag = 20 
```
podemos considerar que o ideal seria o numero do avanço nao superar o tamanho do livro 

```bash
     avancar_pagina()
     |
     |______ o numero da virada e maior que o numero de paginas?
            |
            |____ nao -> incrementar
            |_____ sim -> aviso
```

## segundo metodo: voltar_pagina()


> voltar_pagina deve diminuir em 1 (sem permitir valores negativos). 

isso significa que ele usa o numero atual de paginas apos ou depois da virada e decrementa uma quantidade especifica


```bash

    volta_pag = pagina_atual - voltando_pg

    #considerando a pagina atual sendo a 15 e o volta de paginas em 5
    volta_pag = 15 - 5 -> volta_pag = 10 
```

podemos considerar que a volta de paginas nao pode ultrapassar um valor do total de numero de paginas ir da pagina 15 pra -50 por exemplo


```bash
     voltar_pagina()
     |
     |______ o numero da virada e maior que o numero de paginas?
            |
            |____ nao -> decrementar
            |_____ sim -> aviso
```

## segundo metodo: ir_para_pagina()

>O método `ir_para_pagina recebe um número e define a página atual, respeitando os limites do livro.