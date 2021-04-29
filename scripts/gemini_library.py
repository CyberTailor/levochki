#!/usr/bin/env python3
"""
Экспортирует библиотеку левочек из Notion.so в Gemini-капсулу.
"""

import re
import sys
from notion_readonly.client import NotionClient

METADATA = (
    ("metki", "Метки"),
    ("avtor_ka_redaktor_ka_sostavitel_nitsa", "Автор(ки)"),
    ("god_izdaniia", "Год издания"),
    ("tip_publikatsii", "Тип публикации"),
    ("iazyk", "Язык"),
)


def do_entry(item):
    link = google_drive_re.sub(
        r"https://drive.google.com/uc?export=download&id=\1",
        item.ssylka
    )

    yield f"=> {link} {item.nazvanie_knigi}"

    for prop, label in METADATA:
        data = item.get_property(prop)
        if not data:
            continue
        if isinstance(data, list):
            yield f"* {label}:\t" + ", ".join(data)
        elif isinstance(data, str):
            yield f"* {label}:\t" + data

    description = item.kratkoe_opisanie
    if description:
        yield "* Краткое описание"
        for line in description.split("\n"):
            yield f"> {line}"


if len(sys.argv) != 2:
    print("Использование: gemini_library.py <ссылка-на-библиотеку>")
    sys.exit(1)

google_drive_re = re.compile(r"https://drive.google.com/file/d/(\w+)/.*")

print("* Загружаю данные с Notion ...")
client = NotionClient()
page = client.get_block(sys.argv[1])
entries = page.collection.get_rows()
print("* Записываю файл library.gmi ...")
with open("library.gmi", "w") as dest:
    print("#", page.title, file=dest)
    print("Добро пожаловать в библиотеку!",
          "Здесь можно искать книжки по феминистской и левой теории.",
          end="\n\n", file=dest)
    for entry in entries:
        print("  + Записываю книгу", entry.title, "...")
        print(*do_entry(entry),
              sep="\n", end="\n\n", file=dest)

print("* Записано", len(entries), "книг")
