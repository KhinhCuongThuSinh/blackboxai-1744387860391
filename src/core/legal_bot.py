import asyncio
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from ..utils.logger import logger
from ..handlers.command_handler import CommandHandler
from .mock_api import MockLegalAPI

class LegalBot:
    """Bot Trợ Giúp Pháp Lý"""
    
    def __init__(self, token: str):
        """Khởi tạo bot"""
        self.token = token
        self.api = MockLegalAPI()
        self.handler = CommandHandler(self.api)
        self.logger = logger

    async def start(self):
        """Khởi động bot"""
        try:
            # Khởi tạo application
            application = Application.builder().token(self.token).build()

            # Đăng ký các handlers
            application.add_handler(CommandHandler("start", self.handler.start_command))
            application.add_handler(CommandHandler("help", self.handler.help_command))
            application.add_handler(CommandHandler("search", self.handler.search_command))
            application.add_handler(CommandHandler("term", self.handler.term_command))
            application.add_handler(CommandHandler("news", self.handler.news_command))
            application.add_handler(CommandHandler("latest", self.handler.latest_command))

            # Handler cho các nút bấm
            application.add_handler(CallbackQueryHandler(self.handler.button_handler))

            # Khởi động bot
            self.logger.info("Bot đang khởi động...")
            await application.initialize()
            await application.start()
            await application.run_polling()

        except Exception as e:
            self.logger.error(f"Lỗi khởi động bot: {str(e)}")
            raise

def main():
    """Hàm main để chạy bot"""
    import os
    from dotenv import load_dotenv

    # Load biến môi trường
    load_dotenv()
    
    # Lấy token từ biến môi trường
    token = os.getenv('TELEGRAM_TOKEN')
    if not token:
        raise ValueError("Không tìm thấy TELEGRAM_TOKEN trong biến môi trường!")

    # Khởi tạo và chạy bot
    bot = LegalBot(token)
    
    try:
        print("🚀 Đang khởi động Bot Trợ Giúp Pháp Lý...")
        asyncio.run(bot.start())
    except KeyboardInterrupt:
        print("\n👋 Tạm biệt!")
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")

if __name__ == '__main__':
    main()
