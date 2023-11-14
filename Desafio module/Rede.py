from time import sleep
import wifi
wifi.CriarRedeWifi()
wifi.AlterarSenhaWifi()
wifi.ConectarWifi()
sleep(3)
print('Conexão realizada com sucesso.')
