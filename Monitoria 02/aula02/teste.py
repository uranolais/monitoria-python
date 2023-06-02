def cria_camera(nome, endereco_ip, senha):
    camera = {"nome":nome, "endereco_ip":endereco_ip, "senha":senha}
    return camera

def valida_acesso(camera, senha):
    return camera["senha"]==senha

def acessa_camera(camera):
    # Código para conectar à câmera IP e obter a imagem
    endereco_ip = camera["endereco_ip"]
    # Código para se conectar à câmera usando o endereço IP
    # Código para obter a imagem da câmera    
    # Retorna a imagem obtida

cria_camera("lais",a,1234)

