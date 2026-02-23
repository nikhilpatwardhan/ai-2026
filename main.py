import sys
import logging
from pathlib import Path
from llm import glm_ocr, model_chat

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)


def run():
    logger.info("Parsing PDF...")
    parsed_text = glm_ocr.run_ocr(Path(r"C:\temp\invoice-2.pdf"), "Transcribe this document as clean Markdown")

    logger.info("Asking LLM for total")
    prompt = "Extract only the Total amount in dollars in the following parsed invoice. \n\n" + parsed_text
    response = model_chat.run_prompt("smollm2", prompt)

    logger.info(response)

if __name__ == '__main__':
    run()