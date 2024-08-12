import pyperclip
import time

def count_elements(text):
    # テキストを行で分割
    rows = text.splitlines()
    # 行ごとにタブで分割し、すべてのセルをリストにする
    elements = [cell for row in rows for cell in row.split('\t')]
    return len(elements)

def main():
    last_text = ""
    print("クリップボードの内容を監視しています。終了するにはCtrl+Cを押してください。")
    
    while True:
        # クリップボードからテキストを取得
        current_text = pyperclip.paste()
        
        # 前回のテキストと異なる場合に出力
        if current_text != last_text:
            # 要素数をカウント
            num_elements = count_elements(current_text)
            print(f"クリップボードの内容: {current_text}")
            print(f"要素数: {num_elements}")
            last_text = current_text
        
        # 一定時間待機 (例: 1秒)
        time.sleep(1)

if __name__ == "__main__":
    main()
