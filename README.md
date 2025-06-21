# Django-Project-Social-Media,

this is colabrative project with Atarva Deshmukh Sumit Shelwane and Rajvardhan.
    Admin Login 
    UserName=admin
    emailid=atharvad2366@gmail.com
    password=ASRO2366

Setup Notes
    
    python -m venv env
    
    env\Scripts\activate
    
    pip install django
    
    git clone https://github.com/ATHARVA-DESHMUKH-23/Django-Project-Social-Media.git
    
    cd Django-Project-Social-Media/social_book
    
    python manage.py runserver

PULL notes
    git pull --rebase origin

PUSH BACK notes

    git status
    git add .
    git commit -m 'modified'
    git push origin main

testing push request

update status
    - 20june25 Atharva : basic setup + routing.

[video link](https://www.youtube.com/watch?v=xSUm6iMtREA&t=291s) 

### Sumit Task: Backend Auth (Login, Signup, Account)
#### 🎥 Video Sections:
- (1:00:31) Signup

- (1:33:11) Signin and Logout

- (1:47:55) Account Settings

#### 🗂️ Files/Directories:
- [ ] core/views.py → signup, signin, logout, settings

- [ ] core/urls.py

- [ ] templates/signup.html

- [ ] templates/signin.html

- [ ] templates/setting.html

- [ ] core/models.py (for any user/profile link)

- [ ] social_book/settings.py (for auth settings)

### 🎨 Rajvardhan Deshmukh: Frontend UI (Templates, Static Files)
#### 🎥 Video Sections:
- (0:23:06) Template Setup

- (0:27:52) Static Files

- (2:49:55) Post Feed UI

- (3:20:50) Profile Page

- (4:18:35) Download Images

- (4:38:18) User Suggestions

#### 🗂️ Files/Directories:
- [ ] templates/ → index.html, profile.html, search.html, setting.html, etc.

- [ ] static/ → all CSS/JS/image folders

- [ ] media/ → placeholder assets

### 🔌Athrva DEshmukh: API + Logic (Posts, Likes, Follow)
#### 🎥 Video Sections:
- (0:36:47) Profile Model

- (2:17:00) Uploading Post

- (3:00:22) Like Post

- (3:37:20) Follow and Unfollow User

- (4:10:23) Post Feed Updated

- (4:21:03) Search User

#### 🗂️ Files/Directories:
- [x] core/models.py → Profile, Post, Like, Follow models

- [ ] core/views.py → upload post, like/unlike, follow/unfollow, search

- [ ] core/admin.py → register models

- [ ] core/migrations/

- [ ] media/post_images/, media/profile_images/
