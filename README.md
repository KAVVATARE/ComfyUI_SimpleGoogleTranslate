ComfyUI-SimpleGoogleTranslate

A lightweight text-translation node for ComfyUI.
It provides an easy way to translate any text inside your workflow using Google Translate (googletrans).
Useful for prompt translation, multilingual workflows, script generation, and automations.

✨ Features

Translate text directly inside ComfyUI

Supports all languages available in googletrans

Automatic source language detection (auto)

Very small & fast — no API keys, no external setup

Ideal for:

translating prompts

converting captions into another language

combining with text-processing nodes

workflows that require multilingual output

📦 Installation

Clone this repository into your ComfyUI custom_nodes directory:

cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/ComfyUI-SimpleGoogleTranslate.git


Install dependency:

pip install googletrans==4.0.0-rc1


Restart ComfyUI.

🧩 Node Description
Simple Google Translate Text
Input	Type	Description
source_lang	dropdown	Input language (or "auto" for auto-detect)
target_lang	dropdown	Translation language
text	STRING	Text to translate

Output:

Output	Type	Description
translated	STRING	Translated result
📁 Repository Structure
ComfyUI-SimpleGoogleTranslate/
│
├── simple_google_translate.py
├── __init__.py
├── requirements.txt
└── README.md

📝 Requirements

ComfyUI

googletrans==4.0.0-rc1

✔️ Notes

googletrans は API キー不要で使えますが、Google 側の仕様変更により一時的に不安定になることがあります。その場合は再試行してください。

ノードは utils/Text カテゴリに追加されます。

📸 Example

（あなたが貼ってくれたスクショのように、翻訳前後を Show Text でつなげた画像を残せます。）

👍 License

Free to use, modify, and include in any workflow.

Happy translating!
