
# 1.OPTICAL CHARACTER RECOGNITION VIETNAMESE (Handwritten), Classification Text, Spell Correction
( Nhận diện địa chỉ viết tay tiếng viêt, Nhận diện chữ số, Phân loại văn bản, Sửa lỗi chính tả)
# 2. Giới thiệu đề tài
Ngày nay, trí tuệ nhân tạo đang ngày càng thể hiện vai trò vô cùng quan trọng trong công việc cũng như cuộc sống con người. Có rất nhiều ứng dụng đã được áp dụng vào đời sống hằng ngày như: google dịch, xe ô tô tự lái, hệ thống gợi ý mua bán hàng, hệ thống nhận diện khuôn mặt...
Trong số đó, xử lý ngôn ngữ tự nhiên đang trở thành một lĩnh vực "nóng", hứa hẹn sẽ ứng dụng rất nhiều vào cuộc sống con người.
Dự án lần này sẽ xây dựng một hệ thống trong lĩnh vực nói trên với bài toán  nhận dạng chữ viết tay tiếng Việt, qua đó có thể áp dụng vào thực tiễn để giải quyết công việc nhập liệu các đơn khai chứng từ vào cơ sở dữ liệu.
Hiện nay đã có nhiều phương pháp để giải quyết bài toán này, và với những ưu điểm vượt trội từ Deeplearning, dự án sẽ áp dụng phương pháp này vào đề tài của mình, với mong muốn đem lại kết quả tốt nhất có thể.
## 2.1. Mục đích:
Tạo ra một app, web với nhiệm vụ giúp các cán bộ nhân viên dễ dàng hơn trong việc sao lưu các dữ liệu vào hệ thống từ các form điền của người dùng. Tiết kiệm được thời gian, nguồn nhân lực. Các dữ liệu này được lưu một cách đồng bộ, thống nhất giúp việc truy xuất dữ liệu dễ dàng hơn
Nghiên cứu:
- Nhận diện địa chỉ viết tay tiếng việt
- Nhận diện chữ số viết tay
- Phân loại văn bản
- Sửa lỗi chính tả
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
* Link driver: https://drive.google.com/drive/folders/1sLmY2FHFRHH5oC4k9_yuQdUs-oNvwaLK?fbclid=IwAR2_Ws7fTblHkbvp6YQ94RVoDFl9IJw2QqcVAzurjlk27JROIWKQDzW0ws8
* Liên hệ: fb: https://www.facebook.com/profile.php?id=100038801181933
# 3. Giao diện ứng dụng
** Giao diện regconition address **
<img src ='/display/address.png'>
** Giao diện regconition id **
<img src ='/display/id.png'>
** Giao diện classification text **
<img src ='/display/class.png'>
** Giao diện spell correction **
<img src ='/display/spell.png'>
# 4. Môi trường cài đặt 
- **python3 **
- tensorflow 1.14
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
- https://viblo.asia/p/deep-learning-thiet-ke-module-ocr-cho-bai-toan-nhan-dien-chu-co-nhat-ban-building-ocr-module-for-kuzushiji-recognition-V3m5WPngKO7?fbclid=IwAR3qWOk7_Jx1vAyWMwv1hJqnGXAu5g3CvaBQ4_tTScQ8_jKp-ZokiXeSFk8
- https://medium.com/@RaghavPrabhu/understanding-of-convolutional-neural-network-cnn-deep-learning-99760835f148
- https://towardsdatascience.com/understanding-neural-networks-from-neuron-to-rnn-cnn-and-deep-learning-cd88e90e0a90