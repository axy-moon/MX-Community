function createPost() {
    var form = document.getElementById("post-form");
    var postContent = document.getElementsByName('postcontent');
    if(postContent == '')
        alert("Content cannot be empty");
    else
        form.submit();
}

function showChat() {
    chats = document.getElementById('conversation');

        document.getElementById('hidechat').innerText = '';
        chats.style.display = 'block';

    }
function inputTitle() {
    var titleInput = document.getElementById('post-title');
    titleInput.style.display = 'flex';
}