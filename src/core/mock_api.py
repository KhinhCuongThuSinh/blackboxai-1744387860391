from typing import Dict, List
from datetime import datetime, timedelta
from ..utils.logger import logger

class MockLegalAPI:
    """Mock API cho dữ liệu pháp luật"""
    
    def __init__(self):
        self.legal_documents = [
            {
                "id": "1",
                "title": "Luật Doanh nghiệp 2020",
                "code": "59/2020/QH14",
                "issue_date": "2020-06-17",
                "effective_date": "2021-01-01",
                "category": "Luật",
                "summary": "Quy định về thành lập, tổ chức quản lý, tổ chức lại, giải thể và hoạt động của doanh nghiệp",
                "url": "https://example.com/luat-doanh-nghiep-2020"
            },
            {
                "id": "2",
                "title": "Luật Đất đai (sửa đổi) 2024",
                "code": "22/2024/QH15",
                "issue_date": "2024-01-18",
                "effective_date": "2025-01-01",
                "category": "Luật",
                "summary": "Quy định về chế độ sở hữu đất đai, quyền và nghĩa vụ của Nhà nước và công dân đối với đất đai",
                "url": "https://example.com/luat-dat-dai-2024"
            },
            {
                "id": "3",
                "title": "Nghị định về đăng ký doanh nghiệp",
                "code": "01/2024/ND-CP",
                "issue_date": "2024-01-15",
                "effective_date": "2024-03-01",
                "category": "Nghị định",
                "summary": "Hướng dẫn chi tiết về đăng ký doanh nghiệp",
                "url": "https://example.com/nghi-dinh-01-2024"
            }
        ]
        
        self.legal_news = [
            {
                "id": "1",
                "title": "Những điểm mới của Luật Đất đai 2024",
                "publish_date": "2024-01-19",
                "source": "VnExpress",
                "description": "Quốc hội thông qua Luật Đất đai (sửa đổi) với nhiều điểm mới quan trọng về quyền sử dụng đất...",
                "url": "https://example.com/news/1"
            },
            {
                "id": "2",
                "title": "Hướng dẫn mới về thành lập doanh nghiệp",
                "publish_date": "2024-02-01",
                "source": "Báo Pháp luật",
                "description": "Bộ KH&ĐT ban hành thông tư mới hướng dẫn chi tiết về thủ tục thành lập doanh nghiệp...",
                "url": "https://example.com/news/2"
            },
            {
                "id": "3",
                "title": "Thay đổi về thuế thu nhập doanh nghiệp",
                "publish_date": "2024-02-15",
                "source": "Tuổi Trẻ",
                "description": "Từ 1/7/2024, nhiều quy định mới về thuế TNDN sẽ có hiệu lực...",
                "url": "https://example.com/news/3"
            }
        ]
        
        self.legal_terms = {
            "doanh nghiệp": "Tổ chức kinh tế có tên riêng, có tài sản, có trụ sở giao dịch, được đăng ký thành lập theo quy định của pháp luật",
            "hợp đồng": "Thỏa thuận giữa các bên về việc xác lập, thay đổi hoặc chấm dứt quyền, nghĩa vụ dân sự",
            "sở hữu trí tuệ": "Quyền của tổ chức, cá nhân đối với tài sản trí tuệ, bao gồm quyền tác giả, quyền liên quan đến quyền tác giả, quyền sở hữu công nghiệp",
            "thuế": "Khoản nộp bắt buộc vào ngân sách nhà nước của tổ chức, cá nhân theo quy định của pháp luật"
        }

    def search_documents(self, keyword: str, limit: int = 10) -> Dict:
        """Tìm kiếm văn bản theo từ khóa"""
        try:
            results = []
            keyword = keyword.lower()
            
            for doc in self.legal_documents:
                if (keyword in doc['title'].lower() or 
                    keyword in doc['summary'].lower()):
                    results.append(doc)
                    
                if len(results) >= limit:
                    break
                    
            return {
                "status": "success",
                "total": len(results),
                "documents": results
            }
        except Exception as e:
            logger.error(f"Lỗi khi tìm kiếm văn bản: {str(e)}")
            return {
                "status": "error",
                "message": "Có lỗi xảy ra khi tìm kiếm văn bản"
            }

    def get_latest_documents(self, limit: int = 5) -> Dict:
        """Lấy danh sách văn bản mới nhất"""
        try:
            sorted_docs = sorted(
                self.legal_documents,
                key=lambda x: x['issue_date'],
                reverse=True
            )
            return {
                "status": "success",
                "total": len(sorted_docs[:limit]),
                "documents": sorted_docs[:limit]
            }
        except Exception as e:
            logger.error(f"Lỗi khi lấy văn bản mới: {str(e)}")
            return {
                "status": "error",
                "message": "Có lỗi xảy ra khi lấy văn bản mới"
            }

    def get_latest_news(self, limit: int = 5) -> Dict:
        """Lấy tin tức mới nhất"""
        try:
            sorted_news = sorted(
                self.legal_news,
                key=lambda x: x['publish_date'],
                reverse=True
            )
            return {
                "status": "success",
                "total": len(sorted_news[:limit]),
                "articles": sorted_news[:limit]
            }
        except Exception as e:
            logger.error(f"Lỗi khi lấy tin tức: {str(e)}")
            return {
                "status": "error",
                "message": "Có lỗi xảy ra khi lấy tin tức"
            }

    def search_terms(self, term: str) -> Dict:
        """Tìm kiếm thuật ngữ pháp lý"""
        try:
            term = term.lower()
            if term in self.legal_terms:
                return {
                    "status": "success",
                    "term": term,
                    "definition": self.legal_terms[term]
                }
            return {
                "status": "error",
                "message": "Không tìm thấy thuật ngữ"
            }
        except Exception as e:
            logger.error(f"Lỗi khi tra cứu thuật ngữ: {str(e)}")
            return {
                "status": "error",
                "message": "Có lỗi xảy ra khi tra cứu thuật ngữ"
            }
