# Header 401

Để nhiều loại Trình duyệt và Web Server có thể nói chuyện và hiểu được nhau thì họ phải sử dụng chung một giao thức có tên gọi là HTTP Protocol. Khi người dùng bắt đầu truy cập Web, trình duyệt sẽ chuyển những hành động của họ thành yêu cầu (Request) tới Web Server. Còn Web Server sẽ trả lời (Response) xem có thể đáp ứng hay từ chối cung cấp thông tin cho trình duyệt.

Hãy đoán xem trong thử thách này có những Header thú vị nào nha

> http://chal3.web.letspentest.org/

---

Mình vào web thấy có một thông báo "Hello GET Request. Nice to meet you <3". Sau khi check source code thì mình còn thấy một thông tin khá thú vị:

> ![](1.png)

> Basic Authentication Credential: gaconlonton/cookiehanhoan

Mình tìm kiếm thông tin xem nó là thứ gì, và kết quả là:

> https://mixedanalytics.com/knowledge-base/api-connector-encode-credentials-to-base-64/

Mình tiến xây dựng được 1 header như sau **Authorization: Basic Z2Fjb25sb250b246Y29va2llaGFuaG9hbg==**

Sau đó mình sử dụng BurpSuite để thay đổi request, tuy nhiên kết quả cũng không khác :v

> ![](2.png)

Lúc này mình mới nghĩ đến việc thay đổi Request Method bởi response có nhắc đến phương thức của request. Đổi sang POST và mình có được flag:

> ![](3.png) > **Flag{m4g1c@l_h34d3r_xD}**
