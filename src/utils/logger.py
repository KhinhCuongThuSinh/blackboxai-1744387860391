import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import os
from datetime import datetime
from config import LOG_LEVEL, LOG_FILE

def setup_logger(name='legal_bot'):
    """
    Thiết lập và cấu hình logger cho bot pháp lý
    
    Args:
        name (str): Tên của logger
        
    Returns:
        logging.Logger: Logger đã được cấu hình
    """
    
    # Tạo thư mục logs nếu chưa tồn tại
    log_dir = os.path.dirname(LOG_FILE)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Tạo logger
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, LOG_LEVEL))

    # Định dạng log
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - [%(levelname)s] - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Handler cho console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    try:
        # Handler cho file log chính - giới hạn kích thước
        file_handler = RotatingFileHandler(
            LOG_FILE,
            maxBytes=10 * 1024 * 1024,  # 10MB
            backupCount=5,
            encoding='utf-8'
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Handler cho file log theo ngày - tự động xoay vòng mỗi ngày
        daily_handler = TimedRotatingFileHandler(
            LOG_FILE.replace('.log', '_daily.log'),
            when='midnight',
            interval=1,
            backupCount=30,  # Giữ log 30 ngày
            encoding='utf-8'
        )
        daily_handler.setFormatter(formatter)
        logger.addHandler(daily_handler)

        # Handler cho log lỗi - chỉ ghi các lỗi nghiêm trọng
        error_handler = RotatingFileHandler(
            LOG_FILE.replace('.log', '_error.log'),
            maxBytes=5 * 1024 * 1024,  # 5MB
            backupCount=3,
            encoding='utf-8'
        )
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(formatter)
        logger.addHandler(error_handler)

    except Exception as e:
        logger.error(f"Không thể thiết lập file handlers: {str(e)}")
        logger.warning("Chỉ sử dụng console logging")

    return logger

class BotLogger:
    """
    Class wrapper cho logger với các phương thức tiện ích
    """
    
    def __init__(self, name='legal_bot'):
        self.logger = setup_logger(name)
        self.start_time = datetime.now()

    def log_command(self, user_id, command, args=None):
        """Ghi log khi có lệnh được thực thi"""
        message = f"User {user_id} thực thi lệnh: {command}"
        if args:
            message += f" với tham số: {args}"
        self.logger.info(message)

    def log_error(self, error, context=None):
        """Ghi log lỗi với context"""
        message = f"Lỗi: {str(error)}"
        if context:
            message += f" | Context: {context}"
        self.logger.error(message)

    def log_api_call(self, api_name, status_code, response_time):
        """Ghi log cuộc gọi API"""
        self.logger.info(
            f"API Call - {api_name} | Status: {status_code} | Time: {response_time:.2f}s"
        )

    def log_search(self, user_id, query, results_count):
        """Ghi log tìm kiếm"""
        self.logger.info(
            f"Search - User: {user_id} | Query: {query} | Results: {results_count}"
        )

    def log_user_action(self, user_id, action, details=None):
        """Ghi log hành động của người dùng"""
        message = f"User Action - ID: {user_id} | Action: {action}"
        if details:
            message += f" | Details: {details}"
        self.logger.info(message)

    def get_uptime(self):
        """Lấy thời gian hoạt động của bot"""
        return datetime.now() - self.start_time

# Tạo instance của logger
logger = BotLogger()
