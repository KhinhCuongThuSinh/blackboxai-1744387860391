# Bot Trợ Giúp Pháp Lý

Bot Telegram hỗ trợ tìm kiếm thông tin pháp luật, tra cứu thuật ngữ pháp lý và cập nhật tin tức pháp luật mới.

## Tính năng

- 🔍 **Tìm kiếm văn bản pháp luật**
  - Tìm kiếm theo từ khóa
  - Hiển thị thông tin chi tiết văn bản
  - Link tham khảo trực tiếp

- 📚 **Tra cứu thuật ngữ pháp lý**
  - Cơ sở dữ liệu thuật ngữ phong phú
  - Giải thích dễ hiểu
  - Cập nhật thường xuyên

- 📰 **Tin tức pháp luật**
  - Cập nhật tin tức mới nhất
  - Tổng hợp từ nhiều nguồn uy tín
  - Thông tin chi tiết và chính xác

## Cài đặt

1. Clone repository:
```bash
git clone <repository-url>
cd legal-bot
```

2. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

3. Tạo file `.env` với nội dung:
```env
TELEGRAM_TOKEN=your_telegram_bot_token
ADMIN_IDS=123456789
LOG_LEVEL=INFO
LOG_FILE=bot.log
```

## Sử dụng

### Các lệnh có sẵn

- `/start` - Khởi động bot
- `/help` - Xem danh sách lệnh
- `/search [từ khóa]` - Tìm văn bản pháp luật
- `/term [thuật ngữ]` - Tra cứu thuật ngữ pháp lý
- `/news` - Xem tin tức pháp luật mới
- `/latest` - Xem văn bản mới ban hành

### Ví dụ sử dụng

1. Tìm kiếm văn bản:
```
/search luật doanh nghiệp
```

2. Tra cứu thuật ngữ:
```
/term doanh nghiệp
```

3. Xem tin tức mới:
```
/news
```

## Cấu trúc dự án

```
legal-bot/
├── legal_bot.py     # Mã nguồn chính của bot
├── mock_api.py      # Mock API cho testing
├── logger.py        # Logging system
├── requirements.txt # Dependencies
└── GUIDE.md        # Tài liệu hướng dẫn
```

## Phát triển

### Thêm tính năng mới

1. Cập nhật mock_api.py với dữ liệu mới
2. Thêm handler trong legal_bot.py
3. Cập nhật danh sách lệnh trong help_command

### Testing

```bash
# Chạy bot với mock API
python legal_bot.py
```

## Lưu ý

- Bot sử dụng mock API cho mục đích testing
- Để triển khai thực tế, cần tích hợp với API thực
- Đảm bảo cập nhật token Telegram hợp lệ

## Giấy phép

[MIT License](LICENSE)
