# Services module initialization
from .document_service import DocumentService
from .news_service import NewsService
from .term_service import TermService

__all__ = ['DocumentService', 'NewsService', 'TermService']
