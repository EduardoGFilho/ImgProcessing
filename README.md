# Projeto de Processamento de Imagens

## O projeto prevê dois problemas de filtragem de imagens:
* 1) Realçar o contraste de uma imagem
* 2) Remover o ruído do tipo “salt & pepper” e “gaussian” de imagens


## 1) Realçar o contraste de uma imagem
Siga os passos:
* a) Estude o código abaixo.

~~~Matlab
%retirado de http://www.mathworks.com/help/images/filter-images-using-predefined-filters.html
I = imread('moon.tif');
h = fspecial('unsharp')
I2 = imfilter(I,h);
imshow(I), title('Original Image')
figure, imshow(I2), title('Filtered Image')
~~~

* b) Ao invés do filtro h acima (obtido com fspecial), construa você mesmo um filtro que produza resultado semelhante, de realce de contraste, e informe a matriz que denota este filtro.
  * A implementação consta no repositório, a matriz utilizada foi:
~~~Python 
#passando 0.2 como parâmetro para a funcao
def fspecialUnsharpen(alpha):
    h = np.array([[-alpha, alpha-1, -alpha],
                [alpha-1, alpha + 5, alpha-1],
                [-alpha, alpha-1, -alpha]])
    return (1/(alpha+1))*h
~~~
* c) Explique o motivo do seu filtro realçar o contraste e coloque uma imagem filtrada por ele no seu relatório, junto com a original. Pode ser a própria “moon.tif” ou outra.
  * As imagens constam no repositório, dentro da pasta "Sharpen"
  * A matriz apresentada pode ser obtida a partir da soma de um impulso unitário com uma matriz, definida de tal forma que sua convolução com uma imagem produz aproximadamente o mesmo resultado que aplicar o operador laplaciano sobre esta. Partindo da propriedade associativa das convoluções, podemos entender uma convolução da imagem com a matriz definida como representando a soma da imagem com o próprio laplaciano. Visto que o operador laplaciano apenas possui valor distinto de 0 quando há variação da intensidade de um pixel em relaçao à sua "vizinhanca", podemos concluir que o resultado da convolução será uma imagem composta pela original acrescida de valor onde há variação de sua intensidade, o que é percebido como realce.
* d) O seu filtro pode ser entendido como “passa-baixa” ou “passa-alta”?
  * Como elaborado na questão anterior, o filtro dá ênfase às regiões de maior variação de intensidade da imagem, portanto, pode ser entendido como "passa-alta".

## 2) Remover o ruído do tipo “salt & pepper” e “gaussian” de imagens

Siga os passos:
* a) Obtenha uma foto que tenha um fundo relativamente homogêneo (“quase” uma única cor) e um ou mais objetos em 1º plano. A resolução mínima é de 200 x 200 pixels (pode ser maior). Pode ser uma foto sua ou de um rosto obtido na Internet. Não repita a foto usada por um colega nem deixe repetirem a sua. Para lhe inspirar e servir como exemplo, a foto abaixo tem as características desejadas.
  * A imagem consta no repositório, dentro da pasta "PSNR"

* b) Se a imagem for colorida, a converta para tons de cinza, usando 8 bits por pixel, com valores de 0 a 255. A função rgb2gray.m faz isso. A imagem em tons de cinza será chamada de “im_original”.
  * Consta no repositório 
* c) Usando a função imnoise, crie uma versão ruidosa da imagem original com ruído do tipo “salt & pepper” e densidade (“density”, parâmetro da imnoise) de 0.06. Repita o passo mas com density de apenas 0.005. Além destas duas imagens com ruído salt & pepper, gere imagens com ruído Gaussiano de média 0 e variâncias 0.001 e 0.03, por exemplo, com o comando:
~~~Matlab
imnoise(im_original,'gaussian',0,0.001)
~~~
No final, você deve ter 4 versões ruidosas da imagem original.

Sua tarefa é usar filtros para reduzir o ruído das versões ruidosas e comparar com a imagem original. A figura de mérito da filtragem será a PSNR, ou “razão sinal de pico / ruido”, que usa como “pico” o valor máximo de um pixel que é igual a 255 neste caso. A PSNR pode ser calculada em dB como segue:
~~~Matlab
error=im_original-im_pouco_ruido; %imagem de erro
MSE=mean(error(:).^2) %error(:) eh um vetor 
PSNR = 10*log10(255^2/MSE)  %valor em dB
~~~

Os dois filtros a serem usados são o de média e mediana. O de média pode ser obtido com ```fspecial('average',M)``` , onde M indica que o kernel do filtro é de dimensão M x M. Depois de se obter o kernel do filtro, pode-se usar a função ```filter2``` para executar a filtragem. O filtro de mediana pode usar diretamente a função ```medfilt2``` com algo como
```medfilt2(noisyImage,[M M])```
onde o [M M] indica uma região de M x M pixels da qual se extrai a mediana. Para ambos os filtros, variem os valores de M no conjunto {3, 5, 7}.

* d) Para cada uma das 4 versões ruidosas, para cada um dos dois tipos de filtro (média e mediana) e para cada um dos 3 valores de M, calcule a PSNR entre a imagem original e a imagem ruidosa após passar pelo filtro. Para ter uma ideia dos valores envolvidos, calcule também a PSNR entre a imagem original e a versão ruidosa, sem passar por filtro.
  * Consta no repositório.
Ao fim das simulações, você terá resultados como o abaixo. Componha a partir deles uma tabela e a coloque como parte de seu relatório. Coloque também o script Matlab / Octave usado.

Responda no relatório o seguinte:
* 1) Por que para o ruído salt & pepper o filtro de mediana é tão melhor que o de média?
  * Visto que o ruído salt and pepper é caracterizado por pontos completamente pretos ou completamente brancos espalhados pela imagem, representados por valor máximo ou mínimo de intensidade em uma imagem digital, temos que ao organizá-los numa lista, os pixels ruidosos sempre estarão nas suas extremidades. Visto que a mediana de uma lista retorna apenas os valores no seu meio, os pixels ruidosos tendem a ser despezados pelo algoritmo. Ademais, se a distribuição de pixels brancos e pretos for semelhante numa mesma região, haverá pequeno deslocamento dos pixels no meio da lista visto que a quantidade de pixels brancos adicionados a um extremo e pretos adicionados ao outro tendem a se balancear.
* 2) A PSNR é uma figura de mérito objetiva, mas analisando as imagens de forma subjetiva, qual o filtro que conserva melhor as bordas dos objetos na imagem?
  * Analisando de forma subjetiva, o filtro de mediana converva melhor as bordas dos objetos
* 3) Quando o ruído é Gaussiano e a PSNR é relativamente alta, os filtros não parecem ajudar muito (melhorar a PSNR). Mas quando a PSNR é baixa, eles parecem melhorar. Você concorda? Se sim, qual o motivo deste comportamento? Se não, em qual aspecto o raciocínio está incompleto?
  * Eu concordo com a afirmação. O comportamento provavelmente se deve ao fato de que  quando uma imagem já possui baixo  ruído (PSNR alta), por mais que o ruído seja removido, a diferença causada por tal não será muito expressiva, o que é acentuado pelo fato de dB ser uma escala logaritmica. Por outro lado, quando a imagem possui alto ruído, qualquer efeito que o filtro cause provavelmente causará redução do ruído, portanto alteração mais expressiva na PSNR.
* 4) Pensando no custo computacional dos processos de filtragem, qual o filtro que demanda mais poder de processamento, o de média ou mediana?
  * O custo computacional depende dos algoritmos empregados, contudo, assumindo implementação eficiente de ambos os filtros, o mais custoso seria o de mediana, pois precisa de operações como sorting de uma lista para cada pixel na imagem.
