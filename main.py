import cv2 as cv

import numpy as np

from matplotlib import pyplot as plt

# variavel que irá ler a imagem a ser trabalhada e passando 0 para convertar para GRAYSCALE
img = cv.imread('imagens/python.png', 0)

# cópia da imagem para assim ver o "antes e depois"
imageCopy = img.copy()

# criando variáveis para salver o tamanho da imagem "shape"
altura, largura = imageCopy.shape
print(altura, largura)

# função thresold com seus parâmetros, onde o primeiro é a imagem, o segundo o limite do pixel e o
# terceiro é o valor máximo do pixel

# THRESH_BINARY vai setar os valores acima do limite para 255 e os valores abaixo para 0.
ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# THRESH_BINARY_INV irá fazer o oposto do BINARY
ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)

# THRESH_TOZERO irá setar para 0 quando o valor do pixel for menor que o limite
ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)

# THRESH_TRUNC irá setar os valores que passar do limite para o seu próprio valor passado, nesse caso "127"
# o restante permaneceram os mesmos
ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)

# salvando as imagens do threshold
cv.imwrite('ImagensSemFloodFill/ORIGINAL_IMAGE.png', img)
cv.imwrite('ImagensSemFloodFill/BINARY.png', thresh1)
cv.imwrite('ImagensSemFloodFill/BINARY_INV.png', thresh2)
cv.imwrite('ImagensSemFloodFill/TOZERO.png', thresh3)
cv.imwrite('ImagensSemFloodFill/TRUNC.png', thresh4)

titles = ["Original Image", "BINARY", "BINARY_INV", "TOZERO", "TRUNC"]
images = [img, thresh1, thresh2, thresh3, thresh4]

# for para setar as posições de cada imagem na matriz e montar os subplots
for i in range(5):
    plt.figure('Sem o FloodFill')
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], "gray", vmin=0, vmax=255)
    plt.title(titles[i])

# Abaixo comeca o FloodFill

# for percorrendo a altura e largura da imagem, vendo o valor armazenado em cada pixel
for i in range(altura):
    for j in range(largura):
        if imageCopy[i, j] > 200:  # onde irá comparar o valor do pixel e saber se é maior que 200
            cv.floodFill(imageCopy, None, (j, i), 255)   # se a condição for correta, irá ser setada a nova cor

# irá fazer o mesmo processo de alguns linhas anteriores, só que com o floodfill incluído
ret, thresh1 = cv.threshold(imageCopy, 127, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(imageCopy, 127, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(imageCopy, 127, 255, cv.THRESH_TOZERO)
ret, thresh4 = cv.threshold(imageCopy, 127, 255, cv.THRESH_TRUNC)

titles = ["Original Image", "BINARY", "BINARY_INV", "TOZERO", "TRUNC"]
images = [imageCopy, thresh1, thresh2, thresh3, thresh4]

# salvando as imagens do threshold com floodfill
cv.imwrite('ImagensComFloodFill/FLOODFILL_IMAGE.png', imageCopy)
cv.imwrite('ImagensComFloodFill/ORIGINAL_IMAGE.png', img)
cv.imwrite('ImagensComFloodFill/FLOODFILL_BINARY.png', thresh1)
cv.imwrite('ImagensComFloodFill/BINARY_INV.png', thresh2)
cv.imwrite('ImagensComFloodFill/TOZERO.png', thresh3)
cv.imwrite('ImagensComFloodFill/TRUNC.png', thresh4)

for i in range(5):
    plt.figure('Com o FloodFill')
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], "gray", vmin=0, vmax=255)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks()

plt.show()

cv.imshow('Original', img)
cv.imshow('floodfill', imageCopy)

# função que permite mostrar a janela, como n foi passado como parâmetro, irá ser mostrada até fechar janela
cv.waitKey()
