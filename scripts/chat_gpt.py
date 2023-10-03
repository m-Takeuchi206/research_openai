"""ChatGPTをコード上で使ってみるスクリプト、メモ"""

import os
import openai

# APIキーの設定
openai.api_key = os.environ["OPENAI_API_KEY"]


print("----------")
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "大谷翔平について教えて"},
    ],
)
"""
>>> response
<OpenAIObject chat.completion id=chatcmpl-85WQONmrZxN0F4rMsHZbODQToWY1R at 0x1024f3cb0> JSON: {
  "id": "chatcmpl-85WQONmrZxN0F4rMsHZbODQToWY1R",
  "object": "chat.completion",
  "created": 1696326972,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": ~~sentence~~
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 22,
    "completion_tokens": 603,
    "total_tokens": 625
  }
}
"""
result_1 = response.choices[0]["message"]["content"].strip()
print(result_1)

print("----------")
response_2 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "OpenAIのAPIであるopenai.ChatCompletion.createについて、リクエスト、レスポンスの詳細を教えて"},
    ],
)
print(response_2)
"""
{
  "id": "chatcmpl-85WcI5vvK60v1246pCwEPXPgeQcbl",
  "object": "chat.completion",
  "created": 1696327710,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": ~~sentence~~
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 44,
    "completion_tokens": 638,
    "total_tokens": 682
  }
}
"""
result_2 = response_2.choices[0]["message"]["content"].strip()
print(result_2)
"""
openai.ChatCompletion.createは、OpenAIのチャットベースの言語モデルを使って、対話の続きを生成するためのAPIメソッドです。

リクエストの詳細：
- `messages`（必須）: チャットの履歴を表すリストオブジェクトです。各メッセージはユーザーまたはAIアシスタントによって作成され、`role`と`content`を持ちます。`role`は「system」、「user」、または「assistant」のいずれかの値を取ります。最初のメッセージは「system」でなければなりません。例えば、`{"role": "system", "content": "You are a helpful assistant."}`のようになります。

- `model`（必須）: 使用する言語モデルのIDです。例えば、"gpt-3.5-turbo"を指定します。

- `temperature`（オプション）: モデルの出力の多様性を制御するためのパラメータです。値が高いとよりランダムな応答が生成され、値が低いとより決定論的な応答が生成されます。デフォルト値は0.6です。

- `max_tokens`（オプション）: 応答の長さを制限するために使用されるトークンの最大数です。デフォルト値は50です。

応答の詳細：
- `id`: リクエストの一意のIDです。

- `object`: 要求の種類（この場合は「chat.completion」）です。

- `created`: リクエストが作成された日時です。

- `model`: 使用された言語モデルのIDです。

- `usage`: 応答のトークン数とストリーム数のリストです。

- `choices`: モデルによって生成された応答のリストです。各応答は`message`と`finish_reason`を含みます。`message`には、AIアシスタントの発言内容が含まれます。`finish_reason`には、生成の終了理由が含まれます。

以上がopenai.ChatCompletion.createメソッドのリクエストとレスポンスの詳細になります。
"""

print("----------")
response_3 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "大谷翔平について教えて"},
        {"role": "assistant", "content": result_1}, 
        {"role": "user", "content": "具体的な記録は？"},
    ],
)
print(response_3)
"""
{
  "id": "chatcmpl-85WojftgicFYEDg1n6tOIhANSqovP",
  "object": "chat.completion",
  "created": 1696328481,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": ~~sentence~~,
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 619,
    "completion_tokens": 399,
    "total_tokens": 1018
  }
}
"""
result_3 = response_3.choices[0]["message"]["content"].strip()
print(result_3)
"""
大谷翔平の具体的な記録は以下の通りです。

- 2013年：新人王受賞、最多勝利（15勝）
- 2014年：最多勝利（11勝）
- 2016年：最多勝利（23勝）
- 2016年：最優秀防御率（1.86）、最多奪三振（174個）
- 2018年：MLBオールスターゲームに出場
- 2018年：MLB新人王投票で2位
- 2021年：メジャーリーグベースボール (MLB)オールスターゲームに出場
- 2021年：初のシルバースラッガー賞を受賞（投手）
- 2021年：最多試合連続本塁打記録更新（8試合連続本塁打）
- 2021年：50本塁打以上・10勝以上を達成した初の選手となる（MLB史上初の達成）

また、大谷は通算でアメリカンリーグの選手として、1試合18三振を記録するなど、数々の個人記録を持っています。彼の実績は日本のプロ野球界やメジャーリーグでも非常に注目されており、野球ファンから高く評価されています。
"""
