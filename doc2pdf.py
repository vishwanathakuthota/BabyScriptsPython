import os
import subprocess
import sys
from pathlib import Path

def convert_to_pdf(input_path, output_dir):
    """
    Convert a single file (DOC/DOCX/PPT/PPTX) to PDF using LibreOffice.
    """
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return

    command = [
        "soffice", "--headless", "--convert-to", "pdf", "--outdir", output_dir, input_path
    ]

    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Converted: {os.path.basename(input_path)} → PDF in {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {input_path}: {e}")

def batch_convert(folder_path, output_dir=None):
    """
    Batch convert all DOC/DOCX/PPT/PPTX files in a folder to PDF.
    """
#    folder_path = Path(folder_path)
    folder_path = Path(folder_path)

    if not folder_path.exists():
        print(f"Folder not found: {folder_path}")
        return

    if output_dir is None:
        output_dir = folder_path
    else:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

    supported_ext = [".doc", ".docx", ".ppt", ".pptx"]

    files_to_convert = [f for f in folder_path.glob("*") if f.suffix.lower() in supported_ext]

    if not files_to_convert:
        print("No supported files found in the folder.")
        return

    for file_path in files_to_convert:
        convert_to_pdf(str(file_path), str(output_dir))

if _name_ == "main":
    if len(sys.argv) < 2:
        print("Usage: python batch_convert_to_pdf.py <input_folder> [output_folder]")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2] if len(sys.argv) > 2 else None

    batch_convert(input_folder, output_folder)