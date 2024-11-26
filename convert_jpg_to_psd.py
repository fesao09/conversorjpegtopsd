import os
from photoshop import Session

# Defina os diretórios onde as imagens JPEG estão localizadas e onde os PSDs serão salvos
jpeg_dir = r"C:\Users\felipe.oliveira\Downloads\Conversão\Jpeg"
psd_dir = r"C:\Users\felipe.oliveira\Downloads\Conversão\PSD"

# Crie o diretório PSD, se não existir
os.makedirs(psd_dir, exist_ok=True)

# Função para converter imagens JPEG para PSD
def convert_jpg_to_psd(jpeg_path):
    print(f"Tentando converter: {jpeg_path}")  # Mensagem de depuração
    with Session() as session:
        # Abre a imagem JPEG no Photoshop
        doc = session.app.open(jpeg_path)
        # Define o caminho de saída para o PSD
        psd_path = os.path.join(psd_dir, os.path.splitext(os.path.basename(jpeg_path))[0] + '.psd')
        # Salva o documento como PSD
        doc.saveAs(psd_path, options=None)
        doc.close()  # Fecha o documento
    print(f"Conversão concluída: {jpeg_path} para {psd_path}")  # Mensagem de depuração

def main():
    print("Iniciando a conversão de JPEG para PSD...")  # Mensagem de depuração
    # Loop para converter todas as imagens JPG e JPEG no diretório especificado
    for filename in os.listdir(jpeg_dir):
        if filename.lower().endswith(('.jpg', '.jpeg')):  # Verifica se a extensão é .jpg ou .jpeg
            jpeg_path = os.path.join(jpeg_dir, filename)  # Caminho completo do arquivo JPEG
            try:
                convert_jpg_to_psd(jpeg_path)  # Chama a função de conversão
                print(f"Convertido: {jpeg_path} para {psd_dir}")  # Mensagem de sucesso
            except Exception as e:
                print(f"Ocorreu um erro ao converter {jpeg_path}: {e}")  # Mensagem de erro
    print("Conversão concluída.")  # Mensagem de depuração

if __name__ == "__main__":
    main()
    input("Pressione Enter para sair...")  # Mantém o prompt aberto até que o usuário pressione Enter
