---
<div align="center">
  <h1 align="center">
    <img src="icon.png" width="200"/>
    <br/>
      ok-ww
  </h1> 
<h3><i>Tự động hóa trò chơi Wuthering Waves bằng thị giác máy tính và Win32API</i></h3>
</div>

![Static Badge](https://img.shields.io/badge/platfrom-Windows-blue?color=blue)
[![GitHub release (with filter)](https://img.shields.io/github/v/release/ok-oldking/ok-wuthering-waves)](https://github.com/ok-oldking/ok-wuthering-waves/releases)
[![GitHub all releases](https://img.shields.io/github/downloads/ok-oldking/ok-wuthering-waves/total)](https://github.com/ok-oldking/ok-wuthering-waves/releases)
[![Discord](https://img.shields.io/discord/296598043787132928?color=5865f2\&label=%20Discord)](https://discord.gg/vVyCatEBgA)

### Tài liệu tiếng Việt | [中文说明 (Tiếng Trung)](README.md) | [English (Tiếng Anh)](README_en.md) 

![img.png](readme/img.png)
![img\_1.png](readme/img_1.png)

---

## 🧩 **Tính năng chính**

* Hoạt động **ngay cả khi trò chơi chạy ở chế độ nền**
* Tự động **farm Boss Echo** (Dreamless, Jue, và các boss thế giới)
* **Một cú nhấp chuột** để hoàn thành toàn bộ **nhiệm vụ hàng ngày** và **Tacet Field**
* **Tự động chiến đấu** trong Abyss, bản đồ thế giới, Tacet Field, v.v.
* **Tự động bỏ qua hội thoại** trong các nhiệm vụ
* **Tự động nhặt vật phẩm** (Echo, hoa, rương...)
* Hỗ trợ **tất cả các ngôn ngữ trong game** (đa số tính năng đều hoạt động)

---

## ⚙️ **Cách sử dụng (chạy từ file .exe đã biên dịch)**

* Tải tệp `ok-ww.7z` từ mục phát hành (Releases) mới nhất.
* Giải nén và **nhấp đúp vào `ok-ww.exe`** để chạy chương trình.

---

## 🐍 **Cách sử dụng (chạy từ mã nguồn Python)**

Sử dụng **Python 3.12**, các phiên bản khác có thể không tương thích.

```bash
# Phiên bản chạy bằng CPU
git clone https://github.com/ok-oldking/ok-wuthering-waves
pip install -r requirements.txt --upgrade   # Cài các thư viện cần thiết, có thể phải chạy lại sau khi cập nhật mã nguồn
python main.py          # Chạy bản phát hành chính
python main_debug.py    # Chạy bản debug
```

---

## 💻 **Tham số dòng lệnh**

```bash
ok-ww.exe -t 1 -e
```

* `-t` hoặc `--task`: chỉ định **số nhiệm vụ** cần tự động thực hiện khi khởi động. `1` tương ứng với **nhiệm vụ đầu tiên (chạy nhanh một lần)**.
* `-e` hoặc `--exit`: thêm tùy chọn này để chương trình **tự thoát** sau khi hoàn thành nhiệm vụ.

---

## ⚙️ **Cài đặt cần thiết trong trò chơi**

(Ảnh minh họa thiết lập được đính kèm trong README gốc.)

* Đặt độ sáng, tắt HDR, các chế độ bảo vệ mắt, và dùng phím tắt mặc định.
* Tắt hiển thị thông tin FPS hoặc GPU từ phần mềm bên thứ ba.

---

## ❓ **Câu hỏi thường gặp (FAQ)**

1. **Cài đặt:** Cài vào thư mục chỉ có ký tự tiếng Anh, **KHÔNG** cài vào *Program Files*.
2. **Chống virus:** Thêm thư mục tải và giải nén vào danh sách loại trừ của Windows Defender/Antivirus.
3. **Hiển thị:** Tắt HDR, chế độ bảo vệ mắt, quản lý màu tự động; giữ độ sáng mặc định của game.
4. **Phím tắt tùy chỉnh:** Nếu bạn thay đổi phím mặc định, hãy cài lại trong phần cài đặt ứng dụng.
5. **Phiên bản cũ:** Hãy chắc rằng bạn đang dùng phiên bản mới nhất của **ok-ww**.
6. **Hiệu năng:** Duy trì **60 FPS ổn định**, giảm độ phân giải nếu cần.
7. **Ngắt kết nối:** Nếu bị mất kết nối, hãy mở game trước 5 phút rồi khởi chạy bot, hoặc giữ game mở và đăng nhập lại khi bị lỗi.
8. **Hỗ trợ thêm:** Báo lỗi (bug report) trên GitHub nếu sự cố vẫn xảy ra.

---

## ⚖️ **Tuyên bố miễn trừ trách nhiệm**

Phần mềm này là **công cụ bên ngoài** được tạo ra nhằm **tự động hóa các thao tác trong trò chơi “Wuthering Waves”**.
Công cụ chỉ tương tác với **giao diện người dùng hiện có** và **tuân thủ các quy định, pháp luật hiện hành**.
Mục đích chính là **đơn giản hóa thao tác cho người chơi** mà **không can thiệp, sửa đổi hay phá vỡ cân bằng trò chơi**.
Phần mềm **không chỉnh sửa tệp hoặc mã game gốc**.

Dự án là **mã nguồn mở và miễn phí**, chỉ dùng cho **mục đích học tập, nghiên cứu cá nhân**, không được phép sử dụng cho **mục đích thương mại hoặc trục lợi**.
Nhóm phát triển giữ quyền giải thích cuối cùng.
Mọi rủi ro hoặc hậu quả do người dùng tự chịu trách nhiệm.
Nếu phát hiện người khác **bán hoặc sử dụng phần mềm này cho dịch vụ trả phí**, đó là hành vi cá nhân trái phép, không thuộc phạm vi dự án này.
Các bản bị rao bán có thể chứa **mã độc, virus hoặc đánh cắp tài khoản**, nhóm phát triển **không chịu trách nhiệm** với những hậu quả đó.

---

## 💰 **Tài trợ**

* Chứng chỉ ký mã (code signing) được cung cấp miễn phí bởi [SignPath.io](https://signpath.io/),
  chứng chỉ được tài trợ bởi [SignPath Foundation](https://signpath.org/).

---

## 🔗 **Dự án liên quan**

* [ok-genshin-impact](https://github.com/ok-oldking/ok-genshin-impact) – Tự động hóa Genshin Impact.
* [ok-gf2](https://github.com/ok-oldking/ok-gf2) – Tự động hóa Girls Frontline 2 (chỉ hỗ trợ tiếng Trung giản thể).

---

## 🙌 **Cảm ơn**

Cảm ơn dự án gốc: [https://github.com/lazydog28/mc_auto_boss](https://github.com/lazydog28/mc_auto_boss)

---
hình ảnh.
