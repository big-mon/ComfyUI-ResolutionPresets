## ComfyUI カスタムノード開発方針: ResolutionPresets

**1. プロジェクト概要**

- **プロジェクト名:** `ComfyUI-ResolutionPresets`
- **目的:** ComfyUI ワークフロー内で、特に SDXL (Stable Diffusion XL) で推奨される画像解像度をドロップダウンリストから簡単に選択し、その `width` と `height` の値を他のノード (例: Empty Latent Image) に渡せるようにする。
- **ターゲット:** まずは SDXL の推奨解像度プリセットに特化して実装する。将来的には他のモデルやカスタムプリセットへの拡張も視野に入れるが、初期実装では SDXL のみを対象とする。
- **成果物:** ComfyUI にインストール可能なカスタムノードパッケージ。

**2. 開発言語・環境**

- **言語:** Python 3.x
- **フレームワーク/ライブラリ:** ComfyUI カスタムノード API
- **実行環境:** ComfyUI が動作する Python 環境

**3. 機能要件**

- **3.1. ノード仕様:**
  - **ノードクラス名 (Python):** `ResolutionPresetsSDXL`
  - **ノード内部名 (識別子):** `ResolutionPresetsSDXL`
  - **ノード表示名 (UI):** `Resolution Presets (SDXL)`
  - **ノードカテゴリ (UI):** `utils/presets` (他の適切なカテゴリでも可)
- **3.2. 入力:**
  - **UI 入力:**
    - 名称: `preset`
    - タイプ: ドロップダウンリスト (ComfyUI の `INPUT_TYPES` における文字列リスト指定)
    - 選択肢: SDXL の推奨解像度とアスペクト比を組み合わせた文字列リスト。
      - 例: `"1024x1024 (1:1)"`, `"1152x896 (9:7)"`, `"896x1152 (7:9)"`, etc.
      - 初期リストには、一般的な SDXL 推奨解像度を網羅する (最低 5-10 種類程度)。
- **3.3. 出力:**
  - **出力 1:**
    - 名称: `width`
    - タイプ: 整数 (`INT`)
    - 内容: 選択されたプリセットに対応する画像の幅。
  - **出力 2:**
    - 名称: `height`
    - タイプ: 整数 (`INT`)
    - 内容: 選択されたプリセットに対応する画像の高さ。
- **3.4. 処理ロジック:**
  - ドロップダウンで選択された `preset` 文字列 (例: `"1024x1024 (1:1)"`) を受け取る。
  - 文字列の先頭部分にある解像度表記 (`"1024x1024"`) を抽出する。
  - 抽出した文字列を `'x'` で分割し、幅 (`"1024"`) と高さ (`"1024"`) の文字列を取得する。
  - 取得した幅と高さの文字列をそれぞれ整数 (`int`) に変換する。
  - 変換後の `width` と `height` の整数値をタプル `(width, height)` として返す。
- **3.5. エラーハンドリング:**
  - `preset` 文字列の解析（分割、整数変換）に失敗した場合:
    - コンソールにエラーメッセージを出力する (どのプリセットで、どのようなエラーが発生したか)。
    - 処理を中断せず、デフォルトの解像度 (例: `width=1024`, `height=1024`) を返す。

**4. ファイル構成**

ComfyUI-ResolutionPresets/ # リポジトリルート (カスタムノードディレクトリ)
├── init.py # ノード登録用ファイル
├── resolution_presets.py # ノードクラスとロジック実装ファイル
└── README.md # (任意) 説明、インストール、使用方法

**5. 実装ステップ (AI エージェント向け指示)**

- **ステップ 1: ファイル準備**
  - `ComfyUI-ResolutionPresets` ディレクトリを作成してください。
  - その中に、`__init__.py` と `resolution_presets.py` という名前の 2 つの空の Python ファイルを作成してください。
- **ステップ 2: 解像度リスト定義 (`resolution_presets.py`)**
  - `resolution_presets.py` ファイルを開いてください。
  - `SDXL_RESOLUTIONS` という名前の Python リストを定義してください。
  - このリストには、SDXL の推奨解像度を示す文字列を追加してください。各文字列の形式は `"WxH (Aspect Ratio)"` (例: `"1024x1024 (1:1)"`) としてください。最低でも以下の解像度を含めてください:
    - `"1024x1024 (1:1)"`
    - `"1152x896 (9:7)"`
    - `"896x1152 (7:9)"`
    - `"1216x832 (19:12)"`
    - `"832x1216 (12:19)"`
    - `"1344x768 (7:4)"`
    - `"768x1344 (4:7)"`
    - `"1536x640 (12:5)"`
    - `"640x1536 (5:12)"`
- **ステップ 3: ノードクラス作成 (`resolution_presets.py`)**
  - `ResolutionPresetsSDXL` という名前の Python クラスを作成してください。
  - クラス内に以下のクラス変数を定義してください:
    - `NODE_NAME = "ResolutionPresetsSDXL"`
    - `NODE_DISPLAY_NAME = "Resolution Presets (SDXL)"`
    - `CATEGORY = "utils/presets"`
- **ステップ 4: 入力定義 (`resolution_presets.py`)**
  - `ResolutionPresetsSDXL` クラス内に `INPUT_TYPES` という名前のクラスメソッド (`@classmethod`) を定義してください。
  - このメソッドは、以下の構造を持つ辞書を `return` するように実装してください:
    ```python
    {
        "required": {
            "preset": (SDXL_RESOLUTIONS, ) # ステップ2で定義したリスト
        }
    }
    ```
- **ステップ 5: 出力定義 (`resolution_presets.py`)**
  - `ResolutionPresetsSDXL` クラス内に以下のクラス変数を定義してください:
    - `RETURN_TYPES = ("INT", "INT")`
    - `RETURN_NAMES = ("width", "height")`
- **ステップ 6: 処理関数定義 (`resolution_presets.py`)**
  - `ResolutionPresetsSDXL` クラス内に `FUNCTION = "get_resolution"` というクラス変数を定義してください。
  - `get_resolution` という名前のインスタンスメソッドを定義してください。このメソッドは `self` と `preset` (選択された文字列) を引数に取ります。
  - `get_resolution` メソッド内に以下の処理を実装してください:
    1.  `try-except` ブロックを使用してください。
    2.  `try` ブロック内:
        - `preset` 文字列から最初のスペース (`" "`) までを抽出し、解像度部分 (`"WxH"`) を取得してください。
        - 取得した文字列を `'x'` で分割して、`width_str` と `height_str` を取得してください。
        - `width_str` と `height_str` を `int()` を使って整数に変換し、`width` と `height` 変数に代入してください。
        - `return (width, height)` で結果を返してください。
    3.  `except Exception as e:` ブロック内:
        - `print()` 文を使って、エラーが発生したこと、エラー内容 (`e`)、およびどの `preset` で発生したかを示すメッセージをコンソールに出力してください (例: `f"[ResolutionPresetsSDXL] Error parsing preset: {preset}. Error: {e}"`)。
        - `print()` 文を使って、デフォルト値を返すことを示すメッセージを出力してください (例: `"[ResolutionPresetsSDXL] Returning default 1024x1024."`)。
        - `return (1024, 1024)` でデフォルト値を返してください。
- **ステップ 7: ノード登録 (`__init__.py`)**
  - `__init__.py` ファイルを開いてください。
  - `from .resolution_presets import ResolutionPresetsSDXL` を記述して、作成したクラスをインポートしてください。
  - `NODE_CLASS_MAPPINGS` という名前の辞書を定義し、`{"ResolutionPresetsSDXL": ResolutionPresetsSDXL}` という内容を設定してください。
  - `NODE_DISPLAY_NAME_MAPPINGS` という名前の辞書を定義し、`{"ResolutionPresetsSDXL": "Resolution Presets (SDXL)"}` という内容を設定してください (クラスの `NODE_DISPLAY_NAME` を参照しても良いです)。
  - (任意) `print("### Loading: ComfyUI-ResolutionPresets ###")` を追加して、ロード時にメッセージが表示されるようにしてください。
- **ステップ 8: README 作成 (任意)**
  - `README.md` ファイルを作成し、以下の内容を記述してください:
    - ノードの簡単な説明 (SDXL 推奨解像度を選択できること)。
    - インストール方法 (`custom_nodes` にクローンまたは配置する方法)。
    - 基本的な使い方 (ノードを追加し、出力を Latent ノードなどに接続する例)。
- **ステップ 9: コードレビューとテスト準備**
  - 実装されたコード全体を確認し、誤りや改善点がないかチェックしてください。
  - 実装された `ComfyUI-ResolutionPresets` ディレクトリを ComfyUI の `custom_nodes` ディレクトリに配置し、ComfyUI を再起動してテストできる状態にしてください。

**6. テスト項目**

- ComfyUI 起動時にエラーなくカスタムノードが読み込まれること。
- ノード追加メニューの指定したカテゴリ (`utils/presets`) に `Resolution Presets (SDXL)` が表示されること。
- ノードをワークフローに追加できること。
- ドロップダウンリストに `SDXL_RESOLUTIONS` で定義した選択肢が表示されること。
- 各プリセットを選択した際に、`width` および `height` 出力から正しい整数値が出力されること (Primitive ノードや他のノードに接続して確認)。
- `Empty Latent Image` ノードの `width`, `height` に接続し、期待通りの解像度が設定されること。
- (意図的に不正なプリセット文字列を追加するなどして) エラーハンドリングが機能し、コンソールにエラーメッセージが表示され、デフォルト値 (1024, 1024) が出力されること。
