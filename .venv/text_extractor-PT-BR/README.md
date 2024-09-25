text_extractor-PT-BR
Um pacote Python para extrair textos de imagens usando pytesseract, com suporte para pré-processamento de imagens e extração de texto em português.

Funcionalidades
Extração de Texto: Extrai texto de imagens utilizando o Tesseract OCR.
Pré-processamento de Imagens: Conversão para escala de cinza e binarização para melhorar a precisão do OCR.
Suporte a Múltiplos Idiomas: O idioma padrão é o português, mas pode ser alterado para qualquer idioma suportado pelo Tesseract.
Instalação
Para instalar o pacote, use o pip:

```bash
Copiar código
pip install text_extractor-PT-BR 
```
Dependências
O pacote depende das seguintes bibliotecas:

pytesseract
Pillow
opencv-python
Além disso, o Tesseract OCR precisa estar instalado no sistema.

Instalação do Tesseract
Windows: Baixe e instale o Tesseract aqui.

Ubuntu:

```bash

sudo apt update
sudo apt install tesseract-ocr
```

MacOS:
```bash

brew install tesseract
```

Como Usar
1. Importando o Pacote
Importe as funções extract_text e preprocess_image para utilizar no seu script:

```python

from text_extractor import extract_text, preprocess_image
```
2. Extraindo Texto de uma Imagem
A função extract_text pode ser usada para extrair texto diretamente de uma imagem:

```python

# Extrair texto diretamente de uma imagem
texto = extract_text('caminho/para/imagem.png', lang='por')
print(texto)
```
3. Usando Pré-processamento
Se a imagem precisar de processamento antes da extração, como conversão para escala de cinza e binarização, você pode utilizar o parâmetro preprocess:

```python

# Extrair texto de uma imagem com pré-processamento
texto = extract_text('caminho/para/imagem.png', lang='por', preprocess=True)
print(texto)
```
4. Exemplos de Uso
Extração Simples
```python

from text_extractor import extract_text

# Caminho para a imagem
image_path = 'imagens/documento.png'

# Extração de texto sem pré-processamento
texto = extract_text(image_path, lang='por')
print("Texto extraído:")
print(texto)
Extração com Pré-processamento
python
Copiar código
from text_extractor import extract_text

# Caminho para a imagem
image_path = 'imagens/documento_ruidoso.png'

# Extração de texto com pré-processamento
texto = extract_text(image_path, lang='por', preprocess=True)
print("Texto extraído com pré-processamento:")
print(texto)
```
Pré-processamento Manual e Extração
```python

from text_extractor import preprocess_image, extract_text

# Caminho para a imagem
image_path = 'imagens/documento.png'

# Caminho para salvar a imagem pré-processada
processed_image_path = 'imagens/documento_processado.png'

# Pré-processamento da imagem
preprocess_image(image_path, output_path=processed_image_path)

# Extração de texto a partir da imagem pré-processada
texto = extract_text(processed_image_path, lang='por')
print("Texto extraído após pré-processamento:")
print(texto)
```

5. Parâmetros Disponíveis
extract_text(image_path, lang='eng', preprocess=False)
image_path: Caminho para a imagem de entrada.
lang: Idioma para o OCR (padrão: 'eng' para inglês, 'por' para português).
preprocess: Se True, pré-processa a imagem antes de extrair o texto (padrão: False).
preprocess_image(image_path, output_path=None)
image_path: Caminho para a imagem de entrada.
output_path: Caminho para salvar a imagem processada (opcional). Se não for fornecido, retorna a imagem processada em formato array.
Contribuindo
Sinta-se à vontade para abrir issues e enviar pull requests. Toda ajuda é bem-vinda!

Licença
Este projeto é licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.