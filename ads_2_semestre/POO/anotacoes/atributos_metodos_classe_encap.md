# Atributos e métodos de Classe  + Encapsulamento

### atributos da classe

sao diferentes dos atributos de instacia sendo definido dentro da propria classe fora dos metodos e nao precisam do uso de **self**

``` py
class Conta:
  taxa_geral = 0.03
  def __init__(self, titular: str, taxa: float):
    self.titular = titular
    self.taxa = taxa

```

aqui `taxa_geral` pertence a classe conta ja `titular` e `taxa` pertecem a instancia


### acessando

para acessar usamos `nomeclasse.atributo`:

```py
    print(Conta.taxa_geral) # Existe antes dos objetos existirem
    c = Conta("Ana", 0.05)

    print(c.taxa) # atributo da instância
    print(Conta.taxa_geral) # atributo da classe

```

pode ser acessado mesmo sem a existencia de um objeto,uma mudança nesse atributo mudara todos os objetos


### metodos

um metodo da classe nao depende de uma instancia para criar um metodo de classe basta usar `classmethod` antes de fazer a definição o primeiro parametro utilizado e `cls` fazendo uma referencia a propria classe e nao `self`

``` py

    class Usuario:
    total_usuarios = 0 # atributo da classe
    
    def __init__(self, nome, idade):
        self.nome = nome # Dado do objeto
        self.idade = idade # Dado do objeto
        Usuario.total_usuarios += 1
    
    @classmethod
    def criar_por_texto(cls, texto):
        nome, idade = texto.split(",")
        return cls(nome, int(idade))


```

para utilizar o metodos de classe e semelhante ao acesso de um atributo de classe `NomedDaClasse.metodo()` assim como os atibutos de classe eles podem ser usados antes mesmo de existir um objeto no caso acima foi utilizado um metodo da classe como construtor sao considerados metodos ferramentas da classe


# Encapsulamento

quando falamos em encapsulamento falamos em proteger detalhes internos de uma classe isso ajuda a evitar alterações indevidas no estado do objeto permitindo controlar como os dados são lidos e modificados

### exemplo de Encapsulamento

```py
  class Conta:
    def __init__(self):
    self.saldo = 0
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado")
        else:
            print("Saldo insuficiente")

```

o usuario esta chamando `sacar` sem saber os detalhes internos a classe define as regras e mantem a consistencia dos dados logicamente o exemplo acima nao seria o suficiente para impedir que façamos isso:

```py

    minha_conta=Conta(100)
    minha_conta.saldo=1000000000
    minha_conta.sacar(1000000000)

```

e nescessario melhorarmos o encapsulamento disso em pyhton o encapsulamento e feito com conveções de nomenclatura

``` py

    self.<atributo> # public
    self._<atributo> # protected
    self.__<atributo> # private

```

python nao trava o acesso a esses numeros:
- os atributos publicos podem ser acessado fora da classe
- atributos privados possume `__` antes de seu nome
- essa convensão ajuda a restringir o acesso a infromações internas


```py
  class Carro:
    def __init__(self, modelo, preco):
        self.modelo = modelo # público
        self.__preco = preco # privado

```

nesse exemplo `modelo` pode ser acessado diretamente ja `__preco` so pode ser acessado por metodos internos da propria classe e nao por funções ou qualquer outra interação fora dela


### acesso aos atributos privados

em python, um atributo privado e nomeado internamente pela linguagem

**exemplo**: `__preco` vira `__Carro__preco` chamamos isso de _name mangling_


```py

    class Carro:
        def __init__(self, modelo, preco):
            self.modelo = modelo
            self.__preco = preco
    
    c = Carro("Fiat",50000)
    print(c.modelo)
    print(c._Carro__preco)

```

- isso nao impede o acesso completamente, mas vai dificultar uso indevido
- objetivo e manter a logica de validação dentro da propria classe


# Getter e Setter

as variaveis nao publicas ainda precisam ser acessadas,`getter` lê o valor do atributo e `setter` altera o valor geralmente e feito com validação dessa forma a classe consegue controle sobre o que esta sendo alterado

```py
class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo
            
    def get_saldo(self): # lendo os valores do atributo
        return self.__saldo
    
    def set_saldo(self, valor): # altera com validção
        if valor >= 0:
            self.__saldo = valor

c = Conta(100)
print(c.get_saldo()) # pegando o valor atribuido ao objeto
c.set_saldo(250) # mudando o valor atribuido ao objeto
print(c.get_saldo())
c.set_saldo(-10)

    # 100
    # 250
    # saldo nao pode ser negativo

    
```

aqui vemos que a logica de validação se concentrar na propria classe


### a forma bizarra do python fazer isso
- `@property` para getter | `atributo.setter` para o setter


```py
class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo
        
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            raise ValueError("Saldo não pode ser negativo")
```

com isso nós podemos usar:

```py
c = Conta(100)
print(c.saldo)
c.saldo = 200
print(c.saldo)

# o acesso e igual para qualquer atributo,mais passando pelas regras de acesso
# o codigo fica  mais legivel e mantem a segurança da classe

```

encapsulamento ajuda com os seguintes pontos:

- proteger dados sensiveis
- evitar alterações sem regras
- deixar a classe mais organizada
- Facilita manutenção e evolução do software
- melhora a qualidade do codigo orientado a objetos
  
**exemplo de encapsulamento:**

```py

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
  
    @property
    def nome(self):
        return self.__nome
  
    @nome.setter
    def nome(self, novo_nome):
        if novo_nome.strip():
            self.__nome = novo_nome
        else:
            raise ValueError("Nome inválido")
  
    @property
    def idade(self):
        return self.__idade
  
    @idade.setter
    def idade(self, nova_idade):
        if nova_idade >= 0:
            self.__idade = nova_idade
        else:
            raise ValueError("Idade não pode ser negativa")
```


# Encapsulamento - metodos privados

e possivel tambem assim como atributos "esconder" metodos Dois colocando
`__` no nome do metodo sendo utilizado para metodos que nao podem ser acessados por codigos fora da definição da sua classe normalmente metodos privados sao "ajudantes" da propria classe


```py
class Recipient:
    def __init__(self, nome: str, email: str):
        self.__nome = nome
        if self.__check_email(email):
            self.__email = email
        else:
            raise ValueError("O email não é valido")

    def __check_email(self, email: str):
        # O endereço de email deve ter mais que 5 caracteres e ter . e @
        return len(email) > 5 and "." in email and "@" in email

r=Recipient("eduardo","eduardo.olivindo@ifce.edu.br")
r.__check_email("eduardo.olivindo@ifce.edu.br")
```
