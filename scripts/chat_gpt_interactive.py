"""インタラクティブに、GPTを試してみる"""

import os
import openai


def main():
    openai.api_key = os.environ["OPENAI_API_KEY"]
    amount_tokens = 0
    chat = []

    """
    setting = input("ChatGPTに設定を加えますか？ y/n\n")
    if setting == "y" or setting == "Y":
        content = input("内容を入力してください。\n")
        chat.append({"role": "system", "content": content})
    """
    content = """
        あなたは入力に対して適切なラベルを付与する抽出器です。
        単位のついた数値を入力します。数値の大小や範囲を考慮して、
        最も一致しているものを以下の候補の中から選んで教えてください。
        ただし、どれにも一致しないと判断したら、"No label"を返してください。
        解答する際は、解答の理由を述べた上で、解答例に従って出力してください。

        候補:
        ・〜100ml
        ・100ml〜150ml
        ・150ml〜
        ・3キログラム未満
        ・3キログラム以上5キログラム未満
        ・5キログラム以上
        ・~64GB
        ・64~128GB
        ・128~512GB
        ・512~1,000GB
        ・1T~

        解答例：
        ・120ml:
        120mlは100ml以上150ml未満です。
        response = {"label":"100ml〜150ml", "input":"120ml"}

        ・4kg:
        4kgは3kg以上5kg未満です。
        response = {"label":"3キログラム以上5キログラム未満", "input":"4kg"}

        ・20L:
        20Lは150ml以上です。
        response = {"label":"150ml〜", "input":"20L"}

        ・20,000mAh
        20,000mAhはどの候補にも該当しません。
        response = {"label":"No label", "input":"20,000mAh"}
    """
    chat.append({"role": "system", "content": content})

    print("チャットをはじめます。q または quit で終了します。")
    print("-"*50)
    while True:
        user = input("<あなた>\n")
        if user == "q" or user == "quit":
            print(f"トークン数は{amount_tokens}でした。")
            break
        else:
            chat.append({"role": "user", "content": user})

        print("<ChatGPT>")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat,
            temperature=0.2
        )
        msg = response["choices"][0]["message"]["content"].lstrip()
        amount_tokens += response["usage"]["total_tokens"]
        print(msg)
        chat.append({"role": "assistant", "content": msg})


if __name__ == "__main__":
    main()
