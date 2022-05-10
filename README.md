# PowerConsumption
Criação de um dataset de consumo de energia residencial

O arduino fica conectado a um raspberry Pi que sera o servidor deste projeto. Os arquivos read_arduino.py e send_data.py precisão estar rodando para o projeto funcionar, o arquivo check_data.py só deverá ser rodado quando houver uma suspeita de que houve queda de energia.

Primeiramente o read_arduino.py requisita ao arduino a medida de potência sendo consumida naquele instante e salva no dataset.txt 
O send_data.py cuida da comunição MQTT para enviar as informações do dataset de um dia específico ao aplicativo de celular (WIP)
