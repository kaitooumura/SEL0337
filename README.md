# Prática 5: Configuração de Serviços SystemD e Versionamento com Git

## Resumo do Projeto
Este projeto foi desenvolvido para a disciplina SEL0337 - Projetos em Sistemas Embarcados. O objetivo principal foi explorar o processo de inicialização (boot) de sistemas Linux embarcados, configurando o systemd para gerenciar serviços personalizados.

Foi implementada uma aplicação de automação que controla um LED conectado à GPIO da Raspberry Pi. O serviço foi configurado para iniciar automaticamente junto com o sistema operacional, sem necessidade de intervenção manual do usuário.

## Hardware Utilizado
* Raspberry Pi
* LED e Resistor
* Protoboard e Jumpers
* Conexão na GPIO 15 (BCM)

## Estrutura dos Arquivos
O projeto é composto pelos seguintes scripts desenvolvidos em Python:

* **`pratica5.py`**: Script principal responsável por fazer o LED piscar em loop infinito. Ele utiliza a biblioteca `RPi.GPIO` para alternar o estado do pino 15.
* **`pratica5off.py`**: Script auxiliar de limpeza. Sua função é desligar o LED e liberar a GPIO (`GPIO.cleanup()`) garantindo que o hardware fique em um estado seguro ao encerrar o serviço.
* **`python_pratica5.service`**: O Unit File do systemd que gerencia a execução.

## Funcionamento do Serviço SystemD

O gerenciamento do processo é feito através do arquivo de unidade `python_pratica5.service`, configurado com as seguintes diretrizes:

1.  **Inicialização (`ExecStart`)**:
    Ao iniciar o sistema (target `multi-user`), o systemd executa o comando definido em `ExecStart`, chamando o interpretador Python para rodar o script `pratica5.py`. Isso faz com que o LED comece a piscar imediatamente após o boot.

2.  **Parada (`ExecStop`)**:
    Ao receber o comando de parada (`sudo systemctl stop python_pratica5`), o systemd executa o comando definido em `ExecStop`. Este comando aciona o script `pratica5off.oy`, que desliga o LED corretamente antes de encerrar o processo.

3.  **Permissões (`User`)**:
    O serviço foi configurado para rodar sob o usuário específico (ex: `sel`), garantindo as permissões necessárias para acesso à memória da GPIO.

### Comandos de Controle
Para gerenciar o serviço manualmente no terminal, utilizamos os comandos do utilitário `systemctl`:

```bash
# Iniciar o serviço manualmente
sudo systemctl start python_pratica5

# Parar o serviço (aciona o pratica5off.py)
sudo systemctl stop python_pratica5

# Verificar o status e logs
sudo systemctl status python_pratica5

# Habilitar inicialização automática no boot
sudo systemctl enable python_pratica5
