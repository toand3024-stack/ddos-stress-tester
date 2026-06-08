# 🔥 ADVANCED NETWORK STRESS TESTER v2.0

```
▓█████▄  ██▀███  ▓█████ ▄▄▄       ███▄ ▄███▓
▓██   ██▓██   ██ ▓█   ▀▒████▄    ▓██▒▀█▀ ██▒
▒██   ██▓██   ██ ▒███  ▒██  ▀█▄  ▓██    ▓██░
░██   ██ ██   ██ ▒▓█  ▄░██▄▄▄▄██ ▒██    ▒██ 
░██████▒ ██████  ░▒████▒▓█   ▓██▒▒██▒   ░██▒
░ ▒░▓  ░ ▒░▓  ░  ░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ░  ░
░ ░ ▒  ░ ░ ▒  ░  ░ ░  ░ ░   ▒▒ ░░  ░      ░
  ░ ░    ░ ░       ░    ░   ▒   ░      ░   
    ░  ░   ░  ░    ░  ░     ░  ░       ░   
```

**⚠️ MỤC ĐÍCH SỬ DỤNG GIÁO DỤC - FOR EDUCATIONAL USE ONLY**

Công cụ kiểm tra độ chịu tải của mạng với múi các phương pháp tấn công để mục đích kiểm tra bảo mật.

---

## 📋 Mục Lục

- [Nguyên Lý Hoạt Động](#nguyên-lý-hoạt-động)
- [Các Chế Độ Tấn Công](#các-chế-độ-tấn-công)
- [Yêu Cầu Hệ Thống](#yêu-cầu-hệ-thống)
- [Cài Đặt](#cài-đặt)
- [Cách Sử Dụng](#cách-sử-dụng)
- [Ví Dụ](#ví-dụ)
- [Cảnh Báo Bảo Mật](#cảnh-báo-bảo-mật)

---

## 🔧 Nguyên Lý Hoạt Động

Công cụ này hoạt động bằng cách gửi các yêu cầu HTTP/HTTPS đến máy chủ mục tiêu để kiểm tra khả năng chịu tải và độ ổn định. Nó hỗ trợ nhiều phương pháp tấn công khác nhau:

### Cơ Chế Tấn Công:

1. **Proxy-based Attack** - Sử dụng danh sách proxy để ẩn địa chỉ IP thực
2. **Direct Attack** - Tấn công trực tiếp từ máy của bạn (IP thực hiện)
3. **Slowloris** - Giữ mở nhiều kết nối chậm để cạn kiệt tài nguyên máy chủ
4. **Slow POST (RUDY)** - Gửi POST request chậm để làm quá tải bộ đệm
5. **Slow Read** - Đọc dữ liệu chậm bằng cách giảm cửa sổ TCP
6. **HTTP Flood** - Gửi lượng lớn yêu cầu GET/POST nhanh chóng

---

## 🎯 Các Chế Độ Tấn Công

### 1. Proxy-based GET Flood (Mặc Định)
- Sử dụng danh sách proxy công khai
- Ẩn địa chỉ IP thực
- Tích hợp kiểm tra proxy tự động
- Loại bỏ proxy không hoạt động

```python
Chế độ: 1
Tệp proxy: [nhấn Enter để tải tự động từ mạng]
```

### 2. Direct Attack
- Tấn công trực tiếp không qua proxy
- IP của bạn sẽ hiển thị (khuyên dùng VPN/Tor)
- Tốc độ nhanh hơn

```python
Chế độ: 2
```

### 3. Slowloris
- Mở nhiều kết nối TCP và giữ chúng sống
- Gửi header chậm chạp để làm cho máy chủ chờ
- Hiệu quả với máy chủ có giới hạn kết nối

```python
Chế độ: 3
Số socket: [mặc định 300]
```

### 4. Slow POST (RUDY)
- Gửi POST request với body rất chậm
- Tìm form trên trang và gửi dữ liệu từng phần
- Làm cạn kiệt bộ đệm máy chủ

```python
Chế độ: 4
Số luồng: [mặc định 50]
```

### 5. Slow Read
- Nhận dữ liệu với cửa sổ TCP = 0
- Buộc máy chủ chờ lâu hơn để gửi dữ liệu
- Cạn kiệt bộ nhớ buffer của máy chủ

```python
Chế độ: 5
Số luồng: [mặc định 100]
```

### 6. HTTP Flood
- Gửi lượng lớn yêu cầu GET hoặc POST
- Sử dụng asyncio nếu có > 500 luồng
- Cách tấn công brute-force đơn giản

```python
Chế độ: 6
Phương thức: GET/POST
Số luồng: [mặc định 200]
```

---

## 📦 Yêu Cầu Hệ Thống

### Python
- Python 3.7+
- Hỗ trợ: Linux, macOS, Windows

### Thư viện Bắt Buộc
```
urllib3
```

### Thư viện Tùy Chọn (cho chức năng nâng cao)
```
requests          # Cho Slow POST
beautifulsoup4    # Cho phân tích form
aiohttp          # Cho HTTP Flood async
asyncio          # Cho HTTP Flood async
```

---

## 🚀 Cài Đặt

### 1. Clone Repository từ GitHub

```bash
git clone https://github.com/toand3024-stack/ddos-stress-tester
cd ddos-stress-tester
```

### 2. Cài Đặt Dependencies

```bash
# Cài đặt thư viện bắt buộc
pip install urllib3

# Cài đặt tất cả thư viện (khuyến nghị)
pip install urllib3 requests beautifulsoup4 aiohttp
```

### 3. Cấp Quyền Thực Thi (Linux/macOS)

```bash
chmod +x ddos_v1.py
```

---

## 💻 Cách Sử Dụng

### Chạy Công Cụ

```bash
# Chạy trực tiếp
python3 ddos_v1.py

# Hoặc (nếu đã cấp quyền thực thi)
./ddos_v1.py
```

### Giao Diện Tương Tác

Công cụ sẽ yêu cầu bạn nhập:

1. **Chế độ tấn công** (1-6)
2. **URL mục tiêu** (ví dụ: https://example.com)
3. **Tham số bổ sung** (tùy theo chế độ chọn)

---

## 📝 Ví Dụ

### Ví dụ 1: Proxy-based GET Flood

```
Chọn: 1
URL: https://target.com
Tệp proxy: [nhấn Enter]
```

Kết quả:
```
[+] Found proxies: 500
[+] Checking (≈30 seconds)
[+] Attacking with 50 proxies
proxy1.com:8080: request sent over HTTP/1.1 (200), size 5432 B
proxy2.com:3128: request sent over HTTP/1.1 (503), size 1234 B
...
```

### Ví dụ 2: Slowloris Attack

```
Chọn: 3
Số socket: 500
```

Kết quả:
```
[+] Slowloris attacking target.com:443
X-12345: 54321
X-99999: 12345
...
```

### Ví dụ 3: HTTP Flood

```
Chọn: 6
Phương thức: POST
Số luồng: 1000
```

Kết quả:
```
[+] HTTP POST Flood attacking https://target.com with 1000 threads
HTTP Flood: 502
HTTP Flood: 503
HTTP Flood: 200
...
```

---

## 🛡️ Cảnh Báo Bảo Mật

### ⚠️ CẢNH BÁO QUAN TRỌNG

**Công cụ này chỉ được sử dụng cho:**
- ✅ Kiểm tra bảo mật của máy chủ riêng của bạn
- ✅ Kiểm tra độ chịu tải hợp pháp với sự cho phép
- ✅ Mục đích giáo dục và nghiên cứu
- ✅ Phòng lab và môi trường kiểm tra

**Luật pháp:**
- ❌ Không sử dụng tấn công máy chủ của người khác mà không có sự cho phép
- ❌ Vi phạm có thể dẫn đến hành động pháp lý
- ❌ Có thể bị xử phạt hình sự theo DMCA/Computer Fraud laws

### Mẹo Bảo Mật

1. **Sử dụng VPN/Tor** khi thực hiện direct attack
2. **Tắt chế độ quay lại** sau khi sử dụng
3. **Xóa lịch sử** từ terminal hoặc công cụ
4. **Kiểm tra luật địa phương** trước khi sử dụng
5. **Có được sự cho phép bằng văn bản** từ chủ máy chủ mục tiêu

---

## 🔐 Tính Năng Bảo Mật

- ✅ User-Agent ngẫu nhiên (15+ biến thể)
- ✅ Header HTTP thực tế (Accept, Accept-Encoding, etc.)
- ✅ Kiểm tra Cloudflare protection
- ✅ Hỗ trợ proxy ẩn danh
- ✅ Xác minh proxy tự động
- ✅ Hỗ trợ SSL/TLS
- ✅ Timeout tùy chỉnh
- ✅ Phát hiện và bỏ qua proxy chết

---

## 🐛 Khắc Phục Sự Cố

### Lỗi: "ModuleNotFoundError: No module named 'urllib3'"

```bash
pip install urllib3
```

### Lỗi: "Missing requests/bs4"

```bash
pip install requests beautifulsoup4
```

### Lỗi: Kết nối bị từ chối

- Kiểm tra URL có chính xác không
- Kiểm tra kết nối mạng
- Thử với proxy khác
- Kiểm tra firewall

### Lỗi: "Connection timeout"

- Tăng timeout (chỉnh sửa mã)
- Sử dụng proxy gần hơn
- Kiểm tra tốc độ mạng

---

## 📊 Hiệu Năng

### Yêu Cầu Hệ Thống Tối Thiểu
- RAM: 512 MB
- CPU: 1 core
- Bandwidth: 1 Mbps

### Yêu Cầu Khuyến Nghị
- RAM: 4 GB
- CPU: 4 cores
- Bandwidth: 10 Mbps

---

## 👨‍💻 Tác Giả

- **Phát triển ban đầu**: mishakorzik
- **Cập nhật v2.0**: toandinh

---

## 📄 Giấy Phép

MIT License - Xem file LICENSE để chi tiết

---

## 🤝 Đóng Góp

Mọi đóng góp, báo cáo lỗi và đề xuất tính năng được hoan nghênh!

---

## 📚 Tài Liệu Tham Khảo

- [OWASP DDoS](https://owasp.org/)
- [HTTP Flood Attack](https://en.wikipedia.org/wiki/Denial-of-service_attack)
- [Slowloris Attack](https://en.wikipedia.org/wiki/Slowloris_(software))

---

## ⚖️ Tuyên Bố Pháp Lý

Tác giả không chịu trách nhiệm cho bất kỳ hành động bất hợp pháp nào được thực hiện bằng công cụ này. Người dùng có trách nhiệm tuân thủ tất cả các luật pháp hiện hành.

**Sử dụng công cụ này có nghĩa là bạn đã đọc và đồng ý với các điều khoản này.**

---

**Made with ❤️ by toandinh**
