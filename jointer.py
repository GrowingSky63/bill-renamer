import os, fitz, logging
from util import (
	get_irregular_file_paths,
	get_regular_file_paths,
	get_document_words,
	get_words
)
# =)

def get_base_file_path(file_path: str, code_rect: tuple[float, float, float, float], ref_month_rect: tuple[float, float, float, float]) -> str:
	words = get_document_words(file_path)
	code_words = get_words(words, code_rect)
	ref_month_words = get_words(words, ref_month_rect)
	if code_words and ref_month_words:
		code = code_words[0].text
		ref_month = ref_month_words[0].text.split('/')
		ref_month.reverse()
		return f"{'-'.join(ref_month)}__{code[-3:]}.pdf"
	return ''

def join_documents(file_path: str, base_file_path: str):
	with fitz.open(file_path) as gedisa_file, fitz.open(base_file_path) as copel_file:
		merged_document = fitz.open()
		for page_num in range(gedisa_file.page_count):
			merged_document.insert_pdf(gedisa_file, from_page=page_num, to_page=page_num)
		for page_num in range(copel_file.page_count):
			merged_document.insert_pdf(copel_file, from_page=page_num, to_page=page_num)
	merged_document.save(base_file_path)

def main(search_paths: list[str], code_rect: tuple[float, float, float, float], ref_month_rect: tuple[float, float, float, float]):
	for folder in search_paths:
		if os.path.exists(folder) and os.path.isdir(folder):
			regular_files = get_regular_file_paths(folder)
			for file_path in get_irregular_file_paths(folder):
				file_path = os.path.join(folder, file_path)
				base_file_path = get_base_file_path(file_path, code_rect, ref_month_rect)
				if base_file_path and base_file_path in regular_files:
					join_documents(file_path, os.path.join(folder, base_file_path))
					os.remove(file_path)
					logging.info(f'Arquivo "{os.path.basename(file_path)}" concatenado à "{os.path.basename(base_file_path)}".')
