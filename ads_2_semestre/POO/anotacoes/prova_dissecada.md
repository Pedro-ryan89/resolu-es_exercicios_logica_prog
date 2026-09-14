# Sistema de controle de drone


## Questão Única — Sistema de Controle de um Drone

Crie uma classe para representar o sistema de controle de um drone. A classe deve atender aos seguintes requisitos:

### 1. Atributos e Inicialização — 1,0 ponto

A classe deve registrar a posição do drone nos eixos **X**, **Y** e sua **altura (Z)**.

Ao instanciar um novo objeto, o drone deve iniciar nas seguintes posições:

* X = 0
* Y = 0
* Altura = 0

### 2. Método `voar(deslocamento_z)` — 2,0 pontos

O método deve definir uma nova altura para o drone com base em um valor de deslocamento no eixo **Z**.

O método deve:

* Garantir que o valor recebido seja numérico (`int` ou `float`).
* Caso o valor não seja numérico, deve levantar uma exceção `TypeError` com a mensagem:

`"O deslocamento vertical deve ser um número!"`

* Impedir que a nova altura seja negativa ou superior a **120 metros**.
* Caso a nova altura esteja fora desse intervalo, deve levantar uma exceção `ValueError` com a mensagem:

`"A nova altura deve estar entre 0 e 120 metros!"`

### 3. Método `mover(deslocamento_x, deslocamento_y)` — 2,0 pontos

O método deve definir novas coordenadas para os eixos **X** e **Y**, utilizando os valores de deslocamento fornecidos.

O método deve:

* Garantir que os valores recebidos sejam numéricos (`int` ou `float`).
* Caso algum dos valores não seja numérico, deve levantar uma exceção `TypeError` com a mensagem:

`"O deslocamento horizontal deve ser um número!"`

* Garantir que o drone só possa se mover quando sua altura for maior que **0**.
* Caso o drone esteja no chão, deve levantar uma exceção `RuntimeError` com a mensagem:

`"Impossível mover, pois o drone está no chão!"`

### 4. Encapsulamento — 2,0 pontos

Todos os atributos da classe devem ser **não públicos**.

Os atributos devem ser definidos utilizando o conceito de encapsulamento e disponibilizados por meio de `@property`.

* Os métodos `getter` devem retornar os valores atuais dos atributos.
* Os métodos `setter` devem impedir que os atributos sejam alterados diretamente fora da definição da classe.

### 5. Método `__str__` — 0,5 ponto

A classe deve implementar o método `__str__`, que deve retornar uma representação do drone no seguinte formato:

`"Drone em (x, y) - Altura: z m"`

### 6. Testes — 0,5 ponto

Teste todas as funcionalidades implementadas na classe, incluindo:

* Criação e inicialização do objeto.
* Movimento vertical.
* Movimento horizontal.
* Alteração das coordenadas.
* Tentativas de inserir valores inválidos.
* Tentativa de ultrapassar a altura máxima ou utilizar altura negativa.
* Tentativa de movimentar o drone enquanto ele estiver no chão.
* Verificação do funcionamento das exceções e de seus respectivos tratamentos.

### 7. Menu Interativo — 2,0 pontos

Crie um **novo arquivo Python** que importe a classe desenvolvida.

Nesse arquivo:

1. Instancie um objeto da classe.
2. Crie um menu interativo para o usuário.
3. O menu deve permitir as seguintes opções:

   * **Voar**
   * **Mover**
   * **Sair**
4. O menu deve permanecer em execução em um **laço contínuo** até que o usuário escolha a opção **Sair**.
5. Utilize blocos `try...except` para tratar as possíveis exceções e impedir que o programa seja encerrado quando o usuário fornecer informações incorretas.





 ## decompondo o problema
```bash
    Sistema de drone
    |
    |______ Representar o Drone
    |       |_____ altura
    |       |_____ posicao x
    |       |_____ posicao y
    |
    |______ Controlar Voo
    |        |___ voar()
    |
    |______ controlar movimento
    |        |__ mover()
    |
    |_____ Encapsular Atributos
    |        |___ properties
    |
    |_____ Representar objeto
    |        | ___str()__
    |
    |_____ testar
    |       |___ exceções
    |
    |____ interface
            |___ menu
```

# abstraindo

A questão fala:

> "crie uma classe para representar o sistema de controle de um drone"

nao precisamos representar mais que isso ou seja nao preciso saber do gps,marca,numero de serie,helixces,camera,bataria etc isso sao informações irrelevantes no momento 

abstração consiste em representar aquilo que interessa ao problema enquanto se suprime detalhes irrelevantes

o que realmente aparece na questão sao as informações de velocidade,altura,posicao(x,y)
na nosssa abstração isso seria equivalente a:

```bash
    class Drone:
        x
        y
        altura

```

a questão tambem diz que "Ao instanciar um novo objeto,deve se iniciar em x=0,y=0 e altura=0" trduzindo a programação:

```bash
    quando criar drone:
        x = 0
        y = 0
        altura = 0

```
ou seja precisamos de um construtor.


### primeiro metodo: voar()


> Define uma nova altura com base em um valor de deslocamento no eixo z.


isso significa "altura atual + deslocamento_z" matematicamente ficamos com:

```bash
    nova_altura = altura_atual + deslocamento_z
```

uma parte importante do pensamentoa algoritmico: pegar uma descrição em linguagem natural e transformar ela em uma sequencia logica mas existem regras:

* deslocamento_z precisa ser int ou float
* se deslocamento_z nao for numero typerror
* nova altura precisa estsr entre 0 e 120
* se nova_altura < 0 OU nova altura > 120 valueError


```bash
    voar(z)
    |
    |______ z e numero?
    |       |_____ nao -> typeError
    |       
    |______ calcular nova altura
    |
    |_____ nova altura esta entre 0 e 120
            |____ nao -> value errro
            |____ sim -> atualizar altura
    
```
decomposição + logica + pensamento algoritmico

### seugundo metodo: mover()

o enunciado diz:

> mover(deslocamento_x, deslocamento_y)

primeiro precisamos ver o que seria deslocamento nesse caso temos a seguinte situação:

> se estamos em x=10 e y=20 e fazemos `mover(5,-3)`

a interpretação natural seria:

```bash
    novo_x = 10 + 5  = 15
    novo_y = 20 + (-3) = 17

    # portanto
    novo_x = x + deslocamento_x
    novo_Y = y + deslocamento_y

    #mas existe outra regra
    so pode mover se altura > 0

    #entao
    se altura == 0
        runtimeError

    mover(x, y)
    │
    ├── x é número?
    ├── y é número?
    │
    └── drone está voando?
        │
        ├── não → RuntimeError
        │
        └── sim
            │
            ├── novo_x = x + deslocamento_x
            └── novo_y = y + deslocamento_y
        
```
temos que considerar outra coisa interessante o estado, do drone começa com os valores zerados depois `voar(20)` e depois `mover(10, 5)`:

> x = 10
> y = 5
> altura = 20

# no final temos

```bash
   DRONE
    │
    ├── Estado
    │   ├── x
    │   ├── y
    │   └── altura
    │
    ├── voar(z)
    │   ├── validar z
    │   ├── calcular nova altura
    │   ├── validar limite
    │   └── atualizar altura
    │
    ├── mover(x, y)
    │   ├── validar x
    │   ├── validar y
    │   ├── verificar altura
    │   └── atualizar posição
    │
    ├── Encapsulamento
    │   └── properties
    │
    └── Interface
        └── menu
        
```

# interface

na questão diz que o usuario pode mover o drone e voar com o drone e consequentemente sair da interface do drone o programa precisa rodar continuamente apos a escolha e a inserção dos inputs da escolha selecionada ou seja em loop ate o usuario decidir a parada da mesma


```bash
    criar o drone

    opcao = input

    enquanto verdade:
        op 1
        op 2
        op 3

        escolha a op = opcao # ta vindo do input la de cima baseado na numeração de uma das 3 op

        match opcao:
            caso 1:
                tente
                    deslocamento_z = float(input(valor do deslocamento))
                    drone.voar(deslocamento_z) #metodo da classe
                se der erro:
                    captura o erro personalizado da classe
            caso 2
                tente:
                    mover # metodo da classe
                se der erro:
                    captura o erro da classe
            caos 3 # encerra o loop quebrando ele e retornando false
                encerra tudo

```

# sugestões de melhorias no metodo da resolução

- **estado** → o que o programa precisa lembrar e o que muda durante a execução.

- **Entradas** → o que o usuário/programa fornece, tipos esperados e valores inválidos.

- **Saídas** → o que o programa precisa produzir ou modificar.

- **Regras e restrições** → transformar o enunciado em condições objetivas.

- **Algoritmo → organizar** essas regras em uma sequência de passos.

- **Testes de estado** → verificar não só o resultado, mas se o estado ficou correto após operações e erros.

- **Revisão** → verificar se você consegue explicar sua própria solução.