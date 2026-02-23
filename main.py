import sys
import json
import logging
import openpyxl
import asyncio
from dateutil import parser
from pathlib import Path
from mdextractor import extract_md_blocks
from llm import glm_ocr
from notify.telegram import send_once

logging.basicConfig(
    level=logging.WARN, # So that httpx does not print private API token on console
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

input_file = r"C:\temp\invoice-2.pdf"
output_file = r"out.xlsx"


def extract_json(markdown: str) -> str:
    blocks = extract_md_blocks(markdown)
    return json.loads(blocks[0])


def append_to_excel(json_data):
    wb = openpyxl.load_workbook(output_file)
    sheet = wb.worksheets[0]
    payload = {}
    for key, value in json_data.items():
        if "date" in key.lower():
            payload[1] = parser.parse(value).date()
        elif "total" in key.lower():
            payload[2] = float(value)
    
    sheet.append(payload)
    wb.save(output_file)
    wb.close()


def run():
    logger.info("Parsing PDF...")
    markdown = glm_ocr.run_ocr(Path(input_file), "Transcribe this document and extract the Date and Total amount as json")
    json_data = extract_json(markdown)
    append_to_excel(json_data)
    asyncio.run(send_once("Done"))
    logger.warning("Done")


if __name__ == '__main__':
    run()