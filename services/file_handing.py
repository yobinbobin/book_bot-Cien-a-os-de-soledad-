import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    if len(text) - start < size:
        end_text = text[start:]
        return end_text, len(end_text)
    if text[start + size] in ',.!:;?' and text[start + size + 1] in ',.!:;?' and text[start + size - 1] in ',.!:;?':
        new_ps = size - 2
        end_text = text[start: start + new_ps]
    elif text[start + size] in ',.!:;?' and text[start + size+1] in ',.!:;?':
        end_text = text[start: start + size-1:]
    elif text[start + size] in ',.!:;?' and text[start + size-1] in ',.!:;?' and text[start + size-2] in ',.!:;?':
        end_text = text[start: start + size-3:]
    else:
        end_text = text[start: start + size:]
    last_symbol = end_text[-1]
    while last_symbol not in ',.!:;?':
        end_text = end_text[:-1]
        last_symbol = end_text[-1]
    return end_text, len(end_text)


def prepare_book(path: str) -> None:
    with open(file=path, mode='r', encoding='utf-8') as file:
        text = file.read()
    start, page_number = 0, 1
    while start < len(text):
        page_text, page_size = _get_part_text(text, start, PAGE_SIZE)
        start += page_size
        book[page_number] = page_text.strip()
        page_number += 1


prepare_book(os.path.join(sys.path[0],  os.path.normpath(BOOK_PATH)))