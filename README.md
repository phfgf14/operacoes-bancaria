# Sistema Bancário Simples

Este projeto é uma aplicação de terminal para operações bancárias básicas, desenvolvida em Python. Permite realizar depósitos, saques (com limites) e visualizar o extrato das operações.

## Funcionalidades

- **Depositar:** Permite adicionar valores à conta, desde que positivos.
- **Sacar:** Permite realizar saques, respeitando o limite de valor por saque e o número máximo de saques por sessão.
- **Visualizar Extrato:** Exibe todas as transações realizadas, total de depósitos, total de saques e saldo atual.
- **Sair:** Encerra o sistema.

## Limites

- Máximo de 3 saques por sessão.
- Valor máximo por saque: R$ 500,00.

## Como usar

1. Clone este repositório ou copie o arquivo [`src/operacoes_bancaria.py`](src/operacoes_bancaria.py).
2. Execute o arquivo Python:

   ```sh
   python src/operacoes_bancaria.py
   ```

3. Siga as instruções do menu exibido no terminal.

## Estrutura do Código

- [`depositar()`](src/operacoes_bancaria.py): Função para depósitos.
- [`sacar()`](src/operacoes_bancaria.py): Função para saques.
- [`visualizar_extrato()`](src/operacoes_bancaria.py): Função para exibir o extrato.
- Variáveis globais para controle de depósitos, saques, extrato e limites.

## Exemplo de Uso

```
Bem-vindo ao sistema bancário!

-- Menu de operações ---
1. Sacar
2. Depositar
3. Visualizar extrato
4. Sair

Escolha uma opção:
```

## Requisitos

- Python 3.x


