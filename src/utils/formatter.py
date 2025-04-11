from typing import Dict, List

class ResponseFormatter:
    """Định dạng kết quả trả về"""
    
    @staticmethod
    def format_error(message: str) -> str:
        """Format thông báo lỗi"""
        return f"❌ {message}"

    @staticmethod
    def format_document(doc: Dict) -> str:
        """Format thông tin văn bản"""
        return (
            f"📄 {doc['title']}\n"
            f"📅 Ban hành: {doc['issue_date']}\n"
            f"📋 Số hiệu: {doc['code']}\n"
            f"📝 {doc.get('summary', '')}\n"
            f"🔗 {doc['url']}\n"
        )

    @staticmethod
    def format_news(article: Dict) -> str:
        """Format thông tin tin tức"""
        return (
            f"📰 {article['title']}\n"
            f"⏰ {article['publish_date']}\n"
            f"📝 {article['description']}\n"
            f"🔗 {article['url']}\n"
        )

    @staticmethod
    def format_term(term: str, definition: str) -> str:
        """Format thuật ngữ và định nghĩa"""
        return f"📚 {term.capitalize()}:\n\n{definition}"

    @staticmethod
    def format_list(items: List[str], prefix: str = "•") -> str:
        """Format danh sách items"""
        return "\n".join(f"{prefix} {item}" for item in items)

    @staticmethod
    def format_help() -> str:
        """Format hướng dẫn sử dụng"""
        return (
            "📚 Danh sách lệnh:\n\n"
            "/start - Khởi động bot\n"
            "/help - Hiển thị trợ giúp này\n"
            "/search [từ khóa] - Tìm văn bản pháp luật\n"
            "/term [thuật ngữ] - Tra cứu thuật ngữ pháp lý\n"
            "/news - Xem tin tức pháp luật mới\n"
            "/latest - Xem văn bản mới ban hành"
        )

    @staticmethod
    def format_welcome() -> str:
        """Format tin nhắn chào mừng"""
        return (
            "👋 Chào mừng bạn đến với Bot Trợ Giúp Pháp Lý!\n\n"
            "Bot có thể giúp bạn:\n"
            "🔍 Tìm kiếm văn bản pháp luật\n"
            "📚 Tra cứu thuật ngữ pháp lý\n"
            "📰 Xem tin tức pháp luật mới\n\n"
            "Sử dụng /help để xem danh sách lệnh chi tiết"
        )
