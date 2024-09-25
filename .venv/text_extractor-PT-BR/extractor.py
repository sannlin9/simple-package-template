from PIL import Image
import pytesseract
import cv2

def preprocess_image(image_path, output_path=None):
    """
    Pré-processa a imagem convertendo-a para escala de cinza e binarizando.
    :param image_path: Caminho para a imagem de entrada.
    :param output_path: Caminho para salvar a imagem processada (opcional).
    :return: Caminho para a imagem processada ou a imagem processada.
    """
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
    
    if output_path:
        cv2.imwrite(output_path, binary_image)
        return output_path
    else:
        return binary_image

def extract_text(image_path, lang='eng', preprocess=False):
    """
    Extrai texto de uma imagem usando Tesseract OCR.
    :param image_path: Caminho para a imagem de entrada.
    :param lang: Idioma para o OCR (ex: 'eng' para inglês, 'por' para português).
    :param preprocess: Se True, pré-processa a imagem antes de extrair o texto.
    :return: Texto extraído.
    """
    if preprocess:
        # Pré-processar a imagem e salvar como uma imagem temporária
        processed_image = preprocess_image(image_path)
        # Converter a imagem processada para um formato PIL para o pytesseract
        image = Image.fromarray(processed_image)
    else:
        # Carregar a imagem diretamente
        image = Image.open(image_path)
    
    # Extrair texto usando pytesseract
    custom_config = f'--oem 3 --psm 6 -l {lang}'
    text = pytesseract.image_to_string(image, config=custom_config)
    
    return text
