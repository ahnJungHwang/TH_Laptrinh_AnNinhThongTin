# BÁO CÁO TỔNG HỢP THỰC HÀNH LẬP TRÌNH AN NINH THÔNG TIN

---

## 📋 THÔNG TIN CHUNG
* **Học phần:** Thực hành Lập trình An ninh Thông tin (Lập trình An toàn Thông tin)
* **Sinh viên thực hiện:** Nhan Huỳnh Lâm
* **Mã số sinh viên (MSSV):** 2387700037
* **Lớp / Nhóm:** ST4 - HK1A_26_27
* **Kho lưu trữ:** `TH_LapTrinhAnNinhThongTin`

---

## 📑 MỤC LỤC
1. [Tổng quan chương trình thực hành](#1-tổng-quan-chương-trình-thực-hành)
2. [Cấu trúc cây thư mục toàn dự án](#2-cấu-trúc-cây-thư-mục-toàn-dự-án)
3. [Bài 1: Cơ sở Lập trình Bảo mật, Kiểm tra Đầu vào & Nhật ký An toàn](#3-bài-1-cơ-sở-lập-trình-bảo-mật-kiểm-tra-đầu-vào--nhật-ký-an-toàn)
   - [Lab 1: Xác thực & Làm sạch dữ liệu đầu vào (Secure Validator)](#lab-1-xác-thực--làm-sạch-dữ-liệu-đầu-vào-secure-validator)
   - [Lab 2: Tự động hóa kiểm tra mã nguồn với Git Hooks (GitSecure)](#lab-2-tự-động-hóa-kiểm-tra-mã-nguồn-với-git-hooks-gitsecure)
   - [Lab 3: Ghi nhật ký ưu tiên bảo mật (Secure Logger)](#lab-3-ghi-nhật-ký-ưu-tiên-bảo-mật-secure-logger)
4. [Bài 2: Mật mã ứng dụng & Triển khai Hạ tầng Khóa công khai (PKI)](#4-bài-2-mật-mã-ứng-dụng--triển-khai-hạ-tầng-khóa-công-khai-pki)
   - [Lab 1: Bộ công cụ mật mã đa năng (Crypto Toolkit)](#lab-1-bộ-công-cụ-mật-mã-đa-năng-crypto-toolkit)
   - [Lab 2: Xây dựng hệ thống thẩm quyền chứng chỉ (Mini-CA)](#lab-2-xây-dựng-hệ-thống-thẩm-quyền-chứng-chỉ-mini-ca)
5. [Bài 3: Bảo mật Mạng, Lập trình Socket An toàn & Trinh sát Mạng](#5-bài-3-bảo-mật-mạng-lập-trình-socket-an-toàn--trinh-sát-mạng)
   - [Lab 1: Ứng dụng trò chuyện an toàn qua SSL/TLS & E2EE (SecureChat)](#lab-1-ứng-dụng-trò-chuyện-an-toàn-qua-ssltls--e2ee-securechat)
   - [Lab 2: Bộ công cụ trinh sát và quét mạng bất đồng bộ (NetRecon)](#lab-2-bộ-công-cụ-trinh-sát-và-quét-mạng-bất-đồng-bộ-netrecon)
6. [Bài 4: Quét Lỗ hổng Ứng dụng Web & Quản lý Xác thực JWT](#6-bài-4-quét-lỗ-hổng-ứng-dụng-web--quản-lý-xác-thực-jwt)
   - [Lab 1: Công cụ quét lỗ hổng Web OWASP Top 10 (Web Vuln Scanner)](#lab-1-công-cụ-quét-lỗ-hổng-web-owasp-top-10-web-vuln-scanner)
   - [Lab 2: Bộ công cụ an toàn và kiểm thử JSON Web Token (JWT Security Tools)](#lab-2-bộ-công-cụ-an-toàn-và-kiểm-thử-json-web-token-jwt-security-tools)
7. [Bài 5: Kiểm thử An ninh Phần mềm – Phân tích Tĩnh (SAST) & Phân tích Động (DAST)](#7-bài-5-kiểm-thử-an-ninh-phần-mềm--phân-tích-tĩnh-sast--phân-tích-động-dast)
   - [Lab 1: Phân tích tĩnh mã nguồn xuất báo cáo chuẩn SARIF (PySAST Tool)](#lab-1-phân-tích-tĩnh-mã-nguồn-xuất-báo-cáo-chuẩn-sarif-pysast-tool)
   - [Lab 2: Giám sát tiến trình thời gian thực và cô lập Sandbox (DAST Tool)](#lab-2-giám-sát-tiến-trình-thời-gian-thực-và-cô-lập-sandbox-dast-tool)
8. [Bài 6: Vận hành Bảo mật với DevSecOps – CI/CD Pipeline trên GitLab](#8-bài-6-vận-hành-bảo-mật-với-devsecops--cicd-pipeline-trên-gitlab)
   - [Lab 6.2.1: Thiết lập và thực thi Pipeline CI/CD đa giai đoạn](#lab-621-thiết-lập-và-thực-thi-pipeline-cicd-đa-giai-đoạn)
   - [Lab 6.2.2: Pipeline CI/CD tự động đóng gói và triển khai Docusaurus lên GitLab Pages](#lab-622-pipeline-cicd-tự-động-đóng-gói-và-triển-khai-docusaurus-lên-gitlab-pages)
9. [Bảng tổng hợp công nghệ & Kỹ thuật an ninh](#9-bảng-tổng-hợp-công-nghệ--kỹ-thuật-an-ninh)
10. [Hướng dẫn cài đặt môi trường chung](#10-hướng-dẫn-cài-đặt-môi-trường-chung)
11. [Tổng kết & Đánh giá kết quả](#11-tổng-kết--đánh-giá-kết-quả)

---

## 1. TỔNG QUAN CHƯƠNG TRÌNH THỰC HÀNH

Chuỗi bài thực hành môn **Lập trình An ninh Thông tin** bao quát trọn vẹn vòng đời phát triển phần mềm an toàn (**SSDLC - Secure Software Development Life Cycle**) và quy trình tích hợp bảo mật tự động (**DevSecOps**), trải dài từ:
- **Tầng mã nguồn (Source Code Layer):** Kiểm tra dữ liệu đầu vào nghiêm ngặt (Validation & Sanitization), ngăn chặn lọt bí mật qua Git Hooks (Secret Scanning), ghi nhật ký bảo mật chuẩn JSON chống sửa đổi (Tamper-Resistant Logging).
- **Tầng mật mã & Định danh (Crypto & Identity Layer):** Ứng dụng các thuật toán chuẩn công nghiệp (AES-256-GCM, Argon2, RSA 2048-bit PKCS#1 v1.5), xây dựng hệ thống chứng thực phân cấp (Root CA, Intermediate CA, CRL Revocation).
- **Tầng mạng & Truyền thông (Network & Transport Layer):** Lập trình Socket bảo mật đa tầng qua kênh truyền mTLS và mã hóa đầu cuối E2EE; trinh sát hệ thống mạng bằng Socket bất đồng bộ (`asyncio`) kết hợp Nmap.
- **Tầng ứng dụng Web & API (Application & API Layer):** Quét tự động các lỗ hổng OWASP Top 10 (XSS, SQLi, CSRF, SSRF); bảo vệ REST API bằng JSON Web Token (Access/Refresh Token) và thực nghiệm tấn công từ điển đa luồng.
- **Tầng kiểm thử an ninh chuyên sâu (Security Testing Layer):** Xây dựng công cụ phân tích tĩnh mã nguồn (SAST - AST Engine, xuất SARIF) và phân tích động (DAST - Runtime Memory/CPU Profiling, Virtual Sandbox).
- **Tầng tự động hóa tích hợp & Triển khai (CI/CD & Deployment Layer):** Tích hợp quy trình kiểm thử và triển khai tự động bảo mật trên GitLab CI/CD Pipeline.

---

## 2. CẤU TRÚC CÂY THƯ MỤC TOÀN DỰ ÁN

```text
TH_LapTrinhAnNinhThongTin/
├── Bai1/
│   ├── Lab1/secure-validator-lab/    # Kiểm tra & làm sạch dữ liệu đầu vào (Flask + Regex)
│   ├── Lab 2/                        # GitSecure Hook (Secret Scanning + SAST Bandit + Logs)
│   └── Lab 3/secure_logger_lab/      # SecureLogger (PII Masking, SHA-256 Sign, Gzip Rotate)
├── Bai2/
│   ├── Lab 1/crypto-toolkit/         # AES-256-GCM, Argon2 Password Hash, RSA-2048 Sign/Verify
│   └── Lab 2/mini-ca/                # Hệ thống CA phân cấp: Root CA, Intermediate CA, X.509 CRL
├── Bai3/
│   ├── Lab1/secure-chat/             # Ứng dụng Chat Socket bảo mật: mTLS + AES-256-CBC E2EE
│   └── Lab2/netrecon/                # Trinh sát mạng: Async Port Scanner, Nmap sV, CVE Checker, Web UI
├── Bai4/
│   ├── Lab1/web-vuln-scanner/        # Quét lỗ hổng Web: XSS, SQL Injection, CSRF, SSRF (Flask UI)
│   └── Lab2/jwt-security-tools/      # Xác thực JWT API Gateway, Token Manager, JWT Cracker từ điển
├── Bai5/
│   ├── Lab1/sast-tool/               # Công cụ phân tích tĩnh AST, regex, Flake8, xuất báo cáo SARIF
│   └── Lab2/dast-tool/               # Phân tích động Runtime Monitor, Memory/Network, Sandbox
├── Bai6/
│   ├── pipeline-tutorial/            # Dự án Docusaurus tích hợp GitLab CI/CD & GitLab Pages
│   └── images/                       # Minh chứng thực nghiệm Lab 6.2.1 và Lab 6.2.2
└── README.md                         # Báo cáo tổng hợp toàn bộ 6 bài thực hành
```

---

## 3. BÀI 1: CƠ SỞ LẬP TRÌNH BẢO MẬT, KIỂM TRA ĐẦU VÀO & NHẬT KÝ AN TOÀN

### Lab 1: Xác thực & Làm sạch dữ liệu đầu vào (Secure Validator)
* **Vị trí thư mục:** [`Bai1/Lab1/secure-validator-lab/`](file:///h:/Nam%204/HK1A/ST4/TH_LapTrinhAnNinhThongTin/Bai1/Lab1/secure-validator-lab)
* **Chi tiết báo cáo:** [`README.md`](file:///h:/Nam%204/HK1A/ST4/TH_LapTrinhAnNinhThongTin/Bai1/Lab1/secure-validator-lab/README.md)
* **Mục tiêu kỹ thuật:**
  - Xây dựng mô-đun lọc và làm sạch dữ liệu tập trung (`securevalidator/core.py`), ngăn chặn các nguy cơ: **SQLi**, **XSS**, **Directory Traversal**, **Open Redirect**, **SSRF**.
  - Xây dựng giao diện web Flask (giao diện Pico CSS) phục vụ kiểm thử tương tác trực tiếp.
* **Cơ chế bảo vệ chính:**
  - `validate_email(email)`: Biểu thức chính quy nghiêm ngặt chuẩn RFC 5322; chặn dấu chấm ở đầu/cuối username và dấu chấm liên tiếp `..`.
  - `validate_url(url)`: Bóc tách bằng `urllib.parse`, ràng buộc giao thức `http`/`https`, kiểm tra tên miền đầy đủ có nhãn hợp lệ, loại trừ ký tự đặc biệt nhạy cảm (`$`, `%`, `#`).
  - `validate_filename(filename)`: Chặn Directory Traversal (`..`, `/`, `\`), chặn ký tự Null Byte (`\x00`), chặn danh sách đen phần mở rộng thực thi nguy hiểm (`.exe`, `.php`, `.py`, `.sh`,...).
  - `sanitize_sql_input(text)`: Loại bỏ ký tự phân cách SQL (`'`, `"`, `;`, `--`, `#`) và xóa từ khóa nhạy cảm (`SELECT`, `DROP`, `UNION`, `OR`, `AND`).
  - `sanitize_html_input(html)`: Mã hóa thực thể HTML (`<`, `>`, `&`, `"`, `'`) qua `html.escape`.
* **Kết quả thực nghiệm:**
  - Vượt qua **10/10 bài kiểm thử tự động** (`python -m unittest discover tests`).
  - Đã khắc phục triệt để các lỗi biên: chấp nhận phần mở rộng số (`a.1txt`), email có dấu chấm biên (`nhanlam51204.@gmail.com`), URL khuyết tên miền (`http://.com`) và ký tự lạ (`http://exampl$e.com`).

---

### Lab 2: Tự động hóa kiểm tra mã nguồn với Git Hooks (GitSecure)
* **Vị trí thư mục:** [`Bai1/Lab 2/`](file:///h:/Nam%204/HK1A/ST4/TH_LapTrinhAnNinhThongTin/Bai1/Lab%202)
* **Chi tiết báo cáo:** [`README.md`](file:///h:/Nam%204/HK1A/ST4/TH_LapTrinhAnNinhThongTin/Bai1/Lab%202/README.md)
* **Mục tiêu kỹ thuật:** Triển khai cơ chế DevSecOps mức cục bộ phía Client (`.githooks/pre-commit`) tự động ngăn chặn commit vi phạm an ninh.
* **Cơ chế kiểm soát của GitSecure:**
  - **Secret Scanner:** Dùng Regex quét các mẫu nhạy cảm như `password`, `token`, `secret`, `apikey`, AWS Key (`AKIA`/`ASIA`). Chặn commit ngay lập tức nếu phát hiện chuỗi hardcoded.
  - **File Permissions:** Dùng `stat` kiểm tra cờ bit `stat.S_IWOTH` (ngăn tệp cấu hình có quyền `world-writable 777`), có xử lý tương thích cho nền tảng Windows (`platform.system() == "Windows"`).
  - **SAST Scanner (Bandit):** Quét mã nguồn với `bandit -r . -x ./.venv` bắt cảnh báo mức nghiêm trọng cao (`SEVERITY: High`).
  - **Audit Logging:** Lưu vết toàn bộ sự cố vi phạm vào `gitsecure.log` có mốc thời gian chi tiết.
* **Kết quả thực nghiệm:**
  - Cấu hình thành công đường dẫn Git hook: `git config core.hooksPath .githooks`.
  - Khi thử nghiệm commit file `pre-commit-hook-test/bad.py` chứa mật khẩu hardcoded (`password = <123456>`), GitSecure lập tức chặn commit với exit code 1 và ghi nhận vào `gitsecure.log`.
  - Sau khi đưa biến vào môi trường (`os.getenv`), hook kiểm tra đạt điều kiện và commit thành công (`GitSecure: All checks passed`).

---

### Lab 3: Ghi nhật ký ưu tiên bảo mật (Secure Logger)
* **Vị trí thư mục:** [`Bai1/Lab 3/secure_logger_lab/`](file:///h:/Nam%204/HK1A/ST4/TH_LapTrinhAnNinhThongTin/Bai1/Lab%203/secure_logger_lab)
* **Chi tiết báo cáo:** [`README.md`](file:///h:/Nam%204/HK1A/ST4/TH_LapTrinhAnNinhThongTin/Bai1/Lab%203/secure_logger_lab/README.md)
* **Mục tiêu kỹ thuật:** Xây dựng module ghi nhật ký tập trung **SecureLogger** phục vụ cho ứng dụng web Flask với tiêu chuẩn bảo vệ dữ liệu cá nhân và toàn vẹn file log.
* **Các đặc tính an ninh nổi bật:**
  - **PII Masking (`mask_pii`):** Tự động phát hiện email $\rightarrow$ `<email_masked>`, token/mật khẩu $\rightarrow$ `<token_masked>` trước khi ghi xuống đĩa, tuân thủ GDPR/PDP.
  - **Chống làm giả nhật ký (Tamper Detection):** Băm từng dòng log bằng thuật toán **SHA-256** và ghi vào tệp chữ ký đối chiếu `secure.log.sig`.
  - **Cấu trúc JSON chuẩn hóa:** Định dạng mỗi bản ghi gồm `timestamp` (UTC ISO-8601 kết thúc `Z`), `level`, `message`, `data`, `results`.
  - **Log Rotation & Gzip:** Tự động xoay vòng tệp log khi đạt dung lượng `MAX_LOG_SIZE = 1MB` và nén các tệp cũ thành `.gz`.
* **Kết quả thực nghiệm:**
  - Tích hợp kiểm thử API `/validate` qua Postman: Khi gửi JSON chứa SQL injection payload và mã script XSS, hệ thống làm sạch dữ liệu thành công đồng thời ghi log JSON đã che giấu PII và sinh mã băm SHA-256 tương ứng.

---

## 4. BÀI 2: MẬT MÃ ỨNG DỤNG & TRIỂN KHAI HẠ TẦNG KHÓA CÔNG KHAI (PKI)

### Lab 1: Bộ công cụ mật mã đa năng (Crypto Toolkit)
* **Vị trí thư mục:** [`Bai2/Lab 1/crypto-toolkit/`](file:///h:/Nam%204/HK1A/ST4/TH_LapTrinhAnNinhThongTin/Bai2/Lab%201/crypto-toolkit)
* **Chi tiết báo cáo:** [`README.md`](file:///h:/Nam%204/HK1A/ST4/TH_LapTrinhAnNinhThongTin/Bai2/Lab%201/crypto-toolkit/README.md)
* **Mục tiêu kỹ thuật:** Xây dựng thư viện mật mã hóa toàn diện `securecrypto` theo chuẩn công nghiệp phục vụ bảo vệ dữ liệu tĩnh và chữ ký điện tử.
* **Kiến trúc các phân hệ mật mã:**
  - **Mã hóa đối xứng (AES-256-GCM):** Phái sinh khóa bằng **PBKDF2HMAC-SHA256** (100,000 vòng lặp) cùng Salt ngẫu nhiên 16 bytes và Nonce 12 bytes (`os.urandom`). Chế độ GCM (Galois/Counter Mode) đảm bảo đồng thời tính bí mật (Confidentiality) và xác thực toàn vẹn (Integrity/Authentication Tag).
  - **Băm mật khẩu (Argon2):** Dùng thuật toán tiên tiến nhất hiện nay (`argon2.PasswordHasher`), chống lại các cuộc tấn công vét cạn bằng GPU/ASIC và bảng băm sẵn (Rainbow Table).
  - **Khóa bất đối xứng & Chữ ký số (RSA 2048-bit):** Sinh cặp khóa RSA với số mũ `e = 65537`, thực hiện ký số và xác minh chữ ký với lược đồ đệm **PKCS#1 v1.5** và hàm băm **SHA-256**.
  - **Đa giao diện tiếp cận:** Cung cấp CLI (`securecrypto-cli`), giao diện đồ họa Desktop (**Tkinter**) và REST API (**Flask**).
* **Kết quả thực nghiệm:**
  - Vượt qua **6/6 bài kiểm thử tự động** qua `pytest tests/`.
  - Mã hóa và giải mã hoàn chỉnh tệp tin `data.txt` qua CLI, GUI và qua Postman (`/encrypt` và `/decrypt`).

---

### Lab 2: Xây dựng hệ thống thẩm quyền chứng chỉ (Mini-CA)
* **Vị trí thư mục:** [`Bai2/Lab 2/mini-ca/`](file:///h:/Nam%204/HK1A/ST4/TH_LapTrinhAnNinhThongTin/Bai2/Lab%202/mini-ca)
* **Chi tiết báo cáo:** [`README.md`](file:///h:/Nam%204/HK1A/ST4/TH_LapTrinhAnNinhThongTin/Bai2/Lab%202/README.md)
* **Mục tiêu kỹ thuật:** Hiện thực hóa kiến trúc hạ tầng khóa công khai PKI phân cấp (Hierarchical PKI) và quản lý vòng đời chứng chỉ số X.509.
* **Quy trình triển khai:**
  1. **Khởi tạo Root CA:** Sinh khóa RSA 2048-bit, tạo chứng chỉ tự ký (Self-signed Root Cert) thời hạn 10 năm, thiết lập `BasicConstraints(ca=True, path_length=1)`.
  2. **Khởi tạo Intermediate CA:** CA trung gian do Root CA ký xác thực, thời hạn 5 năm, thiết lập `BasicConstraints(ca=True, path_length=0)`.
  3. **Cấp phát chứng chỉ End-Entity:** Cấp chứng chỉ cá nhân/máy chủ cho chủ thể **`Nhan_Lam`** (ký bởi Intermediate CA, `ca=False`, thời hạn 1 năm).
  4. **Xác minh chuỗi tin cậy (Chain of Trust):** Hàm `verify_certificate_chain` duyệt ngược chuỗi `Nhan_Lam_cert -> Intermediate CA -> Root CA` dùng khóa công khai tương ứng để xác thực chữ ký SHA-256.
  5. **Thu hồi chứng chỉ & X.509 CRL:** Sinh và ký danh sách thu hồi chứng chỉ `ca_crl.pem`. Hàm `check_revocation_status` kiểm tra số serial và lý do thu hồi (`key_compromise`).
* **Kết quả thực nghiệm:**
  - Kịch bản CLI `demo.py` và giao diện đồ họa Tkinter `demo_ui.py` thực thi trơn tru: Tạo CA $\rightarrow$ Cấp phát chứng chỉ $\rightarrow$ Kiểm tra chuỗi hợp lệ (`True`) $\rightarrow$ Thu hồi chứng chỉ $\rightarrow$ Kiểm tra trạng thái báo `Revoked`.
  - Cấu hình an toàn `.gitignore` ngăn ngừa tuyệt đối việc rò rỉ private keys (`certs/*.pem`) lên Git.

---

## 5. BÀI 3: BẢO MẬT MẠNG, LẬP TRÌNH SOCKET AN TOÀN & TRINH SÁT MẠNG

### Lab 1: Ứng dụng trò chuyện an toàn qua SSL/TLS & E2EE (SecureChat)
* **Vị trí thư mục:** [`Bai3/Lab1/secure-chat/`](file:///h:/Nam%204/HK1A/ST4/TH_LapTrinhAnNinhThongTin/Bai3/Lab1/secure-chat)
* **Chi tiết báo cáo:** [`README.md`](file:///h:/Nam%204/HK1A/ST4/TH_LapTrinhAnNinhThongTin/Bai3/Lab1/README.md)
* **Mục tiêu kỹ thuật:** Thiết lập kênh truyền thông bảo mật hai chiều qua Socket Python, chống tấn công nghe lén (Eavesdropping) và tấn công xen giữa (MITM).
* **Kiến trúc bảo mật 2 lớp:**
  - **Lớp giao vận (Transport Layer Security - mTLS):** Cấu hình `ssl.CERT_REQUIRED` bắt buộc xác thực hai chiều giữa Server và Client bằng bộ chứng chỉ số cấp bởi Root CA riêng biệt (sinh bằng OpenSSL).
  - **Lớp ứng dụng (Application Layer - E2EE):** Mỗi client sinh khóa đối xứng **AES-256** riêng biệt, mã hóa gói tin với chế độ **CBC** kết hợp đệm dữ liệu **PKCS7** và IV 16 bytes ngẫu nhiên cho từng tin nhắn.
  - **Hệ thống điều phối:** Server xử lý đa luồng (`threading`), quản lý phiên (`ConnectionManager`) và phòng chat (`RoomManager`), giải mã tin nhắn từ client gửi và mã hóa lại bằng khóa của các client nhận trước khi phân phối.
* **Kết quả thực nghiệm:**
  - Khởi chạy Server lắng nghe tại `127.0.0.1:8443`.
  - Client 1 (`lam`) và Client 2 (`ty`) kết nối, bắt tay TLS thành công và trao đổi thông điệp trực tiếp với nội dung được mã hóa hoàn toàn trên đường truyền mạng.

---

### Lab 2: Bộ công cụ trinh sát và quét mạng bất đồng bộ (NetRecon)
* **Vị trí thư mục:** [`Bai3/Lab2/netrecon/`](file:///h:/Nam%204/HK1A/ST4/TH_LapTrinhAnNinhThongTin/Bai3/Lab2/netrecon)
* **Chi tiết báo cáo:** [`README.md`](file:///h:/Nam%204/HK1A/ST4/TH_LapTrinhAnNinhThongTin/Bai3/Lab2/README.md)
* **Mục tiêu kỹ thuật:** Xây dựng bộ công cụ trinh sát mạng chuyên nghiệp phục vụ kiểm thử xâm nhập (Penetration Testing) và đánh giá an ninh hạ tầng mạng.
* **Các module cốt lõi:**
  - **Port Scanner bất đồng bộ (`asyncio`):** Quét hàng loạt cổng mạng đồng thời sử dụng `asyncio.Semaphore(100)` để kiểm soát tốc độ (Rate Limiting), tránh gây nghẽn băng thông hoặc kích hoạt hệ thống IDS/IPS.
  - **Service Detector:** Tích hợp công cụ **Nmap (`nmap -sV`)** thông qua `subprocess` để nhận dạng chính xác tên dịch vụ và phiên bản chi tiết đang chạy trên cổng mở.
  - **Banner Grabber:** Kết nối TCP Socket với timeout 2 giây thu thập chuỗi dữ liệu chào đầu tiên từ dịch vụ mục tiêu.
  - **Network Mapper:** Thu thập bảng ARP nội bộ (`arp -a`) để lập bản đồ các thiết bị trong mạng LAN mà không cần gửi gói tin chủ động.
  - **Vuln Checker:** Tự động đối soát cổng và dịch vụ với cơ sở dữ liệu lỗ hổng đã biết (**CVE Alert**).
  - **Web UI & Email Alert:** Xây dựng giao diện web Flask và gửi thông báo kết quả quét tự động qua giao thức **SMTP over SSL** (Google App Password).
* **Kết quả thực nghiệm:**
  - Quét thành công máy chủ thử nghiệm `scanme.nmap.org` trên cổng 22, 80: Nhận dạng chính xác `OpenSSH 6.6.1p1` và `Apache httpd 2.4.7`.
  - Giao diện Web tiếp nhận yêu cầu quét và gửi email báo cáo chi tiết về hộp thư Gmail người dùng.

---

## 6. BÀI 4: QUÉT LỖ HỔNG ỨNG DỤNG WEB & QUẢN LÝ XÁC THỰC JWT

### Lab 1: Công cụ quét lỗ hổng Web OWASP Top 10 (Web Vuln Scanner)
* **Vị trí thư mục:** [`Bai4/Lab1/web-vuln-scanner/`](file:///h:/Nam%204/HK1A/ST4/TH_LapTrinhAnNinhThongTin/Bai4/Lab1/web-vuln-scanner)
* **Chi tiết báo cáo:** [`README.md`](file:///h:/Nam%204/HK1A/ST4/TH_LapTrinhAnNinhThongTin/Bai4/Lab1/web-vuln-scanner/README.md)
* **Mục tiêu kỹ thuật:** Xây dựng công cụ tự động kiểm tra bảo mật ứng dụng web nhằm phát hiện sớm các nguy cơ nghiêm trọng thuộc danh mục OWASP Top 10.
* **Các module phát hiện lỗ hổng:**
  - **XSS Scanner:** Kiểm tra việc phản xạ payload mã script JavaScript trong phản hồi HTML.
  - **SQL Injection Tester:** Thử nghiệm chèn các mẫu truy vấn kinh điển (`' OR '1'='1`) và kiểm tra dấu hiệu lỗi cơ sở dữ liệu trả về.
  - **CSRF Detector:** Phân tích cú pháp form HTML, cảnh báo thiếu thuộc tính token chống giả mạo yêu cầu chéo trang.
  - **SSRF Tester:** Bóc tách URL đích, phát hiện hành vi cố ý gọi vào các địa chỉ mạng nội bộ hoặc dải loopback (`127.0.0.1`, `localhost`, IP Private).
  - **Risk Assessment:** Module `report_generator.py` chấm điểm và phân loại rủi ro (Low, Medium, High).
* **Kết quả thực nghiệm:**
  - Vượt qua **9/9 test cases** tự động bằng `unittest`.
  - Quét qua CLI và giao diện Web Flask phát hiện chính xác lỗ hổng SSRF mức độ High và lỗ hổng thiếu token CSRF mức độ Medium.

---

### Lab 2: Bộ công cụ an toàn và kiểm thử JSON Web Token (JWT Security Tools)
* **Vị trí thư mục:** [`Bai4/Lab2/jwt-security-tools/`](file:///h:/Nam%204/HK1A/ST4/TH_LapTrinhAnNinhThongTin/Bai4/Lab2/jwt-security-tools)
* **Chi tiết báo cáo:** [`README.md`](file:///h:/Nam%204/HK1A/ST4/TH_LapTrinhAnNinhThongTin/Bai4/Lab2/jwt-security-tools/README.md)
* **Mục tiêu kỹ thuật:** Xây dựng hệ thống xác thực stateless bảo mật bằng JWT và thực nghiệm tấn công rà soát khóa bí mật (Dictionary Attack).
* **Các module hệ thống:**
  - **Token Manager:** Cấp phát cặp Access Token (hạn 15 phút) và Refresh Token (hạn 24 giờ); hỗ trợ cơ chế cấp mới token không lưu trạng thái.
  - **API Gateway:** Đóng vai trò lớp bảo vệ (Reverse Proxy) kiểm tra header `Authorization: Bearer <token>`, chỉ cho phép truy cập route `/protected` khi token hợp lệ.
  - **JWT Validator:** Xác thực tính hợp lệ của chữ ký số HMAC-SHA256, kiểm tra thời hạn sống (`exp`) và cấu trúc claim.
  - **JWT Cracker:** Công cụ bẻ khóa đa luồng (Multi-threaded Dictionary Attack) thử nghiệm với danh sách từ điển `words.txt`.
  - **Secure Coding:** Nạp khóa bí mật qua biến môi trường (`os.getenv`), loại bỏ hoàn toàn các chuỗi hardcoded secrets.
* **Kết quả thực nghiệm:**
  - Đạt **7/7 passed tests** qua `pytest`.
  - Thử nghiệm tấn công từ điển bẻ khóa thành công secret key yếu (`password123`), minh chứng sự cần thiết của việc sử dụng khóa có độ dài tối thiểu 256 bits theo RFC 7518.

---

## 7. BÀI 5: KIỂM THỬ AN NINH PHẦN MỀM – PHÂN TÍCH TĨNH (SAST) & PHÂN TÍCH ĐỘNG (DAST)

### Lab 1: Phân tích tĩnh mã nguồn xuất báo cáo chuẩn SARIF (PySAST Tool)
* **Vị trí thư mục:** [`Bai5/Lab1/sast-tool/`](file:///h:/Nam%204/HK1A/ST4/TH_LapTrinhAnNinhThongTin/Bai5/Lab1/sast-tool)
* **Chi tiết báo cáo:** [`README.md`](file:///h:/Nam%204/HK1A/ST4/TH_LapTrinhAnNinhThongTin/Bai5/Lab1/README.md)
* **Mục tiêu kỹ thuật:** Xây dựng công cụ phân tích tĩnh mã nguồn Python (**PySAST**) phát hiện lỗi bảo mật và vi phạm quy chuẩn code, xuất báo cáo định dạng chuẩn công nghiệp **SARIF**.
* **Cơ chế phân tích:**
  - **AST Analyzer:** Duyệt cây cú pháp trừu tượng (Abstract Syntax Tree) của Python để phát hiện chính xác việc triệu gọi các hàm cực kỳ nguy hiểm như `eval()`, `exec()`, `subprocess(shell=True)`.
  - **Vuln Pattern Matcher:** Quét regex phát hiện hardcoded password, API key và chuỗi nhạy cảm.
  - **Code Quality Checker:** Tích hợp `flake8` kiểm tra các lỗi định dạng chuẩn PEP 8.
  - **SARIF Reporter:** Chuẩn hóa toàn bộ lỗi phát hiện được ra định dạng `report.sarif`.
* **Kết quả thực nghiệm:**
  - Cài đặt extension **SARIF Viewer** (Microsoft DevLabs) trên VSCode để hiển thị cảnh báo an ninh trực quan ngay trong IDE.
  - Quét `vulnerable_01.py` phát hiện 8 vấn đề, quét `vulnerable_02.py` phát hiện 4 vấn đề; vượt qua **6/6 bài unit test**.

---

### Lab 2: Giám sát tiến trình thời gian thực và cô lập Sandbox (DAST Tool)
* **Vị trí thư mục:** [`Bai5/Lab2/dast-tool/`](file:///h:/Nam%204/HK1A/ST4/TH_LapTrinhAnNinhThongTin/Bai5/Lab2/dast-tool)
* **Chi tiết báo cáo:** [`README.md`](file:///h:/Nam%204/HK1A/ST4/TH_LapTrinhAnNinhThongTin/Bai5/Lab2/README.md)
* **Mục tiêu kỹ thuật:** Xây dựng công cụ kiểm thử động phân tích hành vi chương trình trong lúc thực thi (Runtime Application Self-Protection / DAST).
* **Các thành phần chức năng:**
  - **Runtime Monitor (`psutil`):** Theo dõi mức chiếm dụng CPU, bộ nhớ RAM và các tệp tin đang mở (Open Files) của tiến trình theo PID.
  - **Memory Analyzer:** Sử dụng bộ thu gom rác `gc` phát hiện rò rỉ bộ nhớ (Memory Leaks) và kiểm tra các giới hạn số học (Integer Overflow).
  - **Network Traffic Analyzer:** Giám sát lưu lượng gói tin gửi/nhận qua card mạng.
  - **Security Behavior Checker:** Theo dõi và bắt kịp thời các hành vi gọi hàm nhạy cảm ở thời gian chạy như `os.system()`, `eval()`.
  - **Virtual Sandbox:** Thiết lập không gian thư mục tạm cô lập để thực thi các lệnh chưa được kiểm chứng một cách an toàn.
  - **RESTful API:** Cung cấp các endpoint `/api/monitor`, `/api/memory`, `/api/network`, `/api/security`, `/api/sandbox`.
* **Kết quả thực nghiệm:**
  - Chạy phân tích CLI đầy đủ thông số; vượt qua **5/5 bài kiểm thử tự động** trong 1.067s.
  - Máy chủ Flask khởi chạy thành công tại cổng 5000 sẵn sàng nhận lệnh kiểm thử từ xa.

---

## 8. BÀI 6: VẬN HÀNH BẢO MẬT VỚI DEVSECOPS – CI/CD PIPELINE TRÊN GITLAB

* **Vị trí thư mục:** [`Bai6/`](file:///h:/Nam%204/HK1A/ST4/TH_LapTrinhAnNinhThongTin/Bai6)
* **Chi tiết báo cáo:** [`README.md`](file:///h:/Nam%204/HK1A/ST4/TH_LapTrinhAnNinhThongTin/Bai6/README.md)

### Lab 6.2.1: Thiết lập và thực thi Pipeline CI/CD đa giai đoạn
* **Mục tiêu:** Nắm vững cấu trúc tệp `.gitlab-ci.yml`, các chỉ thị `stages`, `script`, `environment`, và biến môi trường định sẵn.
* **Cấu hình Pipeline:**
  - Định nghĩa 3 stages: `build`, `test`, `deploy`.
  - Khởi tạo 4 jobs:
    - `build-job`: In thông báo chào mừng `$GITLAB_USER_LOGIN`.
    - `test-job1` & `test-job2`: Chạy song song trong stage test (trong đó `test-job2` thử nghiệm mô phỏng độ trễ với `sleep 20`).
    - `deploy-prod`: Triển khai môi trường `production` trên nhánh `$CI_COMMIT_BRANCH`.
* **Kết quả:** Pipeline `#2997084553` đạt trạng thái **Passed** 100%, kiểm tra chi tiết Job logs hiển thị đầy đủ thông tin thực thi của từng runner.

---

### Lab 6.2.2: Pipeline CI/CD tự động đóng gói và triển khai Docusaurus lên GitLab Pages
* **Mục tiêu:** Xây dựng pipeline phức tạp kết hợp Docker container (`image: node`) để tự động đóng gói và xuất bản trang tài liệu web tĩnh.
* **Quy trình triển khai:**
  1. Khởi tạo mã nguồn Docusaurus, cấu hình `baseUrl: '/lam-pipeline-tutorial-project/'` và `url: 'https://devsecops-lab2981744.gitlab.io/'`.
  2. Nâng cấp cấu hình `.gitlab-ci.yml` qua 3 phiên bản:
     - Thử nghiệm kết nối runner (`test-job`).
     - Tự động đóng gói (`build-job`): Chạy `npm install` và `npm run build`, lưu kết quả vào thư mục `artifacts: paths: - "build/"`.
     - Tự động xuất bản (`pages`): Chuyển đổi `build/` thành `public/` và đẩy lên dịch vụ **GitLab Pages**.
* **Kết quả:** Trang web **Docusaurus (`My Site - Dinosaurs are cool`)** được triển khai thành công tại địa chỉ trực tuyến:  
  `https://lam-pipeline-tutorial-project-38f8b1.gitlab.io`

---

## 9. BẢNG TỔNG HỢP CÔNG NGHỆ & KỸ THUẬT AN NINH

| Bài thực hành | Phân hệ / Dự án | Kỹ thuật & Thuật toán Bảo mật | Giao diện hỗ trợ | Kết quả kiểm thử |
| :---: | :--- | :--- | :---: | :---: |
| **Bài 1** | Secure Validator | Regex RFC 5322, Path Traversal Check, SQL Sanitizer, HTML Escape | Flask Web UI | **10/10 Unit Tests** |
| | GitSecure Hook | Client-side Hook, Secret Scanning, File Permissions, Bandit SAST | CLI / Git Hook | **Chặn commit vi phạm** |
| | Secure Logger | PII Masking, SHA-256 Tamper Proofing, JSON ISO-8601, Gzip Rotate | REST API Flask | **Toàn vẹn tệp log** |
| **Bài 2** | Crypto Toolkit | AES-256-GCM, PBKDF2HMAC (100k rounds), Argon2 Hashing, RSA-2048 PKCS#1 v1.5 | CLI, GUI Tkinter, REST API | **6/6 Pytest (100%)** |
| | Mini-CA | PKI phân cấp (Root $\rightarrow$ Inter $\rightarrow$ End-Entity), X.509 CRL, Chain of Trust | CLI, GUI Tkinter | **Xác thực & Thu hồi OK** |
| **Bài 3** | SecureChat | Mutual TLS (mTLS) `CERT_REQUIRED`, AES-256-CBC E2EE, OpenSSL | Multi-threaded Socket | **Chống nghe lén, MITM** |
| | NetRecon Toolkit | Asyncio Port Scanner, Rate Limiting Semaphore, Nmap `-sV`, CVE Mapping, SMTP SSL | CLI, Flask Web UI | **Quét chính xác + Báo email** |
| **Bài 4** | Web Vuln Scanner | XSS Detection, SQLi Testing, CSRF Check, SSRF Detection, Risk Scorer | CLI, Flask Web UI | **9/9 Unit Tests** |
| | JWT Security Tools | Token Manager (Access/Refresh), API Gateway Bearer, Cracker từ điển đa luồng | CLI, Flask API | **7/7 Pytest (100%)** |
| **Bài 5** | PySAST Tool | AST Engine (`eval`/`exec`), Regex Rule Matcher, Flake8 Linter, Chuẩn SARIF | CLI, SARIF Viewer (VSCode) | **6/6 Unit Tests** |
| | DAST Tool | Runtime Monitor (`psutil`), Memory Leaks/Overflow, Virtual Sandbox cô lập | CLI, Flask REST API | **5/5 Unit Tests** |
| **Bài 6** | GitLab CI/CD | Pipeline 3 stages (`build`, `test`, `deploy`), Runner Container, Docusaurus Pages | GitLab Cloud Web | **Pipelines Passed 100%** |

---

## 10. HƯỚNG DẪN CÀI ĐẶT MÔI TRƯỜNG CHUNG

### 10.1. Yêu cầu hệ thống
- **Hệ điều hành:** Windows 10/11 64-bit hoặc Linux/macOS.
- **Python:** Phiên bản 3.10 trở lên (khuyến nghị Python 3.12).
- **Node.js:** Phiên bản 18+ (phục vụ Bài 6 Docusaurus).
- **Công cụ phụ trợ:**
  - **Git** (đã cấu hình User Email & Name).
  - **OpenSSL** (đã thêm vào biến môi trường `PATH`).
  - **Nmap** (đã cài đặt kèm Npcap).

### 10.2. Tạo và kích hoạt môi trường ảo Python
Khuyến nghị tạo môi trường ảo tại thư mục gốc để quản lý thư viện tập trung:
```powershell
# Tạo môi trường ảo
python -m venv .venv

# Kích hoạt trên PowerShell
.\.venv\Scripts\Activate.ps1

# Hoặc trên Command Prompt (cmd)
.\.venv\Scripts\activate.bat
```

### 10.3. Cài đặt các thư viện phụ thuộc chính
```powershell
pip install flask cryptography argon2-cffi pyjwt requests psutil click flake8 sarif-om jsonpickle python-dotenv pytest bandit
```

---

## 11. TỔNG KẾT & ĐÁNH GIÁ KẾT QUẢ

Qua 6 bài thực hành chuyên sâu về **Lập trình An ninh Thông tin**, sinh viên đã:
1. **Làm chủ tư duy Lập trình An toàn (Secure Coding):** Luôn coi dữ liệu đầu vào là không tin cậy, chủ động lọc sạch dữ liệu, áp dụng kỹ thuật che giấu thông tin định danh cá nhân và băm bảo vệ tính toàn vẹn của tệp nhật ký.
2. **Nắm vững kỹ thuật Mật mã học ứng dụng:** Sử dụng thành thạo các thuật toán hiện đại bảo vệ dữ liệu cả lúc lưu trữ (At-Rest) và lúc truyền tải (In-Transit), làm chủ quy trình phát hành, thẩm định và thu hồi chứng chỉ số trong hạ tầng khóa công khai PKI.
3. **Thành thạo kỹ năng Kiểm thử An ninh Đa tầng:** Tự phát triển các công cụ phát hiện lỗ hổng web OWASP, xây dựng bộ phân tích tĩnh mã nguồn SAST dựa trên cây cú pháp trừu tượng AST và bộ phân tích động DAST giám sát tài nguyên tiến trình trong môi trường cô lập Sandbox.
4. **Hiện thực hóa văn hóa DevSecOps:** Tự động hóa kiểm tra mã nguồn tại máy lập trình viên qua Git Hooks, loại bỏ triệt để hardcoded secrets và tích hợp quy trình kiểm thử/triển khai liên tục an toàn trên hệ thống GitLab CI/CD.

Toàn bộ các bài thực hành đều hoàn thành đầy đủ các yêu cầu kỹ thuật của giáo trình, đạt tỷ lệ vượt qua bài kiểm thử tự động **100%**, có đầy đủ tài liệu hướng dẫn và ảnh chụp minh chứng thực nghiệm trong từng thư mục dự án.

