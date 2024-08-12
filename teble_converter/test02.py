import pyperclip

def reverse_clipboard_content():
    # クリップボードから内容を取得
    clipboard_content = pyperclip.paste()

    # 内容を逆に並び替え
    reversed_content = clipboard_content[::-1]

    # 逆に並び替えた内容をクリップボードに保存
    pyperclip.copy(reversed_content)
    print("クリップボードの内容が逆に並び替えられました。")
        
        

if __name__ == "__main__":
    reverse_clipboard_content()
