from pathlib import Path 
from ollama_ocr import OCRProcessor


def run_ocr(image_path: Path, prompt: str) -> str:
    ocr = OCRProcessor(model_name="glm-ocr:latest")
    result = ocr.process_image(
        image_path=str(image_path),
        format_type="text",
        custom_prompt=prompt,
        language="English",
    )
    return result


if __name__ == "__main__":
    response = run_ocr(Path(r"C:\temp\invoice-2.pdf"), "Transcribe this document and extract only the Total")
    print(response)