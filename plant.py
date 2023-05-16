import tensorflow as tf
import numpy as np
import cv2

while menu != "0":
    carrega_imagem = input ("Digite o nome da planta, Ex (imagem.jpg):")

    # Carregar modelo de detecção de doenças em plantas
    modelo = tf.keras.models.load_model('')
    # Ler imagem da planta
    imagem = cv2.imread(carrega_imagem)
    # Redimensionar imagem para entrada do modelo
    imagem_redimensionada = cv2.resize(imagem, (224, 224))
    # Normalizar imagem
    imagem_normalizada = imagem_redimensionada / 255.0
    # Adicionar dimensão de lote à imagem
    imagem_normalizada = np.expand_dims(imagem_normalizada, axis=0)

    # Executar modelo na imagem
    resultado = modelo.predict(imagem_normalizada)
    # Imprimir resultado
        if resultado[0] < 0.5:
     print('Planta saudável')
        else:
        print('Planta doente')
