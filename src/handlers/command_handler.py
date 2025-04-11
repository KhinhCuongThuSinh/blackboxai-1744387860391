from typing import Dict, List, Optional
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from ..utils.logger import logger
from ..services.document_service import DocumentService
from ..services.news_service import NewsService
from ..services.term_service import TermService

class CommandHandler:
    """Xử lý các lệnh của bot"""
    
    def __init__(self, api):
        self.document_service = DocumentService(api)
        self.news_service = NewsService(api)
        self.term_service = TermService(api)
        self.logger = logger

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Xử lý lệnh /start"""
        try:
            welcome_message = (
                "👋 Chào mừng bạn đến với Bot Trợ Giúp Pháp Lý!\n\n"
                "Bot có thể giúp bạn:\n"
                "🔍 Tìm kiếm văn bản pháp luật\n"
                "📚 Tra cứu thuật ngữ pháp lý\n"
                "📰 Xem tin tức pháp luật mới\n\n"
                "Sử dụng /help để xem danh sách lệnh chi tiết"
            )
            
            keyboard = [
                [
                    InlineKeyboardButton("🔍 Tìm văn bản", callback_data='search'),
                    InlineKeyboardButton("📚 Thuật ngữ", callback_data='terms')
                ],
                [
                    InlineKeyboardButton("📰 Tin tức", callback_data='news'),
                    InlineKeyboardButton("❓ Trợ giúp", callback_data='help')
                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await update.message.reply_text(welcome_message, reply_markup=reply_markup)
            self.logger.info(f"User {update.effective_user.id} đã bắt đầu sử dụng bot")
        except Exception as e:
            self.logger.error(f"Lỗi trong lệnh /start: {str(e)}")
            await update.message.reply_text("❌ Có lỗi xảy ra, vui lòng thử lại sau!")

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Xử lý lệnh /help"""
        try:
            help_text = (
                "📚 Danh sách lệnh:\n\n"
                "/start - Khởi động bot\n"
                "/help - Hiển thị trợ giúp này\n"
                "/search [từ khóa] - Tìm văn bản pháp luật\n"
                "/term [thuật ngữ] - Tra cứu thuật ngữ pháp lý\n"
                "/news - Xem tin tức pháp luật mới\n"
                "/latest - Xem văn bản mới ban hành"
            )
            await update.message.reply_text(help_text)
            self.logger.info(f"User {update.effective_user.id} đã xem trợ giúp")
        except Exception as e:
            self.logger.error(f"Lỗi trong lệnh /help: {str(e)}")
            await update.message.reply_text("❌ Có lỗi xảy ra, vui lòng thử lại sau!")

    async def search_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Xử lý lệnh /search"""
        try:
            if not context.args:
                await update.message.reply_text(
                    "🔍 Vui lòng nhập từ khóa tìm kiếm sau lệnh /search\n"
                    "Ví dụ: /search luật doanh nghiệp"
                )
                return
                
            keyword = ' '.join(context.args)
            result = self.document_service.search(keyword)
            response = self.document_service.format_search_results(result)
            await update.message.reply_text(response)
            self.logger.info(f"User {update.effective_user.id} đã tìm kiếm: {keyword}")
        except Exception as e:
            self.logger.error(f"Lỗi trong lệnh /search: {str(e)}")
            await update.message.reply_text("❌ Có lỗi xảy ra khi tìm kiếm!")

    async def term_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Xử lý lệnh /term"""
        try:
            if not context.args:
                terms = self.term_service.get_all_terms()
                response = self.term_service.format_terms_list(terms)
                await update.message.reply_text(response)
                return
                
            term = ' '.join(context.args).lower()
            result = self.term_service.search_term(term)
            response = self.term_service.format_term_result(result)
            await update.message.reply_text(response)
            self.logger.info(f"User {update.effective_user.id} đã tra cứu thuật ngữ: {term}")
        except Exception as e:
            self.logger.error(f"Lỗi trong lệnh /term: {str(e)}")
            await update.message.reply_text("❌ Có lỗi xảy ra khi tra cứu!")

    async def news_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Xử lý lệnh /news"""
        try:
            result = self.news_service.get_latest_news()
            response = self.news_service.format_news_results(result)
            await update.message.reply_text(response)
            self.logger.info(f"User {update.effective_user.id} đã xem tin tức")
        except Exception as e:
            self.logger.error(f"Lỗi trong lệnh /news: {str(e)}")
            await update.message.reply_text("❌ Có lỗi xảy ra khi lấy tin tức!")

    async def latest_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Xử lý lệnh /latest"""
        try:
            result = self.document_service.get_latest()
            response = self.document_service.format_search_results(result)
            await update.message.reply_text(response)
            self.logger.info(f"User {update.effective_user.id} đã xem văn bản mới")
        except Exception as e:
            self.logger.error(f"Lỗi trong lệnh /latest: {str(e)}")
            await update.message.reply_text("❌ Có lỗi xảy ra!")
