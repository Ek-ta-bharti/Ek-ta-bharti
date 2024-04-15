<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ekta Bharti's Profile</title>
  <style>
    /* Add your custom CSS styles here */
    /* Animations */
    @keyframes fadeIn {
      0% { opacity: 0; }
      100% { opacity: 1; }
    }
    @keyframes slideInFromLeft {
      0% { transform: translateX(-100%); }
      100% { transform: translateX(0); }
    }
    /* Other styles */
    body {
      font-family: Arial, sans-serif;
      background-color: #f0f0f0;
      margin: 0;
      padding: 0;
    }
    .container {
      max-width: 900px;
      margin: 20px auto;
      padding: 20px;
      background-color: #fff;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      animation: fadeIn 1s ease-in;
    }
    .profile-info {
      display: flex;
      align-items: center;
    }
    .profile-info img {
      border-radius: 50%;
      margin-right: 20px;
      animation: slideInFromLeft 1s ease-out;
    }
    .profile-details {
      flex-grow: 1;
    }
    .social-links {
      margin-top: 20px;
    }
    .social-links a {
      text-decoration: none;
      margin-right: 10px;
      transition: transform 0.3s ease-in-out;
    }
    .social-links a:hover {
      transform: translateY(-3px);
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="profile-info">
      <img src="https://user-images.githubusercontent.com/5713670/87202985-820dcb80-c2b6-11ea-9f56-7ec461c497c3.gif" width="150" alt="Profile Picture">
      <div class="profile-details">
        <h1>☁️ Hi there <img src="https://emojis.slackmojis.com/emojis/images/1577305505/7373/hand_wave.gif?1577305505" width="30"></h1>
        <h3>My Name is Ekta Bharti | I am a B.Tech CSE Student | Specialization in Cloud Computing and Information Technology | Interest in Full Stack Development</h3>
      </div>
    </div>
    <div class="social-links">
      <a href="https://github.com/ek-ta-bharti">
        <img src="https://img.shields.io/github/followers/ek-ta-bharti?label=follow&color=0000FF&style=social" alt="GitHub Followers">
      </a>
      <a href="https://www.youtube.com/channel/UCmQezsF1x1sCpaL7LikRzCg">
        <img src="https://img.shields.io/youtube/channel/subscribers/UCmQezsF1x1sCpaL7LikRzCg?label=Subscribers&style=social" alt="YouTube Subscribers">
      </a>
      <!-- Add more social media links here -->
    </div>
    <!-- Add more sections (About Me, Skills, Projects, etc.) here -->
  </div>
</body>
</html>
