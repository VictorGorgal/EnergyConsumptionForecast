# PowerConsumption
Projeto para a criação de um dataset de consumo de energia residencial

O arduino fica conectado via USB a um raspberry Pi que será o servidor deste projeto. Os arquivos read_arduino.py e send_data.py precisam estar rodando para o projeto funcionar, o arquivo check_data.py só deverá ser rodado quando houver uma suspeita de que houve queda de energia.

Primeiramente o read_arduino.py requisita o arduino a medida de potência sendo consumida naquele instante e salva no dataset.txt 
O send_data.py cuida da comunição MQTT para enviar as informações do dataset de um dia específico ao aplicativo de celular (WIP)
