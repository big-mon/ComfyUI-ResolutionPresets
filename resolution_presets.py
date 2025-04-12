# SDXL推奨解像度のリスト定義
SDXL_RESOLUTIONS = [
    "1024x1024 (1:1)",   # 正方形
    "1152x896 (9:7)",    # 横長
    "896x1152 (7:9)",    # 縦長
    "1216x832 (19:12)",  # 横長
    "832x1216 (12:19)",  # 縦長
    "1344x768 (7:4)",    # 横長
    "768x1344 (4:7)",    # 縦長
    "1536x640 (12:5)",   # パノラマ横長
    "640x1536 (5:12)",   # パノラマ縦長
]


class ResolutionPresetsSDXL:
    """SDXL推奨解像度のプリセットを提供するノード"""
    
    # ノードの基本情報
    NODE_NAME = "ResolutionPresetsSDXL"
    NODE_DISPLAY_NAME = "Resolution Presets (SDXL)"
    CATEGORY = "utils/presets"
    
    # 出力の定義
    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    
    # 処理関数の指定
    FUNCTION = "get_resolution"
    
    @classmethod
    def INPUT_TYPES(cls):
        """入力タイプの定義
        
        Returns:
            dict: 必須入力としてSDXL_RESOLUTIONSリストから選択可能なpresetを定義
        """
        return {
            "required": {
                "preset": (SDXL_RESOLUTIONS,)
            }
        }
    
    def get_resolution(self, preset: str) -> tuple[int, int]:
        """プリセット文字列から解像度を抽出する
        
        Args:
            preset (str): 解像度プリセット文字列 (e.g., "1024x1024 (1:1)")
        
        Returns:
            tuple[int, int]: 幅と高さのタプル (width, height)
        """
        try:
            # プリセット文字列から解像度部分を抽出
            resolution = preset.split(" ")[0]
            
            # 幅と高さを分割して取得
            width_str, height_str = resolution.split("x")
            
            # 整数に変換
            width = int(width_str)
            height = int(height_str)
            
            return (width, height)
            
        except Exception as e:
            # エラー発生時の処理
            print(f"[ResolutionPresetsSDXL] Error parsing preset: {preset}. Error: {e}")
            print("[ResolutionPresetsSDXL] Returning default 1024x1024.")
            return (1024, 1024)
