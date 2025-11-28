Sistema de Notificação e Pagamento

Este projeto demonstra a aplicação dos padrões de projeto **Factory Method** e **Abstract Factory** em dois módulos desacoplados: um **Sistema de Notificação** e um **Sistema de Pagamento**.

O objetivo é separar a **criação de objetos concretos** (como `NotificacaoEmail` ou `PagamentoPix`) da sua utilização pelo código cliente. Isso garante que o sistema seja altamente **extensível** e adere ao **Princípio Open/Closed** (aberto para extensão, fechado para modificação).

-----

### 🚀 Padrões Aplicados

A estrutura do projeto segue o **Factory Method Clássico** (também é uma forma de Abstract Factory, dependendo de como você vê a agregação de responsabilidades de criação).

| Módulo | Padrão Aplicado | Elemento Chave | Função no Padrão |
| :--- | :--- | :--- | :--- |
| **`notifications/`** | Factory Method | `NotificacaoFactory` | **Creator Abstrato** |
| | | `Notificacao` | **Product Abstrato** |
| **`payments/`** | Factory Method | `PagamentoFactory` | **Creator Abstrato** |
| | | `Pagamento` | **Product Abstrato** |

-----

### 📂 Estrutura do Projeto

O projeto é organizado em pacotes Python para isolar as responsabilidades e facilitar a manutenção (módulos).

```
notification_system/
├── notifications/        # Módulo 1: Sistema de Notificação
│   ├── __init__.py
│   ├── base.py           # Product Abstrato e Concreto (Notificacao, Email, SMS, etc.)
│   ├── factories.py      # Creator Abstrato e Concreto (NotificacaoFactory, Urgente, Normal)
│   └── client.py         # Cliente que usa a Factory
│
├── payments/             # Módulo 2: Sistema de Pagamento
│   ├── __init__.py
│   ├── base.py           # Product Abstrato e Concreto (Pagamento, CartaoCredito, Pix, etc.)
│   └── factories.py      # Creator Abstrato e Concreto (PagamentoFactory, Rapido, Prazo)
│
└── main.py               # Ponto de entrada para execução e testes
```

-----

### 🛠️ Como Executar

1.  **Pré-requisitos:** Certifique-se de ter o **Python 3** instalado.

2.  **Execução:** Navegue até a pasta raiz do projeto (`notification_system/`) e execute o script principal:

    ```bash
    python main.py
    ```

### 🎯 Saída do Programa

O script principal demonstra a utilização das diferentes fábricas em ambos os sistemas, comprovando o desacoplamento da lógica de criação:

```
--- 🔔 Sistema de Notificação (Factory Method) ---

--- NOTIFICAÇÃO NORMAL ---
------------------------------
🗓️ Usando fábrica NORMAL. Usando E-mail.
📧 Enviando E-mail para: usuario@exemplo.com
   Mensagem: Sua fatura está disponível.
------------------------------

--- NOTIFICAÇÃO URGENTE ---
------------------------------
🚨 Usando fábrica URGEGENTE. Priorizando SMS.
📱 Enviando SMS para: 99 99999-9999
   Mensagem: Alerta de segurança: atividade incomum detectada!
------------------------------


--- 💳 Sistema de Pagamento (Factory Method) ---

--- PAGAMENTO RÁPIDO ---
------------------------------
Iniciando serviço de pagamento para valor: R$ 150.75
⚡ Usando fábrica RÁPIDA. Priorizando Cartão de Crédito.
💳 Processando R$ 150.75 via Cartão de Crédito...
   Status: Transação aprovada e concluída.
------------------------------

--- PAGAMENTO A PRAZO ---
------------------------------
Iniciando serviço de pagamento para valor: R$ 899.90
🐌 Usando fábrica PRAZO. Usando Boleto.
📄 Gerando Boleto Bancário para R$ 899.90...
   Status: Boleto gerado. Vencimento em 3 dias úteis.
------------------------------
```
