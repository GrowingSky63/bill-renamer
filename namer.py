import os, logging
from util import (
  get_irregular_file_paths,
  get_document_words,
  get_words,
  find_page,
  rename_file,
  MONTHS
)

def fix_path(file_path: str, code_rect: tuple[float, float, float, float], ref_month_rect: tuple[float, float, float, float], page_num = 0):
  if page_num < 0:
    return file_path
  words = get_document_words(file_path, page=page_num)
  raw_code = get_words(words, code_rect)[0].text.split('-')[0]
  raw_date = ''.join([word.text for word in get_words(words, ref_month_rect)])
  raw_month, year = raw_date.split('/')
  if not raw_month.isnumeric():
    raw_month = MONTHS[raw_month.lower()]
  file_name = f'{year}-{int(raw_month):0>2}__{raw_code[-3:]}.pdf'
  return os.path.join(os.path.dirname(file_path), file_name)

def main(search_paths: list[str], code_rect: tuple[float, float, float, float], ref_month_rect: tuple[float, float, float, float], page_filter: str | None = None):
  for folder in search_paths:
    if os.path.exists(folder) and os.path.isdir(folder):
      for file_path in get_irregular_file_paths(folder):
        file_path = os.path.join(folder, file_path)
        logging.info(f'Analizando "{os.path.basename(file_path)}"...')
        page = 0
        if page_filter:
          page = find_page(file_path, page_filter)
        new_file_path = fix_path(
          file_path,
          code_rect,
          ref_month_rect,
          page
        )
        rename_file(file_path, new_file_path)
        logging.info(f'Arquivo "{os.path.basename(file_path)}" renomeado para "{os.path.basename(new_file_path)}".')