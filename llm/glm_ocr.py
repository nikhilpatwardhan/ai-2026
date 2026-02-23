from pathlib import Path 
from ollama_ocr import OCRProcessor


def run_ocr(image_path: Path) -> str:
    ocr = OCRProcessor(model_name="glm-ocr:latest")
    result = ocr.process_image(
        image_path=image_path,
        format_type="text",
        custom_prompt="Transcribe this document as clean Markdown",
        language="English",
    )
    return result


if __name__ == "__main__":
    run_ocr(Path(r"C:\temp\invoice-2.pdf"))
