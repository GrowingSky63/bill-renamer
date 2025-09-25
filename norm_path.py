import os, logging
from util import (
  get_irregular_file_paths,
  get_document_words,
  get_words,
  find_page,
  rename_file,
  get_numeric_month
)

def fix_path(
  file_path: str,
  code_rect: tuple[float, float, float, float],
  ref_month_rect: tuple[float, float, float, float],
  page_num = 0,
  code_regex: str | None = None,
  ref_month_regex: str | None = None
):
  if page_num < 0:
    return file_path
  words = get_document_words(file_path, page=page_num)
  raw_code = get_words(words, code_rect, code_regex)[-1].text.split('-')[0]
  raw_date = ''.join([word.text for word in get_words(words, ref_month_rect, ref_month_regex)])
  raw_month, year = raw_date.split('/')
  if not raw_month.isnumeric():
    raw_month = get_numeric_month(raw_month)
  file_name = f'{year}-{int(raw_month):0>2}__{raw_code[-3:]}.pdf'
  return os.path.join(os.path.dirname(file_path), file_name)

def normalize_file_path(
    file_path: str,
    code_rect: tuple[float, float, float, float],
    ref_month_rect: tuple[float, float, float, float],
    page_filter: str | None = None,
    code_regex: str | None = None,
    ref_month_regex: str | None = None
):
  try:
    logging.info(f'Analizando "{os.path.basename(file_path)}"...')
    page = 0
    if page_filter:
      page = find_page(file_path, page_filter)
    new_file_path = fix_path(
      file_path,
      code_rect,
      ref_month_rect,
      page,
      code_regex,
      ref_month_regex
    )
    rename_file(file_path, new_file_path)
    logging.info(f'Arquivo "{os.path.basename(file_path)}" renomeado para "{os.path.basename(new_file_path)}".')
  except Exception as e:
    logging.error(f'Erro ao renomear arquivo "{os.path.basename(file_path)}": {e}')

def normalize_file_paths_from_folder(
  folder: str,
  code_rect: tuple[float, float, float, float],
  ref_month_rect: tuple[float, float, float, float],
  page_filter: str | None = None,
  code_regex: str | None = None,
  ref_month_regex: str | None = None
):
  if not os.path.exists(folder) or not os.path.isdir(folder):
    raise ValueError(f"O caminho '{folder}' deve ser um diretório válido e existente.") 

  for file in get_irregular_file_paths(folder):
    normalize_file_path(
      os.path.join(folder, file),
      code_rect,
      ref_month_rect,
      page_filter,
      code_regex,
      ref_month_regex
    )
