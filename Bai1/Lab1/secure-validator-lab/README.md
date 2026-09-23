# BÁO CÁO THỰC HÀNH: SECURE VALIDATOR LAB
**Môn học:** Thực hành Lập trình An toàn Thông tin  
**Bài thực hành:** Bài 1 - Lab 1: Xây dựng & Tối ưu Mô-đun Xác thực Dữ liệu Đầu vào An toàn  
**Sinh viên thực hiện:** Nhan Huỳnh Lâm  

---

## 1. Giới thiệu tổng quan
Trong phát triển ứng dụng web, dữ liệu đầu vào không được kiểm soát chặt chẽ (Untrusted Input) là nguyên nhân hàng đầu dẫn đến các lỗ hổng nghiêm trọng như **SQL Injection (SQLi)**, **Cross-Site Scripting (XSS)**, **Path Traversal**, hay **Bypass Logic / Resource Access**.

Dự án **Secure Validator** cung cấp một giải pháp xác thực (Validation) và làm sạch dữ liệu (Sanitization) tập trung, đồng thời cung cấp giao diện Web trực quan (xây dựng bằng Flask) để kiểm thử dữ liệu người dùng gửi lên theo thời gian thực.

---

## 2. Cấu trúc thư mục dự án

```text
secure-validator-lab/
├── app.py                      # Ứng dụng Web Flask giao diện kiểm thử
├── requirements.txt            # Danh sách thư viện phụ thuộc (Flask, gunicorn)
├── render.yaml                 # Cấu hình triển khai tự động lên Render
├── .gitignore                  # Cấu hình bỏ qua các file tạm/cache
├── securevalidator/            # Gói thư viện xác thực an toàn chính
│   ├── __init__.py             # Export các hàm xác thực và làm sạch
│   └── core.py                 # Mã nguồn hiện thực các logic kiểm tra & lọc dữ liệu
├── templates/
│   └── index.html              # Giao diện kiểm thử trực quan (sử dụng Pico CSS)
├── tests/
│   └── test_validators.py      # Kịch bản kiểm thử tự động (Unit Tests) với unittest
├── images/                     # Ảnh chụp minh chứng thực nghiệm & lỗi ban đầu
│   ├── image1.png              # Minh chứng lỗi chấp nhận phần mở rộng file có số (a.1txt)
│   ├── image2.png              # Minh chứng lỗi chấp nhận dấu chấm trước @ trong email
│   ├── image3.png              # Minh chứng lỗi chấp nhận URL thiếu tên miền chính (http://.com)
│   └── image4.png              # Minh chứng lỗi chấp nhận ký tự đặc biệt trong domain (http://exampl$e.com)
└── README.md                   # Báo cáo thực hành chi tiết
```

---

## 3. Các chức năng & Cơ chế bảo mật (`core.py`)

| Hàm xử lý | Cơ chế bảo vệ kỹ thuật | Mục tiêu ngăn chặn |
| :--- | :--- | :--- |
| `validate_email(email)` | Sử dụng biểu thức chính quy (Regex) nghiêm ngặt tuân thủ RFC; không cho phép dấu chấm `.` ở đầu/cuối phần tên người dùng, chặn dấu chấm liên tiếp (`..`). | Ngăn ngừa dữ liệu rác, lỗi phân giải địa chỉ mail, và nguy cơ tiêm mã độc qua email. |
| `validate_url(url)` | Bắt buộc protocol hợp lệ (`http`/`https`), bóc tách hostname bằng `urllib.parse`, kiểm tra regex tên miền, địa chỉ IP (IPv4) hoặc `localhost`. | Chống giả mạo URL, Open Redirect, SSRF (Server-Side Request Forgery). |
| `validate_filename(filename)` | Kiểm tra chuỗi rỗng, chống Path Traversal (`..`, `/`, `\`), chặn Null Byte (`\x00`), bắt buộc tên file và đuôi file hợp lệ, chặn danh sách đen các đuôi file nguy hiểm (`.exe`, `.php`, `.py`, `.sh`...). | Chống tấn công duyệt thư mục trái phép (Directory Traversal) và tải lên tệp tin độc hại (Malicious File Upload). |
| `sanitize_sql_input(input_str)` | Loại bỏ các ký tự đặc biệt nguy hiểm (`'`, `"`, `--`, `;`, `#`) và xóa các từ khóa nhạy cảm trong câu truy vấn SQL (`OR`, `AND`, `SELECT`, `DROP`, `UNION`...). | Phòng chống tấn công tiêm mã SQL (SQL Injection - SQLi). |
| `sanitize_html_input(html_str)` | Mã hóa toàn bộ các ký tự nhạy cảm trong HTML (`<`, `>`, `&`, `"`, `'`) thông qua `html.escape`. | Ngăn chặn thực thi mã script độc hại (Cross-Site Scripting - XSS). |

---

## 4. Phân tích các lỗi phát hiện ban đầu & Giải pháp khắc phục

Trong quá trình kiểm thử ban đầu, hệ thống đã phát hiện một số lỗi logic và lỗ hổng kiểm duyệt đầu vào (được ghi lại qua các hình ảnh minh chứng dưới đây):

### 4.1. Lỗi định dạng tên tệp tin (Filename Validation)
* **Hiện trạng ban đầu:** Hệ thống cho phép các tệp tin có định dạng mở rộng chứa chữ số hoặc ký tự lạ (ví dụ: `a.1txt`).
* **Rủi ro:** Kẻ tấn công có thể lợi dụng đuôi file bất thường để qua mặt cơ chế kiểm duyệt MIME-type hoặc khai thác lỗi xử lý của web server.
* **Minh chứng ban đầu:**
  ![Minh chứng lỗi Filename](./images/image1.png)  
  *Hình 1: Ban đầu hệ thống đánh giá tệp `a.1txt` là hợp lệ.*
* **Giải pháp khắc phục:** Bổ sung regex chuẩn `^[a-zA-Z0-9_\s-]+\.[a-zA-Z]{2,5}$`, quy định phần mở rộng chỉ được chứa chữ cái (2 đến 5 ký tự) và đối chiếu danh sách phần mở rộng nguy hiểm cần chặn.

---

### 4.2. Lỗi dấu chấm không hợp lệ trong địa chỉ Email
* **Hiện trạng ban đầu:** Hệ thống chấp nhận địa chỉ email có dấu chấm đứng ngay trước ký tự `@` (ví dụ: `nhanlam51204.@gmail.com`).
* **Rủi ro:** Vi phạm tiêu chuẩn cấu trúc RFC 5322; gây lỗi khi hệ thống gửi thư thực tế hoặc làm sai lệch cơ sở dữ liệu người dùng.
* **Minh chứng ban đầu:**
  ![Minh chứng lỗi Email](./images/image2.png)  
  *Hình 2: Email có dấu chấm kết thúc tên tài khoản vẫn được báo hợp lệ.*
* **Giải pháp khắc phục:** Cải tiến biểu thức chính quy thành:
  ```regex
  ^[a-zA-Z0-9_%+-]+(?:\.[a-zA-Z0-9_%+-]+)*@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$
  ```
  Ngăn chặn hoàn toàn dấu chấm xuất hiện ở đầu/cuối của phần local-part và phần domain.

---

### 4.3. Lỗi URL khuyết tên miền chính (Empty Domain Label)
* **Hiện trạng ban đầu:** URL dạng `http://.com` (chỉ có TLD mà không có Second-Level Domain) vẫn được thông qua.
* **Rủi ro:** Xử lý sai đường dẫn, dẫn đến crash ứng dụng khi phân giải DNS hoặc bị khai thác đường dẫn rỗng.
* **Minh chứng ban đầu:**
  ![Minh chứng lỗi URL khuyết domain](./images/image3.png)  
  *Hình 3: URL `http://.com` bị chấp nhận sai.*
* **Giải pháp khắc phục:** Tách `hostname` thông qua `urlparse` và kiểm tra cấu trúc nhãn tên miền bằng regex:
  ```regex
  ^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$
  ```
  Bắt buộc phải có ít nhất một nhãn hợp lệ đứng trước phần mở rộng tên miền.

---

### 4.4. Lỗi URL chứa ký tự đặc biệt nguy hiểm trong Hostname
* **Hiện trạng ban đầu:** URL chứa ký tự đặc biệt lạ trong domain như `http://exampl$e.com` vẫn được xác nhận hợp lệ.
* **Rủi ro:** Tiềm ẩn nguy cơ bypass bộ lọc Web Application Firewall (WAF), HTTP Request Smuggling hoặc Host Header Injection.
* **Minh chứng ban đầu:**
  ![Minh chứng lỗi URL chứa ký tự lạ](./images/image4.png)  
  *Hình 4: URL chứa ký tự `$` trong domain vẫn được báo hợp lệ.*
* **Giải pháp khắc phục:** Quy định chặt chẽ các ký tự trong hostname chỉ bao gồm chữ cái, chữ số và dấu gạch nối `-`, loại bỏ hoàn toàn các ký tự nhạy cảm như `$`, `%`, `#`, `&`...

---

## 5. Hướng dẫn cài đặt & Thực thi (Dành cho Giảng viên)

### Bước 1: Chuẩn bị môi trường & Cài đặt thư viện
Yêu cầu: Đã cài đặt **Python 3.8+**.
Mở terminal tại thư mục gốc của dự án (`secure-validator-lab`) và cài đặt các gói phụ thuộc:
```bash
pip install -r requirements.txt
```

### Bước 2: Chạy kiểm thử tự động (Automated Unit Tests)
Dự án được xây dựng sẵn bộ test case kiểm tra toàn diện tất cả các hàm bảo mật:
```bash
python -m unittest discover tests
```
*Kết quả mong đợi:* Toàn bộ **10/10 test cases** chạy thành công (`Ran 10 tests ... OK`).

### Bước 3: Khởi chạy ứng dụng Web kiểm thử
Khởi chạy máy chủ cục bộ Flask:
```bash
python app.py
```
Truy cập trình duyệt tại địa chỉ: `http://127.0.0.1:5000` để trực tiếp nhập dữ liệu và quan sát kết quả kiểm thực / làm sạch.

---

## 6. Tổng hợp kết quả kiểm thử (Unit Test Results)

| Tên Test Case | Đầu vào thử nghiệm | Mục tiêu kiểm tra | Kết quả thực tế |
| :--- | :--- | :--- | :---: |
| `test_validate_email_valid` | `user@example.com` | Email hợp lệ | **PASSED** (True) |
| `test_validate_email_invalid` | `user@@example..com`, `user.@gmail.com` | Email lỗi định dạng & chứa chấm ở biên | **PASSED** (False) |
| `test_validate_url_valid` | `https://example.com` | URL giao thức https hợp lệ | **PASSED** (True) |
| `test_validate_url_invalid` | `ftp://example.com`, `http://.com`, `http://exampl$e.com` | Protocol lạ, domain rỗng, ký tự `$` | **PASSED** (False) |
| `test_validate_filename_valid` | `report.pdf` | Tên tệp hợp lệ | **PASSED** (True) |
| `test_validate_filename_traversal` | `../../etc/passwd`, `a.1txt`, `shell.php` | Path traversal, đuôi file số, đuôi nguy hiểm `.php` | **PASSED** (False) |
| `test_sanitize_sql_input_injection` | `' OR 1=1 --` | Thử nghiệm SQL Injection | **PASSED** (Đã lọc sạch) |
| `test_sanitize_sql_input_safe_text` | `hello world` | Chuỗi an toàn không bị biến dạng | **PASSED** (Giữ nguyên) |
| `test_sanitize_html_input_script` | `<script>alert("XSS")</script>` | Thử nghiệm XSS Payload | **PASSED** (Đã mã hóa thực thể) |
| `test_sanitize_html_input_safe_text` | `Hello World` | Văn bản thông thường | **PASSED** (Giữ nguyên) |

---

## 7. Kết luận
- Dự án đã hoàn thành đầy đủ các yêu cầu của bài thực hành: Xây dựng cơ chế kiểm thực dữ liệu (Input Validation) và làm sạch dữ liệu (Data Sanitization).
- Đã khắc phục triệt để các trường hợp biên nguy hiểm: dấu chấm biên trong email, cấu trúc hostname sai lệch, ký tự lạ trong URL, và đuôi file không an toàn.
- Hệ thống hoạt động ổn định, vượt qua 100% các kịch bản kiểm thử tự động và hỗ trợ giao diện web trực quan phục vụ đánh giá.
