# 1.OPTICAL CHARACTER RECOGNITION VIETNAMESE (Handwritten)
( Nhận diện nội dung trong form đăng kí)
# 2. Giới thiệu đề tài
Ngày nay, trí tuệ nhân tạo đang ngày càng thể hiện vai trò vô cùng quan trọng trong công việc cũng như cuộc sống con người. Có rất nhiều ứng dụng đã được áp dụng vào đời sống hằng ngày như: google dịch, xe ô tô tự lái, hệ thống gợi ý mua bán hàng, hệ thống nhận diện khuôn mặt...
Trong số đó, xử lý ngôn ngữ tự nhiên đang trở thành một lĩnh vực "nóng", hứa hẹn sẽ ứng dụng rất nhiều vào cuộc sống con người.
Dự án lần này sẽ xây dựng một hệ thống trong lĩnh vực nói trên với bài toán  nhận dạng chữ viết tay tiếng Việt, qua đó có thể áp dụng vào thực tiễn để giải quyết công việc nhập liệu các đơn khai chứng từ vào cơ sở dữ liệu.
Hiện nay đã có nhiều phương pháp để giải quyết bài toán này, và với những ưu điểm vượt trội từ Deeplearning, dự án sẽ áp dụng phương pháp này vào đề tài của mình, với mong muốn đem lại kết quả tốt nhất có thể.
<img src ='/display/form.png' style ='margin: auto'>
## 2.1. Mục đích:
Tạo ra một app, web với nhiệm vụ giúp các cán bộ nhân viên dễ dàng hơn trong việc sao lưu các dữ liệu vào hệ thống từ các form điền của người dùng. Tiết kiệm được thời gian, nguồn nhân lực. Các dữ liệu này được lưu một cách đồng bộ, thống nhất giúp việc truy xuất dữ liệu dễ dàng hơn
## 2.2. Mục tiêu:
Nắm rõ được các kiến thức cơ bản về machine learning, deep learning.
Sử dụng được thành thạo framework Keras, tensorflow
Nắm vững các mô hình của deep learning ( CNN, RNN )
Hoàn thành các nhiệm vụ được phân công đúng tiến độ
## 2.3. Thành viên
- Trần Trung Trực -16T3 (leader)
- Phạm Thế Tâm    -16T3
- Phan Thành Trung -16T2
- Võ Văn Phúc     -16T3
## 2.4. Data train, pretrain_model:
* Liên hệ: fb: https://www.facebook.com/profile.php?id=100038801181933
# 3. Giao diện ứng dụng
** Giao diện ban đầu **
<img src ='/display/before.png'>
** Giao diện sau khi dự đoán **
<img src ='/display/after.png'>
# 4. Môi trường cài đặt 
- **python3 **
- tensorflow 1.11
- flask
- ** CTCWordBeamSearch** => https://github.com/githubharald/CTCWordBeamSearch
- Ngoài ra còn 1 số thư viện có thể cài thêm trong quá trình chạy
# 5. Hướng dẫn chạy
- git clone https://github.com/githubharald/CTCWordBeamSearch.git
- python3 app.py
# 6. Hướng phát triển
Sau này có thể phát  triển phần mềm có thể nhận diện được nhiều form bất kì cho người dùng nhập vào. Từ bài này ta có thể phát triển ra nhiều đề tài mới như : chấm điểm chính tả cho học sinh tiểu học, nhận diện biển số, dịch văn bản viết tay tiếng việt
# 7. Tài liệu tham khảo
- https://viblo.asia/p/ung-dung-deep-learning-cho-bai-toan-nhan-dien-chu-viet-ocr-bWrZnaeQKxw?fbclid=IwAR0JIJ3JT43wseHUasv9rQN9IpHoDKuut8BDVwnXwzCH3OxFqjRmwppZUB0
- https://pbcquoc.github.io/vietnamese-ocr/?fbclid=IwAR2Xum1Gs5arhd6av8t10TgmDsGuWiG1Q6eRRyjjLubCACEsxPxhpB18iFk
- https://viblo.asia/p/deep-learning-thiet-ke-module-ocr-cho-bai-toan-nhan-dien-chu-co-nhat-ban-building-ocr-module-for-kuzushiji-recognition-V3m5WPngKO7?fbclid=IwAR3qWOk7_Jx1vAyWMwv1hJqnGXAu5g3CvaBQ4_tTScQ8_jKp-ZokiXeSFk8

