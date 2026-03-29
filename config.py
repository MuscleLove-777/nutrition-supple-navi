"""栄養＆サプリナビ - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "栄養＆サプリナビ"
BLOG_DESCRIPTION = "プロテイン・サプリメント・食事管理の完全ガイドブログ"
BLOG_URL = "https://musclelove-777.github.io/nutrition-supple-navi"
BLOG_LANGUAGE = "ja"
GITHUB_REPO = "MuscleLove-777/nutrition-supple-navi"

TARGET_CATEGORIES = [
    "プロテイン徹底比較",
    "サプリメント科学",
    "筋トレ食事術",
    "栄養素の基礎知識",
    "ミールプレップ・レシピ",
]

THEME = {
    "primary": "#16a34a",
    "accent": "#84cc16",
    "gradient_start": "#16a34a",
    "gradient_end": "#059669",
    "dark_bg": "#0a1a0f",
    "dark_surface": "#152d1a",
    "light_bg": "#f0fdf4",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 2500
ARTICLES_PER_DAY = 2
SCHEDULE_HOURS = [8, 20]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 70
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "プロテイン": [
        {"service": "マイプロテイン", "url": "https://www.myprotein.jp", "description": "高品質ホエイプロテイン"},
        {"service": "Amazon プロテイン", "url": "https://www.amazon.co.jp", "description": "プロテイン各種比較"},
        {"service": "楽天市場 プロテイン", "url": "https://www.rakuten.co.jp", "description": "プロテインお得セット"},
    ],
    "サプリメント": [
        {"service": "iHerb", "url": "https://www.iherb.com", "description": "海外サプリメント通販"},
        {"service": "Amazon サプリ", "url": "https://www.amazon.co.jp", "description": "サプリメント各種"},
    ],
    "食事管理": [
        {"service": "マッスルデリ", "url": "https://muscledeli.co.jp", "description": "筋トレ向け宅配弁当"},
        {"service": "Amazon 調理器具", "url": "https://www.amazon.co.jp", "description": "ミールプレップ用品"},
    ],
    "書籍": [
        {"service": "Amazon", "url": "https://www.amazon.co.jp", "description": "栄養学・食事管理の書籍"},
        {"service": "楽天ブックス", "url": "https://books.rakuten.co.jp", "description": "スポーツ栄養学書籍"},
    ],
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
DASHBOARD_PORT = 8080
