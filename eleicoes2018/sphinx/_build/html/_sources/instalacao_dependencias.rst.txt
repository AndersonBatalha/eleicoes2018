Instalação das dependências
******************************
Para executar o projeto e necessário ter instalado em sua máquina:

* Python 3.6.7
* Django 1.9.10
* virtualenv
* pip (gerenciador de pacotes do Python)

Supondo que voce utilize Linux como sistema operacional, basta instalar pelo terminal:

.. code-block:: shell

   $ sudo apt install python3.6 virtualenv virtualenvwrapper python-pip

-------------------------------
Criando o ambiente virtual
-------------------------------

    Um ambiente virtual se caracteriza por isolar as aplicações instaladas para um determinado projeto, evitando conflitos de versões entre pacotes iguais que pertençam a projetos diferentes.

1. Abra o terminal e execute:

.. code-block:: shell

   $ mkvirtualenv -p `which python3` env

2. Para instalar as dependências, entre na pasta do projeto e localize o arquivo requirements.txt. Esse arquivo contem os pacotes necessários para a execução do projeto.

.. code-block:: shell

   $ pip install -r requirements.txt

E assim o projeto está pronto para ser executado.
