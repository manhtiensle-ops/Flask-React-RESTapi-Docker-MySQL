
function transformLoginButton(username) {
    // Note: You need to add id="auth-container" to the <div> or <li> wrapping your Login button in the HTML
    const authContainer = document.getElementById('login_btn'); 
    
    if (!authContainer) return;

    // Replace the Login button with the User info and Logout button
    authContainer.outerHTML = `
    <div style="display: flex; align-items: center; gap: 15px; background: rgba(255, 255, 255, 0.08); padding: 6px 8px 6px 18px; border-radius: 30px; border: 1px solid rgba(255,255,255,0.1);">
        <span style="color: #e2e8f0; font-size: 15px;">
            Username: <strong style="color: #4a90e2; font-weight: 600; letter-spacing: 0.5px;">${username}</strong>
        </span>
        <button onclick="logout()" 
                style="background: #ef4444; border: none; color: white; padding: 8px 18px; border-radius: 20px; cursor: pointer; font-weight: 600; font-size: 14px; transition: all 0.2s;"
                onmouseover="this.style.backgroundColor='#dc2626'; this.style.transform='scale(1.05)';" 
                onmouseout="this.style.backgroundColor='#ef4444'; this.style.transform='scale(1)';">
            Logout
        </button>
    </div>
`;
}
async function verifySession() {
    try {
        const response = await fetch('/api/login', { 
            method: 'GET',
            credentials: 'include' 
        });

        if (response.status === 200) {
            // Assuming your backend returns something like: {"status": "authorized", "user": "JohnDoe"}
            const data = await response.json(); 
            if (data.user){
            transformLoginButton(data.user);
            }
        }
    } catch (error) {
        console.error("Failed to verify session:", error);
    }
}
async function logout() {
    try {
        // Because the cookie is (hopefully) HttpOnly, JS cannot delete it. 
        // We must tell the backend to clear the cookie for us.
        await fetch('/api/logout', { 
            method: 'POST',
            credentials: 'include'
        });
        
        // Force reload the page to reset the UI back to the "Login" button state
        window.location.reload();
    } catch (error) {
        console.error("Logout failed:", error);
    }
}


document.addEventListener("DOMContentLoaded", function() {
    verifySession();
});
document.getElementById("login_btn").addEventListener("click",()=>{
    alert("transiting...")
    window.location.href = "/login";
})