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

function rollVal()
{
    var regroll = document.getElementById("regroll").value;
    var regex=/[1-9]{2}MX[0-9]{3}/;
    if(regex.test(regroll)==true)
    {
        
    }
    else
    {
        alert("Enter a valid Roll Number");
    }
}

function regpass()
{
    var regpassword=document.getElementById("regpassword").value;
    var regex=/[1-9]{2}mx[0-9]{3}/;
    if(regex.test(regpassword)==true)
    {
       
    }
    else
    {
         alert("Incorrect Password");
    }
}

