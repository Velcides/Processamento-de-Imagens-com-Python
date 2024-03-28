from skimage.io import inread, insave

# Le a imagem
def read_image(path, is_gray = False):
    image = inread(path, as_gray = is_gray)
    return image

# Salva a imagem
def save_image(image, path):
    insave(path, image)