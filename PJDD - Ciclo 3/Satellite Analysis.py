#Aluno -> Douglas Leonel de Almeida
#Matricula -> 2110213

from PIL import Image
import numpy as np

# Área total do Brasil em hectares (IBGE)
AREA_BRASIL_HECTARES = 851576700

# Carregar a imagem
image_path = "path_para_sua_imagem.png"  # Substitua pelo caminho correto da imagem
def analyze_image(image_path):
    # Abrir imagem
    image = Image.open(image_path)
    
    # Converter para matriz NumPy
    img_array = np.array(image)

    # Contagem total de pixels
    total_pixels = img_array.size

    # Contar pixels por categoria
    unique, counts = np.unique(img_array, return_counts=True)
    pixel_counts = dict(zip(unique, counts))

    # Obter os pixels desejados
    pixels_no_data = pixel_counts.get(0, 0)
    pixels_soja = pixel_counts.get(39, 0)
    pixels_pastagem = pixel_counts.get(15, 0)

    # Pixels válidos (total menos sem dados)
    valid_pixels = total_pixels - pixels_no_data

    # Percentual de soja e pastagem no território nacional
    perc_soja = (pixels_soja / valid_pixels) * 100
    perc_pastagem = (pixels_pastagem / valid_pixels) * 100

    # Cálculo das áreas em hectares
    area_soja_hectares = (perc_soja / 100) * AREA_BRASIL_HECTARES
    area_pastagem_hectares = (perc_pastagem / 100) * AREA_BRASIL_HECTARES

    # Resultados
    results = {
        "total_pixels": total_pixels,
        "pixels_no_data": pixels_no_data,
        "pixels_soja": pixels_soja,
        "pixels_pastagem": pixels_pastagem,
        "area_soja_hectares": area_soja_hectares,
        "area_pastagem_hectares": area_pastagem_hectares,
    }

    return results

# Caminho da imagem
image_path = "sua_imagem.png"  # Substitua pelo caminho correto da imagem

# Executar análise
resultados = analyze_image(image_path)

# Exibir resultados
print(f"Total de pixels: {resultados['total_pixels']}")
print(f"Pixels sem dados (código 0): {resultados['pixels_no_data']}")
print(f"Pixels de soja (código 39): {resultados['pixels_soja']}")
print(f"Pixels de pastagem (código 15): {resultados['pixels_pastagem']}")
print(f"Área de soja em hectares: {resultados['area_soja_hectares']:.2f}")
print(f"Área de pastagem em hectares: {resultados['area_pastagem_hectares']:.2f}")")
