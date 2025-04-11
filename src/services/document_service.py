from typing import Dict, List, Optional
from ..utils.logger import logger

class DocumentService:
    """Xử lý văn bản pháp luật"""
    
    def __init__(self, api):
        self.api = api
        self.logger = logger

    def search(self, keyword: str, limit: int = 10) -> Dict:
        """Tìm kiếm văn bản"""
        try:
            result = self.api.search_documents(keyword, limit)
            self.logger.info(f"Tìm kiếm văn bản với từ khóa: {keyword}")
            return result
        except Exception as e:
            self.logger.error(f"Lỗi khi tìm kiếm văn bản: {str(e)}")
            return {
                "status": "error",
                "message": "Có lỗi xảy ra khi tìm kiếm văn bản"
            }

    def get_latest(self, limit: int = 5) -> Dict:
        """Lấy văn bản mới"""
        try:
            result = self.api.get_latest_documents(limit)
            self.logger.info("Lấy danh sách văn bản mới")
            return result
        except Exception as e:
            self.logger.error(f"Lỗi khi lấy văn bản mới: {str(e)}")
            return {
                "status": "error",
                "message": "Có lỗi xảy ra khi lấy văn bản mới"
            }

    def format_document(self, doc: Dict) -> str:
        """Format thông tin văn bản"""
        return (
            f"📄 {doc['title']}\n"
            f"📅 Ban hành: {doc['issue_date']}\n"
            f"📋 Số hiệu: {doc['code']}\n"
            f"📝 {doc.get('summary', '')}\n"
            f"🔗 {doc['url']}\n"
        )

    def format_search_results(self, results: Dict) -> str:
        """Format kết quả tìm kiếm"""
        if results['status'] == 'error':
            return f"❌ {results['message']}"
            
        if not results.get('documents'):
            return "❌ Không tìm thấy văn bản phù hợp."
            
        response = "🔍 Kết quả tìm kiếm:\n\n"
        for doc in results['documents']:
            response += self.format_document(doc) + "\n"
            
        return response
