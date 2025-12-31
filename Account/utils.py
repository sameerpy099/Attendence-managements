import random
import string
from Student.models import student_basic_detail
from TransportDomain.models import Transport_Mem
from Faculty.models import Facultyman

# Generate unique Student ID
def generate_unique_student_id():
    while True:
        sid = "ST000" + ''.join(random.choices(string.digits, k=8))
        if not student_basic_detail.objects.filter(student_id=sid).exists():
            return sid
def generate_unique_Faculty_id():
    while True:
        sid = "FAC000" + ''.join(random.choices(string.digits, k=8))
        if not Facultyman.objects.filter(faculty_id=sid).exists():
            return sid
def generate_unique_transport_id():
    while True:
        sid = "TRA000" + ''.join(random.choices(string.digits, k=8))
        if not Transport_Mem.objects.filter(Driver_id=sid).exists():
            return sid

# Generate random password
def generate_random_password(length=10):
    chars = string.ascii_letters + string.digits  # letters + numbers
    return ''.join(random.choice(chars) for _ in range(length))
