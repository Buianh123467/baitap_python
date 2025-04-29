import json
import os

class Student:
    def __init__(self, name, mssv, lop, phone, dob, address):
        self.name = name
        self.mssv = mssv
        self.lop = lop
        self.phone = phone
        self.dob = dob
        self.address = address

    def to_dict(self):
        return {
            "Họ tên": self.name,
            "MSSV": self.mssv,
            "Lớp": self.lop,
            "SĐT": self.phone,
            "Ngày sinh": self.dob,
            "Địa chỉ hiện tại": self.address
        }

class Family(Student):
    def __init__(self, name, mssv, lop, phone, dob, address, home_address, father_name, mother_name):
        super().__init__(name, mssv, lop, phone, dob, address)
        self.home_address = home_address
        self.father_name = father_name
        self.mother_name = mother_name

    def to_dict(self):
        return {
            "Thông tin sinh viên": super().to_dict(),
            "Thông tin gia đình": {
                "Địa chỉ gia đình": self.home_address,
                "Họ tên bố": self.father_name,
                "Họ tên mẹ": self.mother_name
            }
        }

class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data
        return []

    def save_students(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.students, f, indent=4, ensure_ascii=False)

    def add_student(self, family: Family):
        new_id = max([item["id"] for item in self.students], default=0) + 1
        student_data = {"id": new_id}
        student_data.update(family.to_dict())
        self.students.append(student_data)
        self.save_students()

    def update_student(self, student_id, updated_data):
        for student in self.students:
            if student["id"] == student_id:
                student.update(updated_data)
                self.save_students()
                return True
        return False

    def delete_student(self, student_id):
        self.students = [s for s in self.students if s["id"] != student_id]
        self.save_students()

    def get_all_students(self):
        return self.students

# --- Example usage ---
if __name__ == "__main__":
    manager = StudentManager()

    # Thêm sinh viên mới
    sv = Family(
        name="Nguyen Van A",
        mssv="12345678",
        lop="DHKTPM16A",
        phone="0123456789",
        dob="2002-01-01",
        address="KTX khu B",
        home_address="123 Đường Quê",
        father_name="Nguyen Van B",
        mother_name="Tran Thi C"
    )
    manager.add_student(sv)

    # Xem danh sách
    for s in manager.get_all_students():
        print(json.dumps(s, indent=4, ensure_ascii=False))
