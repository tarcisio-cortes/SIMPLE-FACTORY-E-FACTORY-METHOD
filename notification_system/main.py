# Ponto de entrada/Teste
# --- Importações para o Sistema de Notificação ---
from notifications.client import ServicoNotificacao
from notifications.factories import FactoryNotificacaoUrgente, FactoryNotificacaoNormal

# --- Importações para o Sistema de Pagamento ---
from payments.factories import FactoryPagamentoRapido, FactoryPagamentoPrazo

def testar_sistema_notificacao():
    """Demonstração da criação de notificações diferentes via Fábrica."""
    print("--- 🔔 Sistema de Notificação (Factory Method) ---")

    # 1. Serviço com Fábrica Normal
    factory_normal = FactoryNotificacaoNormal()
    servico_normal = ServicoNotificacao(factory_normal)
    print("\n--- NOTIFICAÇÃO NORMAL ---")
    servico_normal.notificar("usuario@exemplo.com", "Sua fatura está disponível.")
    
    # 2. Serviço com Fábrica Urgente
    factory_urgente = FactoryNotificacaoUrgente()
    servico_urgente = ServicoNotificacao(factory_urgente)
    print("\n--- NOTIFICAÇÃO URGENTE ---")
    servico_urgente.notificar("99 99999-9999", "Alerta de segurança: atividade incomum detectada!")

def testar_sistema_pagamento():
    """Demonstração da criação de pagamentos diferentes via Fábrica e execução da operação pagar()."""
    print("\n\n--- 💳 Sistema de Pagamento (Factory Method) ---")

    # 1. Serviço de Pagamento Rápido
    factory_rapido = FactoryPagamentoRapido()
    print("\n--- PAGAMENTO RÁPIDO ---")
    factory_rapido.processar(150.75) # O método 'processar' usa o Factory Method 'criarPagamento' e executa 'pagar()'
    
    # 2. Serviço de Pagamento com Prazo
    factory_prazo = FactoryPagamentoPrazo()
    print("\n--- PAGAMENTO A PRAZO ---")
    factory_prazo.processar(899.90) # O método 'processar' usa o Factory Method 'criarPagamento' e executa 'pagar()'

def main():
    testar_sistema_notificacao()
    testar_sistema_pagamento()

if __name__ == "__main__":
    main()