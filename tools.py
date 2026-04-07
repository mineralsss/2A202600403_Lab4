from langchain_core.tools import tool
import re

# MOCK DATA
# Dữ liệu giả lập hệ thống du lịch
# Lưu ý: Giá cả có logic (VD: cuối tuần đắt hơn, hạng cao hơn đắt hơn)
# Sinh viên cần đọc hiểu data để debug test cases.
# ==

FLIGHTS_DB = {
    ("Hà Nội", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "07:20", "price": 1_450_000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "14:00", "arrival": "15:20", "price": 2_800_000, "class": "business"},
        {"airline": "VietJet Air", "departure": "08:30", "arrival": "09:50", "price": 890_000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "11:00", "arrival": "12:20", "price": 1_200_000, "class": "economy"},
    ],
    ("Hà Nội", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "07:00", "arrival": "09:15", "price": 2_100_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "10:00", "arrival": "12:15", "price": 1_350_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "16:00", "arrival": "18:15", "price": 1_100_000, "class": "economy"},
    ],
    ("Hà Nội", "Hồ Chí Minh"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "08:10", "price": 1_600_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "07:30", "arrival": "09:40", "price": 950_000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "12:00", "arrival": "14:10", "price": 1_300_000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "18:00", "arrival": "20:10", "price": 3_200_000, "class": "business"},
    ],
    ("Hồ Chí Minh", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "09:00", "arrival": "10:20", "price": 1_300_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "13:00", "arrival": "14:20", "price": 780_000, "class": "economy"},
    ],
    ("Hồ Chí Minh", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "08:00", "arrival": "09:00", "price": 1_100_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "15:00", "arrival": "16:00", "price": 650_000, "class": "economy"},
    ],
}

HOTELS_DB = {
    "Đà Nẵng": [
        {"name": "Mường Thanh Luxury", "stars": 5, "price_per_night": 1_800_000, "area": "Mỹ Khê", "rating": 4.5},
        {"name": "Sala Danang Beach", "stars": 4, "price_per_night": 1_200_000, "area": "Mỹ Khê", "rating": 4.3},
        {"name": "Fivitel Danang", "stars": 3, "price_per_night": 650_000, "area": "Sơn Trà", "rating": 4.1},
        {"name": "Memory Hostel", "stars": 2, "price_per_night": 250_000, "area": "Hải Châu", "rating": 4.6},
        {"name": "Christina's Homestay", "stars": 2, "price_per_night": 350_000, "area": "An Thượng", "rating": 4.7},
    ],
    "Phú Quốc": [
        {"name": "Vinpearl Resort", "stars": 5, "price_per_night": 3_500_000, "area": "Bãi Dài", "rating": 4.4},
        {"name": "Sol by Meliá", "stars": 4, "price_per_night": 1_500_000, "area": "Bãi Trường", "rating": 4.2},
        {"name": "Lahana Resort", "stars": 3, "price_per_night": 800_000, "area": "Dương Đông", "rating": 4.0},
        {"name": "9Station Hostel", "stars": 2, "price_per_night": 200_000, "area": "Dương Đông", "rating": 4.5},
    ],
    "Hồ Chí Minh": [
        {"name": "Rex Hotel", "stars": 5, "price_per_night": 2_800_000, "area": "Quận 1", "rating": 4.3},
        {"name": "Liberty Central", "stars": 4, "price_per_night": 1_400_000, "area": "Quận 1", "rating": 4.1},
        {"name": "Cochin Zen Hotel", "stars": 3, "price_per_night": 550_000, "area": "Quận 3", "rating": 4.4},
        {"name": "The Common Room", "stars": 2, "price_per_night": 180_000, "area": "Quận 1", "rating": 4.6},
    ],
}

@tool
def search_flights(origin: str, destination: str) -> str:
    """
    Tìm kiếm các chuyến bay giữa hai thành phố.
    Tham số:
    origin: thành phố khởi hành (VD: 'Hà Nội', 'Hồ Chí Minh')
    destination: thành phố đến (VD: 'Đà Nẵng', 'Phú Quốc')
    Trả về danh sách chuyến bay với hãng, giờ bay, giá vé.
    Nếu không tìm thấy tuyến bay, trả về thông báo không có chuyến.
    """
    # TODO: Sinh viên tự triển khai
    # Tra cứu FLIGHTS_DB với key (origin, destination)
    flights = FLIGHTS_DB.get((origin, destination), [])
    
    if not flights:
        # Nếu không tìm thấy, thử tra ngược (destination, origin) xem có không
        flights = FLIGHTS_DB.get((destination, origin), [])
        if flights:
            # Nếu có chuyến ngược lại, trả về "Không tìm thấy chuyến bay từ X đến Y. Tuy nhiên, có chuyến bay từ Y đến X: ..." và liệt kê các chuyến bay đó.
            return f"Không tìm thấy chuyến bay từ {origin} đến {destination}. Tuy nhiên, có chuyến bay từ {destination} đến {origin}:\n"+ "\n".join([f"- {flight['airline']}: {flight['departure']} -> {flight['arrival']}, {flight['price']}₫ ({flight['class']})" for flight in flights])
        else:
            # Nếu cũng không có: "Không tìm thấy chuyến bay từ X đến Y."
            return f"Không tìm thấy chuyến bay từ {origin} đến {destination}."
    else:
        flight_info = []
        for flight in flights:
            # Nếu không có kết quả "Không tìm thấy chuyến bay từ X đến Y."
            formatted_price = f"{flight['price']:,.0f}".replace(",", ".")
            flight_info.append(f"- {flight['airline']}: {flight['departure']} -> {flight['arrival']}, {formatted_price}₫ ({flight['class']})")
        return "\n".join(flight_info)
    
    # Gợi ý: format giá tiền có dấu chấm phân cách (1.450.000₫)

@tool
def search_hotels(city: str, max_price_per_night: int = 99999999) -> str:
    """
    Tìm kiếm khách sạn tại một thành phố, có thể lọc theo giá tối đa mỗi đêm.
    Tham số:
    city: tên thành phố (VD: 'Đà Nẵng', 'Phú Quốc', 'Hồ Chí Minh')
    max_price_per_night: giá tối đa mỗi đêm (VNĐ), mặc định không giới hạn
    Trả về danh sách khách sạn phù hợp với tên, số sao, giá, khu vực, rating.
    """
    # TODO: Sinh viên tự triển khai
    # Tra cứu HOTELS_DB[city]
    hotels = HOTELS_DB.get(city, [])
    # Lọc theo max_price_per_night
    hotels = [hotel for hotel in hotels if hotel["price_per_night"] <= max_price_per_night]
    # Sắp xếp theo rating giảm dần
    hotels.sort(key=lambda x: x["rating"], reverse=True)
    # Nếu không có kết quả "Không tìm thấy khách sạn tại X với giá dưới Y/đêm. Hãy thử tăng ngân sách."
    if not hotels:
        return f"Không tìm thấy khách sạn tại {city} với giá dưới {max_price_per_night:,}₫/đêm. Hãy thử tăng ngân sách."
    
    hotel_info = []
    for hotel in hotels:
        # Format giá tiền có dấu chấm phân cách (1.200.000₫)
        formatted_price = f"{hotel['price_per_night']:,.0f}".replace(",", ".")
        hotel_info.append(f"- {hotel['name']} ({hotel['stars']} sao): {formatted_price}₫, {hotel['area']}, Rating: {hotel['rating']}")
    
    return "\n".join(hotel_info)

@tool
def calculate_budget(total_budget: int, expenses: str) -> str:
    """
    Tính toán ngân sách còn lại sau khi trừ các khoản chi phí.
    Tham số:
    total_budget: tổng ngân sách ban đầu (VNĐ)
    expenses: chuỗi mô tả các khoản chi, mỗi khoản cách nhau bởi dấu phẩy, định dạng 'tên khoản: số tiền' (VD: 'vé máy bay: 890000, khách sạn: 650000')
    Trả về bảng chi tiết các khoản chi và số tiền còn lại.
    Nếu vượt ngân sách, cảnh báo rõ ràng số tiền thiếu.
    """
    def format_vnd(amount: int) -> str:
        return f"{amount:,}".replace(",", ".")

    def extract_amount(text: str):
        # Ưu tiên lấy số đứng trước ký hiệu ₫ từ output của tools
        m = re.search(r"(\d[\d\.,_]*)\s*₫", text)
        raw = m.group(1) if m else text
        digits = re.sub(r"\D", "", raw)
        if not digits:
            return None
        return int(digits)

    if not expenses or not expenses.strip():
        return "Lỗi: expenses đang rỗng."

    lines = [line.strip() for line in expenses.splitlines() if line.strip()]
    if len(lines) <= 1:
        entries = [item.strip() for item in expenses.split(",") if item.strip()]
    else:
        entries = lines

    expense_dict = {}
    parsed_items = 0
    for idx, entry in enumerate(entries, start=1):
        amount = extract_amount(entry)
        if amount is None:
            continue

        name = None
        # Hỗ trợ định dạng thủ công: "tên khoản: số tiền"
        if ":" in entry and "->" not in entry:
            left, right = entry.split(":", 1)
            if extract_amount(right) is not None:
                name = left.strip().lstrip("-").strip()

        # Tự gán nhãn khi parse output từ search_flights/search_hotels
        if not name:
            if "->" in entry:
                name = "vé máy bay"
            elif "sao" in entry or "Rating" in entry:
                name = "khách sạn"
            else:
                name = f"chi phí {idx}"

        expense_dict[name] = expense_dict.get(name, 0) + amount
        parsed_items += 1

    if parsed_items == 0:
        return "Lỗi: Không đọc được chi phí. Hãy dùng 'tên khoản: số tiền' hoặc truyền output từ search_flights/search_hotels."

    # Tính tổng chi phí
    total_expenses = sum(expense_dict.values())

    # Tính số tiền còn lại = total_budget - tổng chi phí
    remaining_budget = total_budget - total_expenses
    # Format bảng chi tiết:
    # Bảng chi phí:
    # Vé máy bay: 890.000₫
    # Khách sạn: 650.000₫
    # Tổng chi: 1.540.000₫
    # Ngân sách: 5.000.000₫
    # Còn lại: 3.460.000₫
    # Nếu âm "Vượt ngân sách X đồng! Cần điều chỉnh."
    if remaining_budget < 0:
        return f"Vượt ngân sách {format_vnd(abs(remaining_budget))}₫! Cần điều chỉnh."

    # Format bảng chi tiết
    result = "Bảng chi phí:\n"
    for name, amount in expense_dict.items():
        formatted_amount = format_vnd(amount)
        result += f"- {name}: {formatted_amount}₫\n"
    result += f"Tổng chi: {format_vnd(total_expenses)}₫\n"
    result += f"Ngân sách: {format_vnd(total_budget)}₫\n"
    result += f"Còn lại: {format_vnd(remaining_budget)}₫"

    return result
