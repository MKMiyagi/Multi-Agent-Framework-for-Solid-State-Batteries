import os
import torch
from pathlib import Path
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions, AcceleratorOptions, AcceleratorDevice, TableFormerMode
from docling.datamodel.base_models import InputFormat


if torch.cuda.is_available():
    accelerator = AcceleratorDevice.CUDA
elif torch.backends.mps.is_available():
    accelerator = AcceleratorDevice.MPS
else:
    accelerator = AcceleratorDevice.AUTO

pipeline_options = PdfPipelineOptions()
pipeline_options.accelerator_options = AcceleratorOptions(num_threads=1, device=accelerator)
pipeline_options.do_ocr = False                  
pipeline_options.do_picture_classification = False 
pipeline_options.do_picture_description = False   
pipeline_options.generate_picture_images = False   
pipeline_options.generate_page_images = False   
pipeline_options.table_structure_options.mode = TableFormerMode.ACCURATE 
pipeline_options.do_table_structure = True

doc_converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
    }
)

input_folder = Path("./pdfs")
output_folder = Path("./processed_text_only")
output_folder.mkdir(parents=True, exist_ok=True)

pdf_files = list(input_folder.glob("*.pdf"))
print(f"Found {len(pdf_files)} PDFs. Starting conversion...")

for pdf_file in pdf_files:
    try:
        print(f"Converting: {pdf_file.name}...")
        result = doc_converter.convert(pdf_file)
        markdown_content = result.document.export_to_markdown(image_placeholder="")

        output_filename = output_folder / f"{pdf_file.stem}.md"
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(markdown_content)
            
    except Exception as e:
        print(f"Failed to convert {pdf_file.name}: {e}")

print("Markdown files are in 'processed_text_only'.")