document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault(); 

    const u = document.getElementById('username').value;
    const p = document.getElementById('password').value;
    const submitBtn = document.getElementById('submitBtn');
    const msgElement = document.getElementById('message');

    // --- HIỆU ỨNG UI: Trạng thái Loading ---
    submitBtn.disabled = true; // Khóa nút bấm
    submitBtn.textContent = "Đang xác thực..."; // Đổi chữ
    msgElement.textContent = ""; // Xóa thông báo cũ
    msgElement.style.opacity = "0"; // Ẩn thông báo

    // Gửi HTTP POST Request tới Backend của bạn qua cổng 5000
    fetch('http://localhost:8000/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: u, password: p })
    })
    .then(response => response.json().then(data => ({ status: response.status, body: data })))
    .then(result => {
        // --- HIỆU ỨNG UI: Khôi phục trạng thái nút bấm ---
        submitBtn.disabled = false;
        submitBtn.textContent = "Đăng Nhập";

        if (result.status === 200) {
            msgElement.style.color = "#a7ffeb"; // Màu xanh sáng cho nền tối
            msgElement.textContent = "Đăng nhập thành công! Đang chuyển hướng...";
            msgElement.style.opacity = "1"; // Hiện thông báo mượt mà
            // (Bạn có thể thêm logic chuyển hướng trang tại đây)
            setTimeout(() => {
            window.location.href = "controlpanel.html"; 
    }       , 1);

        } else {
            msgElement.style.color = "#ff8a80"; // Màu đỏ sáng cho nền tối
            // Bảo mật: Dùng textContent thay vì innerHTML để chống XSS
            msgElement.textContent = result.body.message || "Lỗi không xác định"; 
            msgElement.style.opacity = "1"; // Hiện thông báo mượt mà
        }
    })
    .catch(error => {
        // --- HIỆU ỨNG UI: Khôi phục trạng thái nút bấm khi lỗi mạng ---
        submitBtn.disabled = false;
        submitBtn.textContent = "Đăng Nhập";
        msgElement.style.color = "#ff8a80";
        msgElement.textContent = "Không thể kết nối tới Backend API.";
        msgElement.style.opacity = "1";
    });
});