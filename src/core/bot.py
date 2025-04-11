import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
from test_config import TELEGRAM_TOKEN, ADMIN_IDS
from test_logger import logger
from mock_api import MockLegalAPI

class LegalBot:
    def __init__(self):
        self.api = MockLegalAPI()

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
            logger.info(f"User {update.effective_user.id} đã bắt đầu sử dụng bot")
        except Exception as e:
            logger.error(f"Lỗi trong lệnh /start: {str(e)}")
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
            logger.info(f"User {update.effective_user.id} đã xem trợ giúp")
        except Exception as e:
            logger.error(f"Lỗi trong lệnh /help: {str(e)}")
            await update.message.reply_text("❌ Có lỗi xảy ra, vui lòng thử lại sau!")

    async def search_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Tìm kiếm văn bản pháp luật"""
        try:
            if not context.args:
                await update.message.reply_text(
                    "🔍 Vui lòng nhập từ khóa tìm kiếm sau lệnh /search\n"
                    "Ví dụ: /search luật doanh nghiệp"
                )
                return
                
            keyword = ' '.join(context.args)
            result = self.api.search_documents(keyword)
            
            if result['status'] == 'success' and result['documents']:
                response = "🔍 Kết quả tìm kiếm:\n\n"
                for doc in result['documents']:
                    response += (
                        f"📄 {doc['title']}\n"
                        f"📅 Ban hành: {doc['issue_date']}\n"
                        f"📋 Số hiệu: {doc['code']}\n"
                        f"🔗 {doc['url']}\n\n"
                    )
            else:
                response = "❌ Không tìm thấy văn bản phù hợp."
                
            await update.message.reply_text(response)
            logger.info(f"User {update.effective_user.id} đã tìm kiếm: {keyword}")
        except Exception as e:
            logger.error(f"Lỗi trong lệnh /search: {str(e)}")
            await update.message.reply_text("❌ Có lỗi xảy ra khi tìm kiếm!")

    async def term_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Tra cứu thuật ngữ pháp lý"""
        try:
            if not context.args:
                terms = list(self.api.legal_terms.keys())
                terms_list = "📚 Danh sách thuật ngữ có sẵn:\n\n" + "\n".join(
                    f"• {term}" for term in terms
                )
                await update.message.reply_text(terms_list)
                return
                
            term = ' '.join(context.args).lower()
            result = self.api.search_terms(term)
            
            if result['status'] == 'success':
                response = f"📖 {result['term'].capitalize()}:\n\n{result['definition']}"
            else:
                response = "❌ Không tìm thấy thuật ngữ này."
                
            await update.message.reply_text(response)
            logger.info(f"User {update.effective_user.id} đã tra cứu thuật ngữ: {term}")
        except Exception as e:
            logger.error(f"Lỗi trong lệnh /term: {str(e)}")
            await update.message.reply_text("❌ Có lỗi xảy ra khi tra cứu!")

    async def news_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Xem tin tức pháp luật mới"""
        try:
            result = self.api.get_latest_news()
            
            if result['status'] == 'success' and result['articles']:
                response = "📰 Tin tức pháp luật mới:\n\n"
                for article in result['articles']:
                    response += (
                        f"📌 {article['title']}\n"
                        f"⏰ {article['publish_date']}\n"
                        f"📝 {article['description']}\n"
                        f"🔗 {article['url']}\n\n"
                    )
            else:
                response = "❌ Không có tin tức mới."
                
            await update.message.reply_text(response)
            logger.info(f"User {update.effective_user.id} đã xem tin tức")
        except Exception as e:
            logger.error(f"Lỗi trong lệnh /news: {str(e)}")
            await update.message.reply_text("❌ Có lỗi xảy ra khi lấy tin tức!")

    async def latest_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Xem văn bản mới ban hành"""
        try:
            result = self.api.get_latest_documents()
            
            if result['status'] == 'success' and result['documents']:
                response = "📄 Văn bản mới ban hành:\n\n"
                for doc in result['documents']:
                    response += (
                        f"📄 {doc['title']}\n"
                        f"📅 Ban hành: {doc['issue_date']}\n"
                        f"📋 Số hiệu: {doc['code']}\n"
                        f"🔗 {doc['url']}\n\n"
                    )
            else:
                response = "❌ Không có văn bản mới."
                
            await update.message.reply_text(response)
            logger.info(f"User {update.effective_user.id} đã xem văn bản mới")
        except Exception as e:
            logger.error(f"Lỗi trong lệnh /latest: {str(e)}")
            await update.message.reply_text("❌ Có lỗi xảy ra!")

    async def button_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Xử lý các nút bấm inline"""
        try:
            query = update.callback_query
            await query.answer()
            
            if query.data == 'search':
                await query.message.reply_text(
                    "🔍 Để tìm kiếm văn bản pháp luật, sử dụng:\n"
                    "/search [từ khóa]\n"
                    "Ví dụ: /search luật doanh nghiệp"
                )
            elif query.data == 'terms':
                terms = list(self.api.legal_terms.keys())
                terms_list = "📚 Danh sách thuật ngữ có sẵn:\n\n" + "\n".join(
                    f"• {term}" for term in terms
                )
                await query.message.reply_text(terms_list)
            elif query.data == 'news':
                await self.news_command(update, context)
            elif query.data == 'help':
                await self.help_command(update, context)
                
        except Exception as e:
            logger.error(f"Lỗi khi xử lý nút bấm: {str(e)}")

def main():
    """Khởi động bot"""
    try:
        print("🚀 Đang khởi động bot...")
        bot = LegalBot()
        application = Application.builder().token(TELEGRAM_TOKEN).build()

        # Thêm các handlers
        application.add_handler(CommandHandler("start", bot.start_command))
        application.add_handler(CommandHandler("help", bot.help_command))
        application.add_handler(CommandHandler("search", bot.search_command))
        application.add_handler(CommandHandler("term", bot.term_command))
        application.add_handler(CommandHandler("news", bot.news_command))
        application.add_handler(CommandHandler("latest", bot.latest_command))
        
        # Handler cho các nút bấm
        application.add_handler(CallbackQueryHandler(bot.button_handler))

        print("✅ Bot đã sẵn sàng!")
        logger.info("Bot đã được khởi động!")
        application.run_polling(allowed_updates=Update.ALL_TYPES)

    except Exception as e:
        logger.error(f"Lỗi khởi động bot: {str(e)}")
        print(f"❌ Lỗi: {str(e)}")

if __name__ == '__main__':
    main()
