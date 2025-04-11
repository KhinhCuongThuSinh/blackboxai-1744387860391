from typing import Dict, List, Optional
from ..utils.logger import logger

class NewsService:
    """Xử lý tin tức pháp luật"""
    
    def __init__(self, api):
        self.api = api
        self.logger = logger

    def get_latest_news(self, limit: int = 5) -> Dict:
        """Lấy tin tức mới nhất"""
        try:
            result = self.api.get_latest_news(limit)
            self.logger.info("Lấy tin tức mới nhất")
            return result
        except Exception as e:
            self.logger.error(f"Lỗi khi lấy tin tức: {str(e)}")
            return {
                "status": "error",
                "message": "Có lỗi xảy ra khi lấy tin tức"
            }

    def search_news(self, keyword: str, limit: int = 5) -> Dict:
        """Tìm kiếm tin tức"""
        try:
            # To be implemented with real API
            self.logger.info(f"Tìm kiếm tin tức với từ khóa: {keyword}")
            return {
                "status": "error",
                "message": "Tính năng đang được phát triển"
            }
        except Exception as e:
            self.logger.error(f"Lỗi khi tìm kiếm tin tức: {str(e)}")
            return {
                "status": "error",
                "message": "Có lỗi xảy ra khi tìm kiếm tin tức"
            }

    def format_news(self, article: Dict) -> str:
        """Format thông tin tin tức"""
        return (
            f"📰 {article['title']}\n"
            f"⏰ {article['publish_date']}\n"
            f"📝 {article['description']}\n"
            f"🔗 {article['url']}\n"
        )

    def format_news_results(self, results: Dict) -> str:
        """Format kết quả tin tức"""
        if results['status'] == 'error':
            return f"❌ {results['message']}"
            
        if not results.get('articles'):
            return "❌ Không có tin tức mới."
            
        response = "📰 Tin tức pháp luật:\n\n"
        for article in results['articles']:
            response += self.format_news(article) + "\n"
            
        return response
