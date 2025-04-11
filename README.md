# Bot Trợ Giúp Pháp Lý

Bot Telegram hỗ trợ tìm kiếm thông tin và tổng hợp pháp lý, giúp người dùng dễ dàng tiếp cận với các văn bản pháp luật, thuật ngữ pháp lý và nhận tư vấn cơ bản.

## Tính năng

- 🔍 **Tìm kiếm văn bản pháp luật**
  - Tìm kiếm theo từ khóa
  - Hiển thị kết quả với link tham khảo

- 📚 **Tra cứu thuật ngữ pháp lý**
  - Cơ sở dữ liệu thuật ngữ phong phú
  - Giải thích dễ hiểu

- 📰 **Tin tức pháp luật**
  - Cập nhật tin tức mới nhất
  - Tổng hợp từ nhiều nguồn uy tín

- 📝 **Mẫu đơn và hợp đồng**
  - Nhiều mẫu đơn phổ biến
  - Hướng dẫn điền mẫu

- ❓ **Tư vấn pháp lý cơ bản**
  - Trả lời các câu hỏi thường gặp
  - Hướng dẫn thủ tục

- 📚 **Trang tham khảo pháp lý**
  - Cung cấp danh sách các trang web tham khảo pháp lý

## Cài đặt

1. Clone repository:
```bash
git clone <repository-url>
cd legal-bot
```

2. Cài đặt các thư viện:
```bash
pip install -r requirements.txt
```

3. Tạo file `.env` với nội dung:
```env
TELEGRAM_TOKEN=your_telegram_bot_token
ADMIN_IDS=123456789,987654321
LEGAL_API_KEY=your_legal_api_key
NEWS_API_KEY=your_news_api_key
```

## Sử dụng

### Các lệnh có sẵn

- `/start` - Khởi động bot
- `/help` - Xem danh sách lệnh
- `/search [từ khóa]` - Tìm văn bản pháp luật
- `/term [thuật ngữ]` - Tra cứu thuật ngữ pháp lý
- `/news` - Xem tin tức pháp luật mới
- `/template [loại]` - Tải mẫu đơn, hợp đồng
- `/consult [vấn đề]` - Tư vấn pháp lý
- `/references [từ khóa]` - Xem danh sách trang tham khảo pháp lý
- `/stats` - Xem thống kê (chỉ admin)

### Ví dụ sử dụng

1. Tìm kiếm văn bản:
```
/search luật doanh nghiệp
```

2. Tra cứu thuật ngữ:
```
/term dân sự
```

3. Tải mẫu đơn:
```
/template đơn kiện
```

4. Tư vấn:
```
/consult thủ tục đăng ký kinh doanh
```

5. Xem trang tham khảo:
```
/references thư viện pháp luật
```

## Phát triển

### Cấu trúc dự án

```
legal-bot/
├── bot.py              # Mã nguồn chính của bot
├── config.py           # Cấu hình
├── requirements.txt    # Thư viện phụ thuộc
└── README.md          # Tài liệu hướng dẫn
```

### Thêm tính năng mới

1. Thêm hàm xử lý trong `bot.py`
2. Cập nhật danh sách lệnh trong hàm `help_command()`
3. Thêm handler trong hàm `main()`

## Đóng góp

Mọi đóng góp đều được chào đón! Vui lòng tạo issue hoặc pull request.

## Lưu ý

- Bot chỉ cung cấp thông tin tham khảo
- Để được tư vấn chính xác, vui lòng liên hệ luật sư
- Các mẫu đơn chỉ mang tính chất tham khảo

## Giấy phép

[MIT License](LICENSE)
