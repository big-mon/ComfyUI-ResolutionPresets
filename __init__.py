"""ComfyUI用のSDXL推奨解像度プリセットノード"""

# ロード時の通知メッセージ
print("### Loading: ComfyUI-ResolutionPresets ###")

# ノードクラスのインポート
from .resolution_presets import ResolutionPresetsSDXL

# ノードの登録
NODE_CLASS_MAPPINGS = {
    "ResolutionPresetsSDXL": ResolutionPresetsSDXL
}

# ノード表示名の登録
NODE_DISPLAY_NAME_MAPPINGS = {
    "ResolutionPresetsSDXL": "Resolution Presets (SDXL)"
}
