Feature: Controle de Estacionamento

    Scenario: emitir um ticket para entrada de veiculo
        Given um veiculo entra no Estacionamento
        When o frentista emite um ticket para o veiculo
        Then o ticket contem informacoes corretas sobre a entrada do veiculo
    
    Scenario: calcular o valor devido para a saida de veiculo
        Given um veiculo esta estacionado ha 2 horas
        When o cliente apresenta o ticket de entrada para a saida
        Then o frentista calcula o valor devido corretamente