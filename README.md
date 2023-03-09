# my-simple-rsa.py

🦢🦢🦢 RSA暗号をPythyonで実装してみた！  

## 実行方法

```shell
pip install -r requirements.txt
```

```shell
python ./main.py --prime1 素数A --prime2 素数B --message メッセージ
python ./main.py --prime1 11 --prime2 13 --message "Hello World!!!"
```

## 実行結果

```shell
公開鍵: (143, 65537)
秘密鍵: (143, 53)
元のメッセージ: Hello World!!!
暗号化されたメッセージ: 0000063000009500001140000114000008900001370000085000001600001200000089000008200001140000133000013700000850000069000013700000850000069000013700000850000069
復号化されたメッセージ: Hello World!!!
```

---

以下のコマンドでテストを実行できます。  

```shell
pytest
```
