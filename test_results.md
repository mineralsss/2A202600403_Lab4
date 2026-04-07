## Case 1 - Direct Answer
```
C:\Users\tuana\Lab4>python C:\Users\tuana\Lab4\agent.py
============================================================
TravelBuddy - Trợ lý Du lịch Thông minh
 Gõ 'quit' để thoát
============================================================

Bạn: Xin chào ! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu

TravelBuddy đang suy nghĩ...
Trả lời trực tiếp

TravelBuddy: Chào bạn! Thật tuyệt khi bạn đang có kế hoạch đi du lịch. Bạn đã có ý tưởng nào về điểm đến chưa? Hoặc bạn có điều kiện về ngân sách và thời gian không? Mình có thể gợi ý cho bạn một số địa điểm thú vị ở Việt Nam.

Bạn:
```

## Case 2 - Single Tool Call
``` 
C:\Users\tuana\Lab4>python C:\Users\tuana\Lab4\agent.py
============================================================
TravelBuddy - Trợ lý Du lịch Thông minh
 Gõ 'quit' để thoát
============================================================

Bạn: Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng

TravelBuddy đang suy nghĩ...
Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})
Trả lời trực tiếp

TravelBuddy: Dưới đây là thông tin về các chuyến bay từ Hà Nội đi Đà Nẵng:

1. **Vietnam Airlines**:
   - Giờ bay: 06:00 -> 07:20
   - Giá vé: 1.450.000 ₫ (economy)

2. **Vietnam Airlines**:
   - Giờ bay: 14:00 -> 15:20
   - Giá vé: 2.800.000 ₫ (business)

3. **VietJet Air**:
   - Giờ bay: 08:30 -> 09:50
   - Giá vé: 890.000 ₫ (economy)

4. **Bamboo Airways**:
   - Giờ bay: 11:00 -> 12:20
   - Giá vé: 1.200.000 ₫ (economy)

Nếu bạn cần thêm thông tin hoặc muốn đặt vé, hãy cho mình biết nhé!

Bạn:

```

## Case 3 - Multi-Step Tool Chaining
```
C:\Users\tuana\Lab4>python C:\Users\tuana\Lab4\agent.py
============================================================
TravelBuddy - Trợ lý Du lịch Thông minh
 Gõ 'quit' để thoát
============================================================

Bạn: Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!

TravelBuddy đang suy nghĩ...
Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})
Gọi tool: search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 2500000})
Trả lời trực tiếp

TravelBuddy: Chuyến bay:
- Chọn hãng VietJet Air, chuyến bay 16:00 -> 18:15, giá vé 1.100.000₫ (economy).

Khách sạn:
- Lahana Resort (3 sao): 800.000₫/đêm, tổng chi phí cho 2 đêm là 1.600.000₫.

Tổng chi phí ước tính:
- Vé máy bay: 1.100.000₫
- Khách sạn: 1.600.000₫
- Tổng cộng: 2.700.000₫

Gợi ý thêm: Bạn còn dư ra 2.300.000₫ cho các hoạt động vui chơi, ăn uống trên đảo. Hãy nhớ thử những món hải sản ngon và tham gia các tour khám phá đảo nhé!

Bạn:
```

## Case 4 - Missing Info / Clarification 
```
C:\Users\tuana\Lab4>python C:\Users\tuana\Lab4\agent.py
============================================================
TravelBuddy - Trợ lý Du lịch Thông minh
 Gõ 'quit' để thoát
============================================================

Bạn: Tôi muốn đặt khách sạn

TravelBuddy đang suy nghĩ...
Trả lời trực tiếp

TravelBuddy: Mình rất vui được giúp bạn! Bạn có thể cho mình biết bạn muốn đặt khách sạn ở đâu và ngân sách tối đa mỗi đêm là bao nhiêu không?

Bạn:
```

## Case 5 - Guardrial / Refusial
```
C:\Users\tuana\Lab4>python C:\Users\tuana\Lab4\agent.py
============================================================
TravelBuddy - Trợ lý Du lịch Thông minh
 Gõ 'quit' để thoát
============================================================

Bạn: Giải giúp tôi bài tập lập trình Python về linked list

TravelBuddy đang suy nghĩ...
Trả lời trực tiếp

TravelBuddy: Xin lỗi, mình không thể giúp bạn với yêu cầu đó. Nhưng nếu bạn cần hỗ trợ về du lịch, mình rất vui lòng giúp! Bạn có dự định đi đâu hoặc cần tư vấn gì về chuyến đi?

Bạn:
```

## Case 6 - No Direct Route / Alternative Suggestion
```
C:\Users\tuana\Lab4>python C:\Users\tuana\Lab4\agent.py
============================================================
TravelBuddy - Trợ lý Du lịch Thông minh
 Gõ 'quit' để thoát
============================================================

Bạn: tìm cho tôi chuyến bay từ hà nội đi côn đảo

TravelBuddy đang suy nghĩ...
Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Côn Đảo'})
Trả lời trực tiếp

TravelBuddy: Rất tiếc, hiện tại không có chuyến bay từ Hà Nội đến Côn Đảo. Bạn có thể xem xét các hướng đi khác hoặc các chặng bay trung gian qua thành phố khác như Hồ Chí Minh nếu bạn muốn khám phá Côn Đảo. Bạn có muốn tôi tìm chuyến bay từ Hà Nội đến Hồ Chí Minh trước không?

Bạn:
```

## Case 7 - Reverse Route Suggestion
```
C:\Users\tuana\Lab4>python C:\Users\tuana\Lab4\agent.py
============================================================
TravelBuddy - Trợ lý Du lịch Thông minh
 Gõ 'quit' để thoát
============================================================

Bạn: Tôi muốn tìm chuyến bay từ Hồ Chí Minh đi Hà Nội

TravelBuddy đang suy nghĩ...
Gọi tool: search_flights({'origin': 'Hồ Chí Minh', 'destination': 'Hà Nội'})
Trả lời trực tiếp

TravelBuddy: Hơi tiếc là hiện tại mình không tìm thấy chuyến bay từ Hồ Chí Minh đến Hà Nội. Nhưng có một số chuyến bay từ Hà Nội về Hồ Chí Minh mà bạn có thể tham khảo:

1. **Vietnam Airlines**: 06:00 -> 08:10, giá 1.600.000₫ (economy)
2. **VietJet Air**: 07:30 -> 09:40, giá 950.000₫ (economy)
3. **Bamboo Airways**: 12:00 -> 14:10, giá 1.300.000₫ (economy)
4. **Vietnam Airlines**: 18:00 -> 20:10, giá 3.200.000₫ (business)

Nếu bạn có thể thay đổi kế hoạch hoặc cần thêm thông tin, cứ cho mình biết nhé!

Bạn:
```

## Case 8 - Follow-up Destination Change / Context Preservation
```
C:\Users\tuana\Lab4>python C:\Users\tuana\Lab4\agent.py
============================================================
TravelBuddy - Trợ lý Du lịch Thông minh
 Gõ 'quit' để thoát
============================================================

Bạn: Tôi muốn tìm chuyến bay từ Hồ Chí Minh đi Hà Nội

TravelBuddy đang suy nghĩ...
Gọi tool: search_flights({'origin': 'Hồ Chí Minh', 'destination': 'Hà Nội'})
Trả lời trực tiếp

TravelBuddy: Hơi tiếc là hiện tại mình không tìm thấy chuyến bay từ Hồ Chí Minh đến Hà Nội. Nhưng có một số chuyến bay từ Hà Nội về Hồ Chí Minh mà bạn có thể tham khảo:

1. **Vietnam Airlines**: 06:00 -> 08:10, giá 1.600.000₫ (economy)
2. **VietJet Air**: 07:30 -> 09:40, giá 950.000₫ (economy)
3. **Bamboo Airways**: 12:00 -> 14:10, giá 1.300.000₫ (economy)
4. **Vietnam Airlines**: 18:00 -> 20:10, giá 3.200.000₫ (business)

Nếu bạn có thể thay đổi kế hoạch hoặc cần thêm thông tin, cứ cho mình biết nhé!

Bạn: tôi bây giờ lại muốn đi đà nẵng

TravelBuddy đang suy nghĩ...
Gọi tool: search_flights({'origin': 'Hồ Chí Minh', 'destination': 'Đà Nẵng'})
Trả lời trực tiếp

TravelBuddy: Dưới đây là các chuyến bay từ Hồ Chí Minh đến Đà Nẵng mà bạn có thể tham khảo:

1. **Vietnam Airlines**: 09:00 -> 10:20, giá 1.300.000₫ (economy)
2. **VietJet Air**: 13:00 -> 14:20, giá 780.000₫ (economy)

Nếu bạn cần đặt vé hoặc tìm thêm thông tin về khách sạn cũng như chi phí khác cho chuyến đi, hãy cho mình biết nhé!

Bạn:
```