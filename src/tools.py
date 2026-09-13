"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    # Tool 1: Tra cứu hồ sơ học vụ sinh viên
    {
        "name": "academic_query",
        "description": "Tra cứu hồ sơ và thông tin học vụ của sinh viên VinUni bằng mã sinh viên. Trả về thông tin cá nhân, GPA, lớp, email, trạng thái học tập, cố vấn học tập và danh sách môn đang học.",
        "parameters": {
            "type": "object",
            "properties": {
                "student_id": {
                    "type": "string",
                    "description": "Mã sinh viên cần tra cứu (ví dụ: 'SV2026001')"
                }
            },
            "required": ["student_id"]
        }
    },

    # Tool 2: Đặt lịch hẹn tư vấn học vụ
    {
        "name": "schedule_appointment",
        "description": "Đặt lịch hẹn tư vấn học vụ với Cố vấn học tập VinUni. Lưu ý: Sinh viên phải tồn tại trong hệ thống mới có thể đặt lịch.",
        "parameters": {
            "type": "object",
            "properties": {
                "student_id": {
                    "type": "string",
                    "description": "Mã sinh viên cần đặt lịch (ví dụ: 'SV2026001')"
                },
                "datetime_str": {
                    "type": "string",
                    "description": "Thời gian đặt lịch hẹn (ví dụ: '14:00 15/09/2026')"
                },
                "advisor_name": {
                    "type": "string",
                    "description": "Tên cố vấn học tập (ví dụ: 'PGS.TS Nguyễn Văn A')"
                }
            },
            "required": ["student_id", "datetime_str"]
        }
    },

    # Tool 3: Tra cứu lịch thi của sinh viên
    {
        "name": "exam_schedule_query",
        "description": "Tra cứu lịch thi của sinh viên VinUni bằng mã sinh viên. Trả về danh sách các môn thi kèm ngày, giờ và phòng thi.",
        "parameters": {
            "type": "object",
            "properties": {
                "student_id": {
                    "type": "string",
                    "description": "Mã sinh viên cần tra cứu lịch thi (ví dụ: 'SV2026001')"
                }
            },
            "required": ["student_id"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_DATABASE = {
    "SV2026001": {
        "full_name": "Nguyễn Văn An",
        "class": "AI-K4",
        "gpa": 3.85,
        "email": "an.nv@vinuni.edu.vn",
        "status": "Đang học",
        "advisor": "PGS.TS Nguyễn Văn A",
        "courses": ["Trí tuệ Nhân tạo", "Machine Learning", "Xác suất Thống kê"],
        "exam_schedule": [
            {"course": "Trí tuệ Nhân tạo", "date": "20/09/2026", "time": "08:00", "room": "B201"},
            {"course": "Machine Learning", "date": "22/09/2026", "time": "13:30", "room": "A305"},
            {"course": "Xác suất Thống kê", "date": "25/09/2026", "time": "09:00", "room": "C102"}
        ]
    },
    "SV2026002": {
        "full_name": "Trần Thị Bình",
        "class": "AI-K4",
        "gpa": 3.60,
        "email": "binh.tt@vinuni.edu.vn",
        "status": "Đang học",
        "advisor": "TS. Lê Thị B",
        "courses": ["Deep Learning", "Xử lý Ngôn ngữ Tự nhiên", "Toán Rời rạc"],
        "exam_schedule": [
            {"course": "Deep Learning", "date": "21/09/2026", "time": "08:00", "room": "A201"},
            {"course": "Xử lý Ngôn ngữ Tự nhiên", "date": "23/09/2026", "time": "14:00", "room": "B102"},
            {"course": "Toán Rời rạc", "date": "26/09/2026", "time": "10:00", "room": "C201"}
        ]
    },
    "SV2026003": {
        "full_name": "Lê Hoàng Cường",
        "class": "CS-K4",
        "gpa": 3.42,
        "email": "cuong.lh@vinuni.edu.vn",
        "status": "Đang học",
        "advisor": "PGS.TS Nguyễn Văn A",
        "courses": ["Cấu trúc Dữ liệu", "Lập trình Web", "Cơ sở Dữ liệu"],
        "exam_schedule": [
            {"course": "Cấu trúc Dữ liệu", "date": "19/09/2026", "time": "08:00", "room": "A101"},
            {"course": "Lập trình Web", "date": "24/09/2026", "time": "13:00", "room": "B303"},
            {"course": "Cơ sở Dữ liệu", "date": "27/09/2026", "time": "09:30", "room": "A205"}
        ]
    },
    "SV2026004": {
        "full_name": "Phạm Thị Dung",
        "class": "BA-K4",
        "gpa": 3.70,
        "email": "dung.pt@vinuni.edu.vn",
        "status": "Đang học",
        "advisor": "TS. Lê Thị B",
        "courses": ["Quản trị Kinh doanh", "Marketing số", "Kinh tế Vi mô"],
        "exam_schedule": [
            {"course": "Quản trị Kinh doanh", "date": "20/09/2026", "time": "14:00", "room": "D101"},
            {"course": "Marketing số", "date": "23/09/2026", "time": "08:30", "room": "D203"},
            {"course": "Kinh tế Vi mô", "date": "26/09/2026", "time": "13:00", "room": "D105"}
        ]
    },
    "SV2026005": {
        "full_name": "Hoàng Minh Đức",
        "class": "AI-K4",
        "gpa": 2.95,
        "email": "duc.hm@vinuni.edu.vn",
        "status": "Cảnh báo học vụ",
        "advisor": "PGS.TS Nguyễn Văn A",
        "courses": ["Trí tuệ Nhân tạo", "Giải tích 2", "Vật lý Đại cương"],
        "exam_schedule": [
            {"course": "Trí tuệ Nhân tạo", "date": "20/09/2026", "time": "08:00", "room": "B201"},
            {"course": "Giải tích 2", "date": "24/09/2026", "time": "10:00", "room": "C301"},
            {"course": "Vật lý Đại cương", "date": "28/09/2026", "time": "08:00", "room": "A102"}
        ]
    }
}


def execute_academic_query(student_id: str) -> str:
    """Thực thi tra cứu học vụ theo mã sinh viên"""
    student = MOCK_DATABASE.get(student_id.strip().upper())
    if student:
        # Trả về thông tin cơ bản (không bao gồm lịch thi — dùng tool riêng)
        data = {
            "full_name": student["full_name"],
            "class": student["class"],
            "gpa": student["gpa"],
            "email": student["email"],
            "status": student["status"],
            "advisor": student["advisor"],
            "courses": student["courses"]
        }
        return json.dumps({
            "status": "SUCCESS",
            "student_id": student_id,
            "data": data
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy dữ liệu sinh viên có mã '{student_id}'"
        }, ensure_ascii=False)


def execute_exam_schedule_query(student_id: str) -> str:
    """Thực thi tra cứu lịch thi theo mã sinh viên"""
    student = MOCK_DATABASE.get(student_id.strip().upper())
    if student:
        return json.dumps({
            "status": "SUCCESS",
            "student_id": student_id,
            "full_name": student["full_name"],
            "exam_schedule": student.get("exam_schedule", [])
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy lịch thi của sinh viên có mã '{student_id}'"
        }, ensure_ascii=False)


def execute_schedule_appointment(student_id: str, datetime_str: str, advisor_name: str = "PGS.TS Nguyễn Văn A") -> str:
    """Thực thi đặt lịch hẹn tư vấn học vụ — kiểm tra sinh viên tồn tại trước khi đặt lịch"""
    student = MOCK_DATABASE.get(student_id.strip().upper())
    if not student:
        return json.dumps({
            "status": "STUDENT_NOT_FOUND",
            "message": f"Không thể đặt lịch: sinh viên '{student_id}' không tồn tại trong hệ thống."
        }, ensure_ascii=False)

    return json.dumps({
        "status": "SUCCESS",
        "booking_id": f"BK-{student_id}-{hash(datetime_str) % 1000:03d}",
        "student_id": student_id,
        "student_name": student["full_name"],
        "datetime": datetime_str,
        "advisor": advisor_name,
        "message": f"Đặt lịch thành công cho sinh viên {student['full_name']} ({student_id}) với {advisor_name} vào lúc {datetime_str}."
    }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "academic_query": execute_academic_query,
    "schedule_appointment": execute_schedule_appointment,
    "exam_schedule_query": execute_exam_schedule_query
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)
