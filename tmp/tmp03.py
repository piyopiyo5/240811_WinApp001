def read_values_from_file(filename, key, values_container):
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



if 0:
    data = {
    'Name': 'John Doe',
    'Age': 30,
    'Occupation': 'Software Developer'
    }   
    with open('data.txt', 'w') as file:
        for key, value in data.items():
            file.write(f"{key}:{value}\n")
            
else:
    filename = 'data.txt'
    key_to_find = 'Age'
    value_container = []  # 値を格納するためのリスト

    result = read_values_from_file(filename, key_to_find, value_container)

    if result > 0:
        print(f"Key '{key_to_find}' found {result} values")
        print("found list:")
        for i in range(result):
            print(f"  {value_container[i]}")
    else:
        print(f"Key '{key_to_find}' not found.")







