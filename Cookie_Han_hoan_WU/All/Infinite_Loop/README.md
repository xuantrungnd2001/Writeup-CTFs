# Infinite Loop

Cuộc đời luôn là vậy. Một giây trước tưởng đã cùng đường, một giây sau có lại đầy hy vọng. Các chiến binh đã có công cụ mạnh mẽ trong tay, hãy dùng nó để can thiệp dòng chảy.

> http://chal6.web.letspentest.org/

---

Mình vào web đăng nhập bằng 1 tài khoản bất kì thì hiện thông báo trang không hoạt động:

> ![](1.png)

Tuy nhiên khi để ý kĩ thì mình phát hiện ra một điều. So với lúc đầu thì id trên URL đã thay đổi. Và thế là mình kiếm tra source code:

> ![](2.png)

Mình tìm thấy các id chạy từ 0 đến 10. Mình thử đem vào BurpSuite để brute id và tìm kết quả:

> ![](3.png)

Mình cho id chạy từ 0 đến 10:

> ![](4.png)

Lọc response theo lenght giảm dần:

> ![](5.png)

**Flag{Y0u_c4ptur3_m3_xD!!!}**
