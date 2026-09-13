# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Đậu Văn Thạch  
> **Mã Sinh Viên / Mã Học viên:** 2A202602592  
> **Chủ đề Lựa chọn:** Trợ lý Học vụ & Tra cứu Lịch thi VinUni  

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 4 / 5 | Bài toán cần tra cứu thông tin Cố vấn học tập trước rồi mới tự động đặt lịch hẹn ở bước tiếp theo. |
| **2. Tool Interaction** | 5 / 5 | Hệ thống bắt buộc kết nối với MCP Server để truy vấn dữ liệu hồ sơ học vụ & ghi nhận đặt lịch tư vấn. |
| **3. Dynamic Decision** | 5 / 5 | Việc xác định tên Cố vấn và tạo lịch hẹn ở bước 2 phụ thuộc hoàn toàn vào kết quả quan sát (Observation) từ bước 1. |
| **4. Long Horizon Goal** | 4 / 5 | Agent duy trì mục tiêu từ tra cứu đến hoàn tất đặt lịch hẹn tư vấn cho sinh viên qua nhiều lượt gọi Tool. |
| **TỔNG ĐIỂM AGENTIC FIT** | **18 / 20** | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật (Gemini API):

```json
[
  {
    "step": 1,
    "query": "đặt lịch tư vấn với sv2026001 vào lúc 10:00 ngày 19/9/2026",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "schedule_appointment",
    "arguments": {
      "student_id": "SV2026001",
      "datetime_str": "10:00 19/09/2026"
    },
    "observation": {
      "status": "SUCCESS",
      "booking_id": "BK-SV2026001-99",
      "student_id": "SV2026001",
      "datetime": "10:00 19/09/2026",
      "advisor": "PGS.TS Nguyễn Văn A",
      "message": "Đặt lịch thành công cho sinh viên SV2026001 với PGS.TS Nguyễn Văn A vào lúc 10:00 19/09/2026."
    },
    "latency_ms": 2219.52
  },
  {
    "step": 2,
    "query": "đặt lịch tư vấn với sv2026001 vào lúc 10:00 ngày 19/9/2026",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Đặt lịch thành công cho sinh viên SV2026001 với PGS.TS Nguyễn Văn A vào lúc 10:00 19/09/2026.",
    "latency_ms": 10.0
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini API - `gemini-3.6-flash`).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 4 lượt.
- **Kết quả đẩy Repo nộp bài:** [x] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
