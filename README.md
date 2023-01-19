#Projeto de Processamento de Imagens

##O projeto prevê dois problemas de filtragem de imagens:
  1)Realçar o contraste de uma imagem
  2)Remover o ruído do tipo “salt & pepper” e “gaussian” de imagens


##1)Realçar o contraste de uma imagem
Siga os passos:
Estude o código abaixo.

~~~Matlab
%retirado de http://www.mathworks.com/help/images/filter-images-using-predefined-filters.html
I = imread('moon.tif');
h = fspecial('unsharp')
I2 = imfilter(I,h);
imshow(I), title('Original Image')
figure, imshow(I2), title('Filtered Image')

Ao invés do filtro h acima (obtido com fspecial), construa você mesmo um filtro que produza resultado semelhante, de realce de contraste, e informe a matriz que denota este filtro.
Explique o motivo do seu filtro realçar o contraste e coloque uma imagem filtrada por ele no seu relatório, junto com a original. Pode ser a própria “moon.tif” ou outra.
O seu filtro pode ser entendido como “passa-baixa” ou “passa-alta”?

2)Remover o ruído do tipo “salt & pepper” e “gaussian” de imagens

Siga os passos:
Obtenha uma foto que tenha um fundo relativamente homogêneo (“quase” uma única cor) e um ou mais objetos em 1º plano. A resolução mínima é de 200 x 200 pixels (pode ser maior). Pode ser uma foto sua ou de um rosto obtido na Internet. Não repita a foto usada por um colega nem deixe repetirem a sua. Para lhe inspirar e servir como exemplo, a foto abaixo tem as características desejadas.


Se a imagem for colorida, a converta para tons de cinza, usando 8 bits por pixel, com valores de 0 a 255. A função rgb2gray.m faz isso. A imagem em tons de cinza será chamada de “im_original”.
Usando a função imnoise, crie uma versão ruidosa da imagem original com ruído do tipo “salt & pepper” e densidade (“density”, parâmetro da imnoise) de 0.06. Repita o passo mas com density de apenas 0.005. Além destas duas imagens com ruído salt & pepper, gere imagens com ruído Gaussiano de média 0 e variâncias 0.001 e 0.03, por exemplo, com o comando:
imnoise(im_original,'gaussian',0,0.001)
No final, você deve ter 4 versões ruidosas da imagem original.

Sua tarefa é usar filtros para reduzir o ruído das versões ruidosas e comparar com a imagem original. A figura de mérito da filtragem será a PSNR, ou “razão sinal de pico / ruido”, que usa como “pico” o valor máximo de um pixel que é igual a 255 neste caso. A PSNR pode ser calculada em dB como segue:
error=im_original-im_pouco_ruido; %imagem de erro
MSE=mean(error(:).^2) %error(:) eh um vetor 
PSNR = 10*log10(255^2/MSE)  %valor em dB


Os dois filtros a serem usados são o de média e mediana. O de média pode ser obtido com fspecial('average',M), onde M indica que o kernel do filtro é de dimensão M x M. Depois de se obter o kernel do filtro, pode-se usar a função filter2 para executar a filtragem. O filtro de mediana pode usar diretamente a função medfilt2 com algo como
medfilt2(noisyImage,[M M])
onde o [M M] indica uma região de M x M pixels da qual se extrai a mediana. Para ambos os filtros, variem os valores de M no conjunto {3, 5, 7}.

Para cada uma das 4 versões ruidosas, para cada um dos dois tipos de filtro (média e mediana) e para cada um dos 3 valores de M, calcule a PSNR entre a imagem original e a imagem ruidosa após passar pelo filtro. Para ter uma ideia dos valores envolvidos, calcule também a PSNR entre a imagem original e a versão ruidosa, sem passar por filtro.

Ao fim das simulações, você terá resultados como o abaixo. Componha a partir deles uma tabela e a coloque como parte de seu relatório. Coloque também o script Matlab / Octave usado.

Responda no relatório o seguinte:
Por que para o ruído salt & pepper o filtro de mediana é tão melhor que o de média?
A PSNR é uma figura de mérito objetiva, mas analisando as imagens de forma subjetiva, qual o filtro que conserva melhor as bordas dos objetos na imagem?
Quando o ruído é Gaussiano e a PSNR é relativamente alta, os filtros não parecem ajudar muito (melhorar a PSNR). Mas quando a PSNR é baixa, eles parecem melhorar. Você concorda? Se sim, qual o motivo deste comportamento? Se não, em qual aspecto o raciocínio está incompleto?
Pensando no custo computacional dos processos de filtragem, qual o filtro que demanda mais poder de processamento, o de média ou mediana?
