# Projeto de agendamento de estações de trabalho - Backend

**Projeto que é minha primeira vez usando Django**.

## Funcionalidades

- Requisito mínimo:
	- Painel administrativo (com *django-admin*):
		- CRUD de reservas + ver lista.
		- CRUD de estações de trabalho + ver lista.
	- Endpoints:
		- Reservas.
			- Listar.
			- Criar.
		- Estações de trabalho.
			- Listar.

- Entrega:
	- Painel administrativo (com *django-admin*).
		- Info:
			- Url: <http://127.0.0.1:9001/admin/>
			- Username: `admin`
			- Password: `123123`
		- Features:
			- CRUD de reservas + ver lista.
			- CRUD de estações de trabalho + ver lista.
	- Endpoints:
		- Reservas.
			- Listar: <http://localhost:9001/schedules/>
			- Criar: <http://localhost:9001/schedules/create/>
			- Bônus:
				- Apagar: <http://localhost:9001/schedules/:id/delete>
				- Ver: <http://localhost:9001/schedules/:id/>
				- Editar: <http://localhost:9001/schedules/:id/update/>
		- Estações de trabalho.
			- Listar: <http://localhost:9001/workstations/>
			- Bônus:
				- Criar: <http://localhost:9001/workstations/create/>
				- Apagar: <http://localhost:9001/workstations/:id/delete>
				- Ver: <http://localhost:9001/workstations/:id/>
				- Editar: <http://localhost:9001/workstations/:id/update/>

## Opções técnicas

- O projeto utiliza o [SQLite](https://www.sqlite.org/) como solução RDBMS para fins de simplicidade.

## Instalação

O projeto utiliza o [Pipenv](https://pipenv.pypa.io/en/latest/) para facilitar o gerenciamento de pacotes e *virtual environments*.

Podemos instalar o *Pipenv* via *pip*: `pip install pipenv`.  
(Caso, deseje outros métodos, veja no site oficial de [Pipenv](https://pipenv.pypa.io/en/latest/) )

No diretório do projeto:

1. Crie um novo *virtual environments* e instale as dependências do projeto: `pipenv install`

## Execução

No diretório do projeto:

1. Ative o *virtual environments*: `pipenv shell`
1. Execute o projeto: `python manage.py runserver 9001`

A aplicação estará rodando em <http://127.0.0.1:9001/>.

Se você estiver utilizando Visual Studio Code, há configuração para automatizar o processo, basta executar o projeto via:

- *Debug: Start Without Debugging (Ctrl+F5)*: Roda o servidor do frontend sem debugging.
- *Debug: Start Debugging (Ctrl+F5)*: Roda o servidor do frontend em modo debugging.
