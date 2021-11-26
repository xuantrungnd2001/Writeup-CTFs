# Gatling gun

Với chiếc Gatling gun mạnh mẽ trong tay, Mèo Yang Hồ có thể vượt qua bất kì cánh cửa bảo mật nào. Nhưng thật buồn cười là trong tay hắn lại không có một viên đạn nào.

Nếu bạn muốn nghịch súng với Mèo thì hãy đi nhặt đạn ở trong Github của Cookie Hân Hoan nhé.

> http://chal9.web.letspentest.org/

---

Mình vào web và đã thử đăng nhập thì thấy Flag giả:

> ![](1.png)

Ở 1 challenge github của giải. Mình tìm thấy github của cookie hân hoan và thấy có 1 vài folder có vẻ khá hữu ích ở bài này:

> ![](2.png)

Down file zip về

> [HoangTuEch.zip](HoangTuEch-main.zip)

Mình dùng Burp để Brute 3 trường tương ứng với 3 file .txt tìm được:

> ![](3.png)

Xác định được rằng có khá nhiều request, và có sự xuất hiện của Flag giả. Nên mình tiến hành Grep_Extract:

> ![](4.png)

Mình brute và lọc kết quả theo response length không có Flag giả:

> ![](5.png)

**FLAG{e6c068faf9241fe9d1f2000516718377}**
