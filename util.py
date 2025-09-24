import os, re, logging, fitz
from entities import Word
from datetime import datetime

MONTHS = {
	"janeiro": "01",
	"fevereiro": "02",
	"março": "03",
	"abril": "04",
	"maio": "05",
	"junho": "06",
	"julho": "07",
	"agosto": "08",
	"setembro": "09",
	"outubro": "10",
	"novembro": "11",
	"dezembro": "12"
}

def setup_logger():
	"""
	Configures the logger to save logs in a ./logs folder with a timestamped filename.
	"""
	os.makedirs("logs", exist_ok=True)  # Create the logs folder if it doesn't exist
	log_filename = datetime.now().strftime("logs/%Y-%m-%d_%H-%M-%S_jointer.log")
	logging.basicConfig(
		filename=log_filename,
		level=logging.INFO,
		format="%(asctime)s - %(levelname)s - %(message)s",
		datefmt="%Y-%m-%d %H:%M:%S"
	)


def get_irregular_file_paths(folder_path: str = '.', re_pattern: str = r'^\d{4}-\d{2}__\d{3}\.pdf$') -> list[str]:
	folder_path = os.path.normpath(folder_path)
	re_compiled_pattern = re.compile(re_pattern)
	return [file_path for file_path in os.listdir(folder_path) if file_path.lower().endswith('.pdf') and not re_compiled_pattern.match(file_path)]

def get_regular_file_paths(folder_path: str = '.', re_pattern: str = r'^\d{4}-\d{2}__\d{3}\.pdf$') -> list[str]:
	folder_path = os.path.normpath(folder_path)
	re_compiled_pattern = re.compile(re_pattern)
	return [file_path for file_path in os.listdir(folder_path) if file_path.lower().endswith('.pdf') and re_compiled_pattern.match(file_path)]

def find_page(file_path, filter: str) -> int:
	try:
		with fitz.open(file_path) as file:
			for page_num in range(file.page_count):
				page = file[page_num].get_textpage()
				if filter in page.extractText():
					return page_num
		raise ValueError('Página não encontrada')
	except ValueError as e:
		logging.error(f'Erro ao abrir o arquivo "{file_path}": {e}')
		return -1
	
def get_words(words, limits) -> list[Word]:
	rect = fitz.Rect(*limits)
	words = [w for w in words if fitz.Rect((w.x0, w.y0, w.x1, w.y1)).intersects(rect)]
	return words

def rename_file(file_path: str, new_file_path: str):
	try:
		os.rename(file_path, new_file_path)
	except FileExistsError:
		logging.warning(f'Arquivo "{os.path.basename(file_path)}" já existe como "{os.path.basename(new_file_path)}".')
		os.remove(file_path)

def get_document_words(file_path: str, page: int=0) -> list[Word]:
	with fitz.open(file_path, filetype="pdf") as file:
		return [Word(*word) for word in file[page].get_textpage().extractWORDS()]