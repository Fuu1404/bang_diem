# Bảng Điểm Sinh Viên (Flask App)

Ứng dụng quản lý bảng điểm sinh viên viết bằng Python Flask, được cấu hình theo chuẩn **Zero-Configuration Flask** mới nhất của Vercel.

---

## 📁 Cấu trúc dự án

```text
bang_diem/
├── app.py                  # Ứng dụng Flask chính (Bảng điểm & bài tập phụ)
├── sodiem.py               # Bản sao mã nguồn bảng điểm gốc
├── requirements.txt        # Danh sách dependencies cho môi trường Vercel build
├── .gitignore              # Danh sách các file bỏ qua khi commit Git
└── README.md               # Tài liệu hướng dẫn
```

---

## 🚀 Chạy ứng dụng ở môi trường Local

### 1. Kích hoạt môi trường ảo (Virtual Environment)
Trên Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. Cài đặt dependencies (nếu chạy lần đầu)
```powershell
pip install -r requirements.txt
```

### 3. Khởi chạy ứng dụng
```powershell
python app.py
```
Truy cập tại: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🌐 Các tính năng chính

- `/`: Trang chủ tổng quan hệ thống.
- `/students`: Danh sách sinh viên kèm bộ lọc theo lớp (`/students?lop=K47A`).
- `/students/<mssv>`: Xem chi tiết thông tin và bảng điểm môn học của sinh viên.
- `/students/<mssv>/export`: Tải bảng điểm học phần dưới định dạng file CSV.
- `/sv/<mssv>`: Đường dẫn rút gọn tự động redirect (301) về trang chi tiết sinh viên.
- `/search?q=...`: Tìm kiếm sinh viên theo họ tên hoặc MSSV.
- `/api/students`: API trả về danh sách dữ liệu sinh viên định dạng JSON.
- Các route thực hành phụ: `/chia_nhom`, `/square/<n>`, `/sum/<n>`, `/user/<username>`.

---

## ☁️ Hướng dẫn Deploy lên Vercel

Dự án sử dụng cơ chế **Zero-Configuration** chính thức của Vercel dành cho Flask:
- Vercel tự động nhận diện file `app.py` và `requirements.txt`.
- Không cần cấu hình phức tạp hay file rewrites.

### Các bước thực hiện:
1. Push mã nguồn mới lên GitHub:
   ```bash
   git add .
   git commit -m "Switch to Vercel native zero-configuration Flask"
   git push origin main
   ```
2. Vercel sẽ tự động phát hiện commit mới trên nhánh `main`, tiến hành build và cập nhật website live trong vài chục giây.
