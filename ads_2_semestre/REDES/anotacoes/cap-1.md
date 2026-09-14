# borda da internet

- hosts: clientes e servidores
- servidores geralemente ficam em centros de dados
- redes de acesso e meios fisicos
    - enlace e cabeados e nao cabeados

o nucleo da internet e composta por roteadores interconectados feita de uma
"rede de redes"

os sistemas finais sao conectados atraves de redes de acesso:
- residencias
- institucionais(escola,empresas)
- redes de acessos moveis(Wi-fi, 4/5G)


## Host

a função principal do host e recever mensagens do aplicativo divir em pacotes com um comprimento de L bits,transmitir o pacote para a rede com uma taxa de transmissão R (tambem conhecida com largura da banda do link)

``` bash

    atraso de transmissão   =  tempo nescessario para =  L(bits)/R(bits/s)
    do pacote

```


## links
- `bit`: propraga-se entre os pares de transmissor/receptor
- `link fisico`: o que se encontra entre o transmissor e o receptor
- `meios guiados`:
    - os sinais se propagama em meios solidos: cobre,fibra,cabo oxial
- `meios nao guiados`:
    - sinais se propragam livremente: radio
- `par traçando(TP)`:
    - dois fios de cobre isolados: cat 5: Ethernet de 100mbps, 1Gbps , Cat 6: Ethernet de 10gbps
- `Cabo coaxial`:
    - dois condutores cocêntricos de cobre
    - bidirecional
    - Banda larga:
        - varios canais de frequencia no cabo
        - centenas de Mbps por canal
- `Cabo de fibra optica`:
    - fibra de vidro/plastico que transporta pulsos de luz
        - cada puslo repesenta um bit
    - operação de velocidade alta
        - transmissão ponta a ponta de alta velocidade:
    - baixa taxa de erros:
        - repetidores espaçados entre si
        - imune a ruídos e eletromagnéticos
- `sinais de rádio sem fio`:
    - sinal que e transmitido em varias "bandas" do espectro eletromagnético
    - sem "fio" físico
    - transmissão, "half-duplex" (do emissor para o receptor)
    - efeitos do ambiente de propragação:
        - reflexão
        - obstrução por objetos
        - interferência/ruido
- `tipos de link de rádio`:
    - LAN sem fio (wi-fi)
        - 10 a 100 Mbps: dezenas de metros
    - de área ampla (por exemplo, celular 4/5g)
        - dezenas de Mbps (4g) em cerca em 10 Km
    - Bluetooth: substituição de cabos
        - distancias curtas, velocidades ilimitadas
    - micro-ondas terrestre
     - ponto a ponot; canais de 45 Mbps
    - satelite
        - até < 100mbps (starlink) no dowlink
        - atraso de ponta a ponta de 270ms (geoestacionario)


# nucleo da rede

o nucleo da rede e uma malha de roteadores interconectados
  - comutação de pacotes: os host dividem as mensagens em **pacotes**
    - a rede faz o encaminhamento dos pacotes para de um roteador ao outro atraves dos links no caminho da **origem ate o destino**


## comutação de pacotes

 a transmissão de pacotes pode levar L/R segundos para enviar um pacote de L bits para a uma taxa de R bps ou seja 10 kbits / 100 Mbps = 0,1 ms de atraso de tranmissao

 o armazenamento e o encaminhamento do pacote inteiro deve chega ao roteador antes que possa ser tranmitido no proximo link

### enfileiramento
 ocorre principalmente quadno o volume de trabalho chega mais rapido do que pode ser atendido


 se a taxa de recepção chegar a exceder a taxa de transmissão do link por algum tempo que seja os pacotes podem ficar na fila aguardando serem transmitidos pelo link de saida ou poder ser descartados se o buffer do roteador fica cheia

 ## alternatica á comutação de pacotes: comutação de circuitos
  
sao recurso de ponta a ponta alocados e reservados para uma "chamada" entre a origem e o destino e como se fosse uma rua interligando os dois feita para aquela transmissão

supondo que temos 4 circuitos de links e dedicamos o 1 e 2 circuitos, a chamada recebe o 2 circuito no link superior e o 1 circuito no link direto

- recursos dedicados: sem compartilhamento
    - o desempenho e semelhante ao de um circuito dedicado

o segmento do circuito fica ocioso se nao for utilizado por nemnhuma chamada nao tendo compartilhamento ele e commente usados em rede telefônias tradicionais

## comutação de circuitos: FDM e TDM

### multiplexação por divisão de frequencia (FDM)

frequêcia divididas em bandas de frequêcia (estreitas) cada chamada recebe sua propria banda e pode transmitir na taxa máxima dessa banda estreita

### Multiplexação por divisão de tempo (TDM)

tempo dividido em intervalos cada chamada recebe um ou mais intervalos periodicos e pode transmitir na taxa máxima da banda de frequnêcia (mais ampla) apenas durante seus intervalos de tempo


## comu de pacotes vs comu de cicuitos

quantos usuarios podem utilizar essa rede?:
  - comutação de circuitos: 10 usuarios
  - comutação de pacotes: com 35 usuarios, a probabilidade de mais de 10 estarem ativos ao mesmo tempo e menor que 0,04%


  # Estrutura da Internet

os host conectam á internet por meio dos provedores de internets conhecidos como (ISPs) os ISPs por sua vez tem que estar interconectados
    - para que quaisquer dois hosts possam enviar pacotes um para o outro
a rede de redes que temos e muito complexa a evolução foi devido a fatores economicos e politicas nacionais

## estruturando a Internet

conectar cada provedor diretamente não e escalavel por isso a solução encontrada foi a criação de ISPs globais onde os provedores de acesso, tanto clientes quanto fornecedores tem um acordo economico mas se for algo viavel economicamente então nascem mais de uma ISPs globais tambem temos concorrente globais que se conectam entre si criando uma porta de troca de trafego IXP(Internet Exchange Point) possibilitando surgirmento das redes regionais para conectar redes de acesso a provedores de internet e as redes de provedores de conteudo podem operar suas proprias redes levando os serviços e conteudo mais perto dos usuarios finais

 - ISPs comerciais de "nivel 1" com cobertura nacional e internacional
 - redes de provedores de conteudo: rede privada que conecta seus data centers á internet muitas vezes contornando ISPs regionais de nivel 1