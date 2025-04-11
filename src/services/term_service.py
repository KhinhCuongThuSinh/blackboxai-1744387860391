from typing import Dict, List, Optional
from ..utils.logger import logger

class TermService:
    """Xử lý thuật ngữ pháp lý"""
    
    def __init__(self, api):
        self.api = api
        self.logger = logger

    def search_term(self, term: str) -> Dict:
        """Tìm kiếm thuật ngữ"""
        try:
            result = self.api.search_terms(term)
            self.logger.info(f"Tra cứu thuật ngữ: {term}")
            return result
        except Exception as e:
            self.logger.error(f"Lỗi khi tra cứu thuật ngữ: {str(e)}")
            return {
                "status": "error",
                "message": "Có lỗi xảy ra khi tra cứu thuật ngữ"
            }

    def get_all_terms(self) -> List[str]:
        """Lấy danh sách thuật ngữ"""
        try:
            terms = list(self.api.legal_terms.keys())
            self.logger.info("Lấy danh sách thuật ngữ")
            return terms
        except Exception as e:
            self.logger.error(f"Lỗi khi lấy danh sách thuật ngữ: {str(e)}")
            return []

    def format_term_result(self, result: Dict) -> str:
        """Format kết quả tra cứu thuật ngữ"""
        if result['status'] == 'error':
            return f"❌ {result['message']}"
            
        return (
            f"📚 {result['term'].capitalize()}:\n\n"
            f"{result['definition']}"
        )

    def format_terms_list(self, terms: List[str]) -> str:
        """Format danh sách thuật ngữ"""
        if not terms:
            return "❌ Không có thuật ngữ nào."
            
        response = "📚 Danh sách thuật ngữ:\n\n"
        for term in terms:
            response += f"• {term}\n"
            
        response += "\nSử dụng /term [thuật ngữ] để xem giải thích"
        return response
