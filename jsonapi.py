import urllib.request
import json

# 1. 呼び出したいAPIのURL（今回はテスト用のユーザー情報API）
url = "https://jsonplaceholder.typicode.com/users/1"

try:
    # 2. APIにリクエストを送信してデータを取得
    with urllib.request.urlopen(url) as response:
        # 3. データを読み込んで文字コードを変換
        data = response.read().decode('utf-8')
        
        # 4. JSON文字列をPythonの辞書型データに変換
        user_info = json.loads(data)
        
        # 結果を表示
        print(f"ユーザー名: {user_info['name']}")
        print(f"メールアドレス: {user_info['email']}")
        print(f"所属都市: {user_info['address']['city']}")

except Exception as e:
    print(f"エラーが発生しました: {e}")
