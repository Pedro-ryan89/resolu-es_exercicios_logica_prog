
### Protocolos

regras que especificam o formato e a ordem das mensagens trocadas entre dois componentes de rede

# pilhas de protocolo TCP/IP

**IP:** cuida do enderçamento dos dipositivos e do roteamento para que os pacotes de dados cheguem ao destino certo

**TCP:** divide os dados em pedaçõs, envia e garante que cheguem completos ao destino certo

```bash

    Aplicação - faz a ponte do usuario a rede
    Tranporte - usa TCP para entrega segura ou UDP para entrega rapidas
    rede - usa IP para guiar os pacotes pelas redes ate o destino
    Enlace -|
    Física -|____ lidam com o meio de transmissão fisica de dados
```
