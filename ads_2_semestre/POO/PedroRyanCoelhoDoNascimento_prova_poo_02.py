from abc import ABC, abstractmethod


class DispositivoDeRede(ABC):
    def __init__(self, nome_do_dispositivo: str, endereco_ip: str) -> None:
        self._nome_do_dispositivo = nome_do_dispositivo
        self._endereco_ip = endereco_ip

    @property
    def nome_dispositivo(self) -> str:
        return self._nome_do_dispositivo

    @nome_dispositivo.setter
    def nome_dispositivo(self, nome: str) -> None:
        self._nome_do_dispositivo = nome

    @property
    def endereco_ip(self) -> str:
        return self._endereco_ip

    @endereco_ip.setter
    def endereco_ip(self, ip: str) -> None:
        self._endereco_ip = ip

    @abstractmethod
    def configuracao(self) -> str:
        pass

    def __str__(self) -> str:
        return f"Nome: {self._nome_do_dispositivo} | IP: {self._endereco_ip}"


class Roteador(DispositivoDeRede):
    def __init__(self,nome_do_dispositivo: str,endereco_ip: str,protocolo: str,) -> None:
        super().__init__(nome_do_dispositivo, endereco_ip)
        self.protocolo = protocolo

    def configuracao(self) -> str:
        return (
            f"Roteador: configurando protocolo {self.protocolo} "
            f"no dispositivo {self.nome_dispositivo}"
        )


class Switch(DispositivoDeRede):
    def __init__(self,nome_do_dispositivo: str,endereco_ip: str,vlan: str,) -> None:
        super().__init__(nome_do_dispositivo, endereco_ip)
        self.vlan = vlan

    def configuracao(self) -> str:
        return (
            f"Switch: configurando VLAN {self.vlan} "
            f"no dispositivo {self.nome_dispositivo}"
        )


class Firewall(DispositivoDeRede):
    def __init__( self,nome_do_dispositivo: str,endereco_ip: str,nivel_de_seguranca: str,) -> None:
        super().__init__(nome_do_dispositivo, endereco_ip)
        self.nivel_de_seguranca = nivel_de_seguranca

    def configuracao(self) -> str:
        return (
            f"Firewall: configurando nível de segurança "
            f"{self.nivel_de_seguranca} no dispositivo {self.nome_dispositivo}"
        )


class TopologiaRede:
    def __init__(self) -> None:
        self.dispositivos_de_rede: list[DispositivoDeRede] = []

    def adicionar(self, dispositivo: DispositivoDeRede) -> None:
        self.dispositivos_de_rede.append(dispositivo)

    def remover_dispositivo(self, dispositivo: DispositivoDeRede) -> None:
        self.dispositivos_de_rede.remove(dispositivo)

    def listar_dispositivo(self) -> None:
        for indice, dispositivo in enumerate(self.dispositivos_de_rede, start=1):
            print(f"{indice}. {dispositivo}")

    def provisionamento_global(self) -> None:
        for dispositivo in self.dispositivos_de_rede:
            print(dispositivo.configuracao())


roteador = Roteador("Roteador Central", "192.168.1.1", "OSPF")
switch = Switch("Switch do Escritório", "192.168.1.2", "10")
firewall = Firewall("Firewall Principal", "192.168.1.3", "Alto")

topologia = TopologiaRede()

print("\n====== ADICIONANDO DISPOSITIVOS ======\n")
topologia.adicionar(roteador)
topologia.adicionar(switch)
topologia.adicionar(firewall)

print("\n====== LISTANDO DISPOSITIVOS ======\n")
topologia.listar_dispositivo()

print("\n====== PROVISIONAMENTO GLOBAL ======\n")
topologia.provisionamento_global()



