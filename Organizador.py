from PIL import Image
import os

CarpetaActual = os.path.abspath(os.getcwd())

if __name__ == "__main__":
    for filename in os.listdir(CarpetaActual):
        name, extension = os.path.splitext(CarpetaActual + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            os.makedirs(CarpetaActual + '/Fotos', exist_ok=True)
            picturesFolder = CarpetaActual + '/Fotos'
            os.rename(CarpetaActual + "/" + filename, picturesFolder + "/" + filename)
            print(filename)

        if extension in [".mp3", ".wav", ".wave", ".bwf",]:
            os.makedirs(CarpetaActual + '/Musica', exist_ok=True)
            musicFolder = CarpetaActual + '/Musica'
            os.rename(CarpetaActual + "/" + filename, musicFolder + "/" + filename)
            print(filename)

        if extension in [".mov", ".mkv", ".mp4", ".wmv", ".flv"]:
            os.makedirs(CarpetaActual + '/Videos', exist_ok=True)
            VideosFolder = CarpetaActual + '/Videos'
            os.rename(CarpetaActual + "/" + filename, VideosFolder + "/" + filename)
            print(filename)

        if extension in [".gif"]:
            os.makedirs(CarpetaActual + '/Gifs', exist_ok=True)
            gifsFolder = CarpetaActual + '/Gifs'
            os.rename(CarpetaActual + "/" + filename, gifsFolder + "/" + filename)
            print(filename)

        if extension in [".txt", ".doc", ".docx", ".md", ".odt"]:
            os.makedirs(CarpetaActual + '/Texto', exist_ok=True)
            textFolder = CarpetaActual + '/Texto'
            os.rename(CarpetaActual + "/" + filename, textFolder + "/" + filename)
            print(filename)

        if extension in [".pdf"]:
            os.makedirs(CarpetaActual + '/PDFs', exist_ok=True)
            pdfFolder = CarpetaActual + "/PDFs"
            os.rename(CarpetaActual + "/" + filename, pdfFolder + "/" + filename)
            print(filename)

        if extension in [".zip", ".rar", ".7z"]:
            os.makedirs(CarpetaActual + '/Compresiones', exist_ok=True)
            compresionesFolder = CarpetaActual + '/Compresiones'
            os.rename(CarpetaActual + "/" + filename, compresionesFolder + "/" + filename)
            print(filename)

        if extension in [".exe"]:
            os.makedirs(CarpetaActual + '/Programas', exist_ok=True)
            programasFolder = CarpetaActual + '/Programas'
            os.rename(CarpetaActual + "/" + filename, programasFolder + "/" + filename)
            print(filename)

        if extension in [".iso"]:
            os.makedirs(CarpetaActual + '/CDs', exist_ok=True)
            cdsFolder = CarpetaActual + '/CDs'
            os.rename(CarpetaActual + "/" + filename, cdsFolder + "/" + filename)
            print(filename)
