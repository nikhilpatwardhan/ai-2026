import ollama
from ollama_ocr import OCRProcessor


def main():
    ocr = OCRProcessor(model_name='glm-ocr:latest')
    result = ocr.process_image(
        image_path=r"C:\temp\invoice-2.pdf",
        format_type='text',
        custom_prompt='Transcribe this document as clean Markdown',
        language='English'
    )
    print(result)


if __name__ == "__main__":
    main()
