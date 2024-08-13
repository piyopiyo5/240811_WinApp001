def readValuesFromDictionary(filename, key, values_container):
    """
    指定されたファイルからキーに対応するすべての値を読み取ります。

    Args:
    - filename: 読み取るテキストファイル名
    - key: 検索するキー
    - values_container: キーに対応する値を格納するリスト（空で初期化）

    Returns:
    - int: 見つかったキーの数
    """
    found_count = 0
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        file_key, file_value = line.split(':', 1)
                        if file_key == key:
                            values_container.append(file_value)
                            found_count += 1
                    except ValueError:
                        # 行が 'key:value' フォーマットでない場合はスキップ
                        continue
        return found_count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0
    
def readValueFromDictionary(filename, key, buffer_list):
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        file_key, file_value = line.split(':', 1)
                        if file_key == key:
                            buffer_list.append(file_value)
                            return 1
                    except ValueError:
                        # 行が 'key:value' フォーマットでない場合はスキップ
                        continue
        return 0
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0
    
    
def writeValueToDictionary(filename, key, value):
    with open(filename, 'a') as file:
        file.write("\n" + key + ":" + value)