let generatedOTP = "";

function goToPage(type){

    localStorage.setItem("authType", type);

    window.location.href = "auth.html";
}

function exitSystem(){

    const confirmExit =
    confirm("Are you sure you want to exit?");

    if(confirmExit){

        localStorage.clear();

        window.location.href = "index.html";
    }
}

function recordVoice(){

    const status =
    document.getElementById("voiceStatus");

    status.innerHTML =
    "🎤 Recording Voice...";

    setTimeout(() => {

        status.innerHTML =
        "✅ Voice Recorded Successfully";

        localStorage.setItem(
        "voiceRecorded",
        "true");

    }, 3000);
}

function generateOTP(){

    generatedOTP =
    Math.floor(
    100000 + Math.random() * 900000
    ).toString();

    localStorage.setItem(
    "generatedOTP",
    generatedOTP);

    alert(
    "Your OTP is: " + generatedOTP);
}

function submitAuth(){

    const username =
    document.getElementById(
    "username").value;

    const password =
    document.getElementById(
    "password").value;

    const voice =
    localStorage.getItem(
    "voiceRecorded");

    if(username === "" ||
       password === ""){

        alert(
        "Please fill all fields");

        return;
    }

    if(voice !== "true"){

        alert(
        "Please record your voice");

        return;
    }

    generateOTP();

    window.location.href =
    "otp.html";
}

function verifyOTP(){

    const enteredOTP =
    document.getElementById(
    "otp").value;

    const realOTP =
    localStorage.getItem(
    "generatedOTP");

    const status =
    document.getElementById(
    "otpStatus");

    if(enteredOTP === realOTP){

        status.innerHTML =
        "✅ OTP Verified Successfully";

        status.style.color =
        "#00ff88";

    } else {

        status.innerHTML =
        "❌ OTP Rejected";

        status.style.color =
        "red";
    }
}