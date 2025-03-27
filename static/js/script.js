function calculate() {
    const electricityUsage = document.getElementById('electricity').value;
    
    if (!electricityUsage) {
        alert('กรุณากรอกปริมาณการใช้ไฟฟ้า');
        return;
    }

    // ส่งข้อมูลไปที่ backend
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ electricity_usage: electricityUsage })
    })
    .then(response => response.json())
    .then(data => {
        // แสดงผลลัพธ์
        document.getElementById('carbon-value').textContent = data.carbon_footprint;
        document.getElementById('trees-count').textContent = data.trees;
        document.getElementById('result').style.display = 'block';
        
        // เอฟเฟ็กต์动画
        animateValue('carbon-value', 0, data.carbon_footprint, 1000);
        animateValue('trees-count', 0, data.trees, 1000);
    });
}

// ฟังก์ชันทำให้ตัวเลขค่อยๆ เพิ่มขึ้น
function animateValue(id, start, end, duration) {
    let startTimestamp = null;
    const element = document.getElementById(id);
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        const value = Math.floor(progress * (end - start) + start);
        element.textContent = value;
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}