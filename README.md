# Conversor de Imagens JPEG para PSD

Este projeto é um script em Python que utiliza o Photoshop para converter imagens no formato JPEG para PSD de forma automática. Ele percorre um diretório específico, processa os arquivos JPEG encontrados e salva as versões convertidas em um novo diretório.

## Funcionalidades

- Conversão automática de imagens JPEG (.jpg e .jpeg) para PSD.
- Criação automática do diretório de saída caso ele não exista.
- Suporte para múltiplos arquivos no diretório de origem.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para desenvolvimento do script.
- **Photoshop Python API**: Biblioteca utilizada para interagir com o Adobe Photoshop.
- **OS Module**: Para manipulação de arquivos e diretórios.

## Requisitos

1. Python 3.6 ou superior.
2. Adobe Photoshop instalado e configurado no sistema.
3. Biblioteca `photoshop-python-api` instalada:

```bash
pip install photoshop-python-api
```

## Como Usar

1. Clone ou faça o download deste repositório.
2. Certifique-se de que os diretórios para imagens JPEG e PSD estão configurados corretamente no código:

```python
jpeg_dir = r"C:\Users\seu_usuario\Downloads\Conversão\Jpeg"
psd_dir = r"C:\Users\seu_usuario\Downloads\Conversão\PSD"
```

3. Execute o script:

```bash
python convert_jpg_to_psd.py
```

4. As imagens convertidas serão salvas no diretório especificado para PSDs.

## Estrutura do Projeto

```
Conversão/
|-- Jpeg/                # Diretório com as imagens JPEG de entrada
|-- PSD/                 # Diretório onde serão salvas as imagens convertidas
|-- convert_jpg_to_psd.py # Script principal
```

## Problemas Comuns

1. **Erro ao importar `photoshop`:** Verifique se o Photoshop está instalado e configurado corretamente no sistema.
2. **Arquivo não encontrado:** Certifique-se de que o caminho especificado para os diretórios está correto.

## Licença

Este projeto é distribuído sob a Licença MIT. Consulte o arquivo LICENSE para mais informações.

---

Feito com ❤ por Felipe

