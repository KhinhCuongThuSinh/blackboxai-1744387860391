from typing import Optional, List, Dict
import re
from ..utils.logger import logger

class InputValidator:
    """Kiểm tra và xác thực dữ liệu đầu vào"""
    
    @staticmethod
    def validate_search_keyword(keyword: str) -> bool:
        """Kiểm tra từ khóa tìm kiếm"""
        if not keyword or len(keyword.strip()) < 2:
            return False
        # Kiểm tra ký tự đặc biệt
        if re.search(r'[<>{}[\]\\]', keyword):
            return False
        return True

    @staticmethod
    def validate_term(term: str) -> bool:
        """Kiểm tra thuật ngữ"""
        if not term or len(term.strip()) < 2:
            return False
        # Chỉ cho phép chữ cái, số và dấu cách
        if not re.match(r'^[\w\s]+$', term):
            return False
        return True

    @staticmethod
    def validate_date(date_str: str) -> bool:
        """Kiểm tra định dạng ngày"""
        try:
            # Kiểm tra định dạng YYYY-MM-DD
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
                return False
            return True
        except Exception:
            return False

    @staticmethod
    def sanitize_input(text: str) -> str:
        """Làm sạch dữ liệu đầu vào"""
        # Loại bỏ ký tự đặc biệt
        text = re.sub(r'[<>{}[\]\\]', '', text)
        # Chuẩn hóa khoảng trắng
        text = ' '.join(text.split())
        return text

    @staticmethod
    def validate_document_data(doc: Dict) -> bool:
        """Kiểm tra dữ liệu văn bản"""
        required_fields = ['title', 'code', 'issue_date', 'url']
        return all(field in doc for field in required_fields)

    @staticmethod
    def validate_news_data(article: Dict) -> bool:
        """Kiểm tra dữ liệu tin tức"""
        required_fields = ['title', 'publish_date', 'description', 'url']
        return all(field in article for field in required_fields)

    @staticmethod
    def validate_term_data(term_data: Dict) -> bool:
        """Kiểm tra dữ liệu thuật ngữ"""
        required_fields = ['term', 'definition']
        return all(field in term_data for field in required_fields)

    @staticmethod
    def validate_api_response(response: Dict) -> bool:
        """Kiểm tra response từ API"""
        if not isinstance(response, dict):
            return False
        if 'status' not in response:
            return False
        return True

    @staticmethod
    def log_validation_error(error_type: str, data: any) -> None:
        """Ghi log lỗi validation"""
        logger.error(f"Validation error - {error_type}: {str(data)}")

class RateLimiter:
    """Kiểm soát tần suất request"""
    
    def __init__(self, max_requests: int = 60, time_window: int = 60):
        self.max_requests = max_requests  # Số request tối đa
        self.time_window = time_window    # Thời gian (giây)
        self.requests = []                # Danh sách thời gian request
        
    def can_make_request(self, user_id: int) -> bool:
        """Kiểm tra có thể thực hiện request"""
        import time
        current_time = time.time()
        
        # Xóa các request cũ
        self.requests = [req for req in self.requests 
                        if current_time - req['timestamp'] < self.time_window]
        
        # Đếm số request của user
        user_requests = len([req for req in self.requests 
                           if req['user_id'] == user_id])
        
        if user_requests >= self.max_requests:
            return False
            
        self.requests.append({
            'user_id': user_id,
            'timestamp': current_time
        })
        return True
