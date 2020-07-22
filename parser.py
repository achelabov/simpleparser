import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup


def parse(response):
    global original_label, translate_label
    soup = BeautifulSoup(get_request(response), 'lxml')
    tags = soup.find_all('div', class_='string_container')

    original = []
    translated = []

    for tag in tags:
        original.append(
            {
                'original': tag.find('div', class_='original').text
            }
        )
        translated.append(
            {
                'translate': tag.find('div', class_='translate').text
            }
        )

    for i in range(len(original)):
        original[i] = original[i].get('original')
        translated[i] = translated[i].get('translate')

    original_label['text'] = ''.join(original)
    translate_label['text'] = ''.join(translated)


def get_request(response):
    return response.text


def get_text(event):
    global get_link_entry
    link = get_link_entry.get()

    try:
        response = requests.get(link)
    except:
        tk.messagebox.showerror(title='Error', message='Incorrect URL')
    else:
        get_request(response)
        parse(response)


def main():
    global root, get_link_entry, original_label, translate_label
    root = tk.Tk()

    original_frame = tk.LabelFrame(root, width=400, height=800, text='Original')
    translate_frame = tk.LabelFrame(root, width=400, height=800, text='Translated')

    get_link_frame = tk.LabelFrame(root, width=300, height=50, text='Link from amalgama-lab.com')

    original_label = tk.Label(original_frame, bg='white', width=40, height=40)
    translate_label = tk.Label(translate_frame, bg='white', width=40, height=40)

    get_link_entry = tk.Entry(get_link_frame, width=40)
    get_link_button = tk.Button(get_link_frame, width=10, height=1, text='click')

    get_link_button.bind('<Button-1>', get_text)

    original_label.pack(fill='both')
    translate_label.pack(fill='both')

    get_link_button.pack(side='right')
    get_link_entry.pack(side='left')

    get_link_frame.pack(side='bottom')
    original_frame.pack(side='left')
    translate_frame.pack(side='right')

    root.mainloop()


if __name__ == '__main__':
    main()
