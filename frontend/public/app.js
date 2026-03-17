

 
fetch('/api/login', {
    method: 'GET',
    headers: { 'Content-Type': 'application/json' },
    credentials: 'same-origin'
})
.then(async response => {
    
    const statusCode = response.status;
    
    const data = await response.json(); 

    console.log(`Server trả về mã: ${statusCode}`, data);

    if (statusCode === 200) {
        console.log("Cookie hợp lệ! Đang chuyển hướng...");
        
        alert(`Welcome ${data.user}`); 
        
        const urlParams = new URLSearchParams(window.location.search);
        const nextUrl = urlParams.get('next') || '/';
        window.location.replace(nextUrl);
        
    } else {
        console.log("Chưa có Cookie hoặc bị từ chối truy cập. Ở lại trang Login.");
    }
})
.catch(error => {
    console.error("Lỗi khi kết nối tới server:", error);
});




document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault(); 

    const u = document.getElementById('username').value;
    const p = document.getElementById('password').value;
    const submitBtn = document.getElementById('submitBtn');
    const msgElement = document.getElementById('message');

    submitBtn.disabled = true; // Khóa nút bấm
    submitBtn.textContent = "Đang xác thực..."; // Đổi chữ
    msgElement.textContent = ""; // Xóa thông báo cũ
    msgElement.style.opacity = "0"; // Ẩn thông báo

    
    fetch('/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'same-origin',
        body: JSON.stringify({ username: u, password: p })
    })
    .then(response => response.json().then(data => ({ status: response.status, body: data })))
    .then(result => {
        submitBtn.disabled = false;
        submitBtn.textContent = "Đăng Nhập";

        if (result.status === 200) {
            msgElement.style.color = "#a7ffeb"; // Màu xanh sáng cho nền tối
            msgElement.textContent = "Đăng nhập thành công! Đang chuyển hướng...";
            msgElement.style.opacity = "1"; // Hiện thông báo mượt mà
            // (Bạn có thể thêm logic chuyển hướng trang tại đây)
            const urlParams = new URLSearchParams(window.location.search);
            const nextUrl = urlParams.get('next') || '/';
            window.location.replace(nextUrl);
            alert(`goto ${nextUrl}`)

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

