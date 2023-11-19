# crawl_shopee
- Crawl tất cả các sản phẩm thuộc các nhóm hàng lớn liệt kê ở trang chủ của  shopee.vn
- Phương pháp: lấy API các giá trị trả về từ web  từ đó lấy ra các thông tin cần thiết ( file shoppe.postman_collection.json)

 - Số lượng sản phẩm lấy được trong 1 phút ( phụ thuộc vào đường truyền mạng và máy chạy )  :  trung bình ~300sp/1p
 - Tổng số sản phẩm lấy được : ~ 130.000 sản phẩm
 - File lưu trữ  kết quả : category_price_raw.csv

- Mô tả trường :
  +  display_parent_name : tên danh mục nhóm hàng 
  +  display_name : tên nhóm sản phẩm
  +   name : tên sản phẩm
  +   url : url sản phẩm
  +   ratingStar : điểm đánh giá trung bình
  +   price : giá tiền ( trung bình )
  +   revenue : doanh thu

- Techstack : Scrapy và MongoDB
