document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const message = document.getElementById('message');

    async function checkSystemStatus() {
    try {
        const response = await fetch('http://127.0.0.1:5000/');
        const data = await response.json();

        if (data.action === "redirect") {
            // Thực hiện lệnh mở trang login.html ở phía Frontend
            window.location.href = data.target; 
        }
    } catch (error) {
        console.error("Backend is offline!");
    }
    }
    checkSystemStatus();
    try {
        // Gửi POST request tới Flask API
        const response = await fetch('http://127.0.0.1:5000/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password }) // Chuyển sang JSON string
        });

        // const result = await response.json();

        // if (response.status === 200) {
        //     message.style.color = "#00ff88";
        //     message.innerText = result.message + ". Redirecting...";
        //     window.location.href = `http://127.0.0.1:5000${result.redirect_url}`;
        //     // Giả lập chuyển hướng sang trang admin
        //     setTimeout(() => alert("Access Granted! Welcome to /admin"), 1000);
        // } else {
        //     message.style.color = "#ff4d4d";
        //     message.innerText = result.message;
        // }
        //
                        // ... (giữ nguyên phần fetch) ...
            const result = await response.json();

            if (response.status === 200) {
                message.style.color = "#00ff88";
                message.innerText = "Access Granted. Initializing Dashboard...";
                
                // Chuyển hướng sau 1.5 giây để người dùng kịp thấy hiệu ứng
                setTimeout(() => {
                    window.location.href = result.redirect_url; 
                }, 1500);
            } else {
                message.style.color = "#ff4d4d";
                message.innerText = result.message;
            }
        //
    } catch (err) {
        message.innerText = "Error: Cannot connect to Backend!";
    }
});