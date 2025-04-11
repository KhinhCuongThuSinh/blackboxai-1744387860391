import os
from dotenv import load_dotenv

# Load biến môi trường từ file .env
load_dotenv()

# Cấu hình Bot
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
if not TELEGRAM_TOKEN:
    raise ValueError("Không tìm thấy TELEGRAM_TOKEN trong biến môi trường!")

# Danh sách ID của admin (có thể thêm nhiều ID)
ADMIN_IDS = [int(id) for id in os.getenv('ADMIN_IDS', '').split(',') if id]

# API Keys cho các dịch vụ
LEGAL_API_KEY = os.getenv('LEGAL_API_KEY')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

# Cấu hình logging
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE = os.getenv('LOG_FILE', 'bot.log')

# Cấu hình Web Server cho Dashboard
WEB_HOST = os.getenv('WEB_HOST', '0.0.0.0')
WEB_PORT = int(os.getenv('WEB_PORT', 8000))
DEBUG_MODE = os.getenv('DEBUG_MODE', 'False').lower() == 'true'

# Cấu hình Database (nếu cần)
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = int(os.getenv('DB_PORT', 5432))
DB_NAME = os.getenv('DB_NAME', 'legal_bot')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')

# Cấu hình API
API_TIMEOUT = int(os.getenv('API_TIMEOUT', 10))  # seconds
API_MAX_RETRIES = int(os.getenv('API_MAX_RETRIES', 3))

# Cấu hình Cache
CACHE_ENABLED = os.getenv('CACHE_ENABLED', 'True').lower() == 'true'
CACHE_TTL = int(os.getenv('CACHE_TTL', 3600))  # seconds

# Giới hạn request
RATE_LIMIT = int(os.getenv('RATE_LIMIT', 60))  # requests per minute
MAX_CONNECTIONS = int(os.getenv('MAX_CONNECTIONS', 100))

# Cấu hình tìm kiếm
SEARCH_RESULT_LIMIT = int(os.getenv('SEARCH_RESULT_LIMIT', 10))
MIN_SEARCH_LENGTH = int(os.getenv('MIN_SEARCH_LENGTH', 3))

# Cấu hình tin nhắn
MAX_MESSAGE_LENGTH = 4096  # Telegram message limit
DEFAULT_LANGUAGE = os.getenv('DEFAULT_LANGUAGE', 'vi')

# URLs và Endpoints
LEGAL_API_URL = os.getenv('LEGAL_API_URL', 'https://api.legal-service.com/v1')
NEWS_API_URL = os.getenv('NEWS_API_URL', 'https://api.news-service.com/v1')

# Danh sách nguồn tin tức được phép
ALLOWED_NEWS_SOURCES = os.getenv('ALLOWED_NEWS_SOURCES', 'source1,source2').split(',')

# Cấu hình bảo mật
ENABLE_SSL = os.getenv('ENABLE_SSL', 'True').lower() == 'true'
SSL_CERT_PATH = os.getenv('SSL_CERT_PATH', '')
SSL_KEY_PATH = os.getenv('SSL_KEY_PATH', '')

# Kiểm tra cấu hình bắt buộc
def validate_config():
    """Kiểm tra các cấu hình bắt buộc"""
    required_vars = [
        ('TELEGRAM_TOKEN', TELEGRAM_TOKEN),
        ('LEGAL_API_KEY', LEGAL_API_KEY),
        ('NEWS_API_KEY', NEWS_API_KEY)
    ]
    
    missing_vars = [var[0] for var in required_vars if not var[1]]
    
    if missing_vars:
        raise ValueError(
            f"Thiếu các biến môi trường bắt buộc: {', '.join(missing_vars)}"
        )
    
    if not ADMIN_IDS:
        raise ValueError("Cần có ít nhất một ADMIN_ID!")

# Thực hiện kiểm tra khi import module
validate_config()
