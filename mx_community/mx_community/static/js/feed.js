function createPost() {
    var form = document.getElementById("post-form");
    console.log('js')
    form.submit();
}

function showChat() {
    chats = document.getElementById('conversation');

    if (chats.style.display = 'none') {
        chats.style.display = 'block';
        document.getElementById('hidechat').innerText = 'Hide Chats'
    }
    else if (chats.style.display = 'block'){
        chats.style.display = 'none';
        document.getElementById('hidechat').innerText = 'Show Chats'
    }
}